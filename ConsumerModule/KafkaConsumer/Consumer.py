from json import loads
import requests
from kafka import KafkaConsumer
from Scripts.ApiRequest import make_api_request
import csv
import time
import logging

url = 'https://www.ajio.com/api/category/83'
unique_record = set()
fields = ['pid', 'pid2', 'product_name', 'avg_rating', 'price', 'comp_category', 'product_url', 'image_urls', 'brands',
          'discount_price', 'others']


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def save_to_csv(data, currateId):
    global unique_record
    with open(f'../Outputs/{currateId}.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        reader = csv.reader(csvfile)

        if len(list(reader)) == 0:
            writer.writerow(fields)

        if is_iterable(data):
            for product in data:
                pid = product.get('url').rsplit('/', 1)[-1]
                if pid in unique_record:
                    continue
                else:
                    unique_record.add(pid)
                record = [
                    product.get('code'),
                    pid,
                    product.get('name'),
                    product.get('averageRating'),
                    product.get('price', {}).get('value'),
                    {
                        "l1": product.get('segmentNameText'),
                        "l2": product.get('verticalNameText'),
                        "l3": product.get('brickNameText')
                    },
                    'https://www.ajio.com' + product.get('url'),
                    {i['url'] for i in product.get('images', [])},
                    product.get('brandTypeName'),
                    product.get('offerPrice', {}).get('formattedValue'),
                    product
                ]
                writer.writerow(record)


my_consumer = KafkaConsumer(
    'category_topic',
    bootstrap_servers=['10.120.20.78:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    max_poll_records=50,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

max_retries = 3

for message in my_consumer:
    message = message.value
    # print("consumer reached")
    logging.info(f"category : {message['categoryId']}, pageNo : {message['pageNo']} / {message['totalPages']}")
    print(f"category : {message['categoryId']}, pageNo : {message['pageNo']} / {message['totalPages']}")
    api_data = None
    retry_count = 0
    while retry_count < max_retries:
        try:
            api_data = make_api_request(message['pageNo'], url, message['categoryId'])
            break
        except requests.Timeout:
            logging.error("Timeout occurred. Retrying...")
            logging.error(f"Consumer ,timeout occurred for message: {message}")
            retry_count += 1
            time.sleep(1)

    if api_data and api_data.status_code == 200:
        api_data = api_data.json()
        data = api_data.get('products')
        save_to_csv(data, message['categoryId'])
        # count=count+1
    else:
        logging.error(f"Consumer ,failed to retrieve with status code: {api_data.status_code}")

    # print(f"record added ,count = {count}")
