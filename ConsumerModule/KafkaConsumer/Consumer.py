from json import loads

import requests
from kafka import KafkaConsumer
from Scripts.ApiRequest import make_api_request
import csv
import time

url = 'https://www.ajio.com/api/category/83'
my_consumer = KafkaConsumer(
    'category_topic',
    bootstrap_servers=['localhost : 9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)


def save_to_csv(data, currateId):
    with open(f'../Outputs/{currateId}.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for product in data:
            record = [
                product['code'] if 'code' in product else None,
                product['name'] if 'name' in product else None,
                product['averageRating'] if 'averageRating' in product else None,
                product['price']['value'] if 'price' in product and 'value' in product['price'] else None,

                {
                    "l1": product['segmentNameText'] if 'segmentNameText' in product else None,
                    "l2": product['verticalNameText'] if 'verticalNameText' in product else None,
                    "l3": product['brickNameText']
                } if 'brickNameText' in product else None,
                'https://www.ajio.com' + product['url'] if 'url' in product else None,
                {i['url'] for i in product.get('images', [])},
                product['brandTypeName'] if 'brandTypeName' in product else None,
                product['offerPrice']['formattedValue'] if 'offerPrice' in product and 'formattedValue' in product[
                    'offerPrice'] else None
            ]

            writer.writerow(record)
            print("record added for pid - " + product['code'])


max_retries=3
for message in my_consumer:
    message = message.value
    api_data=None
    retry_count=0
    while retry_count < max_retries:
        try:
            api_data = make_api_request(message['pageNo'], url, message['categoryId']).json()
            break
        except requests.Timeout:
            print("Timeout occurred. Retrying...")
            retry_count += 1
            time.sleep(1)

    # api_data = api_data.json()
    if api_data:
        data = api_data['products'] if 'products' in api_data else None
        save_to_csv(data, message['categoryId'])
