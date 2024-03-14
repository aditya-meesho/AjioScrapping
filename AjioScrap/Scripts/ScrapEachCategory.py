import json
import os
from ApiRequest import make_api_request
from AjioScrap.Utils.Kafka.KafkaProducer import ProduceEvent
from time import sleep

# from JsonToExcel import ConvertToExcel

url = 'https://www.ajio.com/api/category/83'
json_file_path = '../outputs/FilteredCategoryId/directCurateId.json'
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)


def InitalRequestForEachID(currateId):
    url = 'https://www.ajio.com/api/category/83'
    api_res = make_api_request(1, url, currateId)
    print("initial request for ", currateId + "  ->  status ", api_res.status_code)
    data = api_res.json()
    pages = data['pagination']['totalPages']
    if api_res.status_code == 200:
        return pages
    else:
        return None

for category in data:
    print(category)
    api_data = InitalRequestForEachID(category)
    print(api_data)
    for page in range(1, api_data + 1):
        value = {"categoryId": category, "pageNo": page}
        ProduceEvent(value, "category_topic")

print("All Required data pushed in the Topic")
