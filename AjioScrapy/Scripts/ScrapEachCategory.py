import json
from ApiRequest import make_api_request
from AjioScrapper.Kafka.KafkaProducer import ProduceEvent
import logging

url = 'https://www.ajio.com/api/category/83'
json_file_path = '../outputs/FilteredCategoryId/directCurateId.json'
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)


def InitalRequestForEachID(currateId):
    global url
    api_res = make_api_request(1, url, currateId)
    logging.info(f"initial request for  {currateId}  ->  status  {api_res.status_code}")
    data = api_res.json()
    pages = data['pagination']['totalPages']
    if api_res.status_code == 200:
        return pages
    else:
        logging.error(
            f"ScrapEachCategory.InitialRequestForEachID ,unable to fetch for category: {currateId} with status code : {api_res.status_code}")
        return None


for category in data:
    api_data = InitalRequestForEachID(category)
    if api_data is not None:
        for page in range(1, api_data + 1):
            value = {"categoryId": category, "pageNo": page, "totalPages": api_data}
            ProduceEvent(value, "category_topic")
        logging.info(f"ScrapEachCategory ,successfully pushed to kafka for category : {category}")
    else:
        logging.error(f"ScrapEachCategory ,unable to fetch for category : {category}")
    print(f"Required data for {category} category pushed in the kafka")
print("All Required data pushed in the Topic")
