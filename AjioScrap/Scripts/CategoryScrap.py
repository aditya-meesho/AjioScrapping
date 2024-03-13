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


# def save_to_json(data, filename, page, totalPage):
#     with open(f"../outputs/ProductData/RawJson/{filename}.json", 'a') as json_file:  # Append mode
#         json.dump(data, json_file, indent=4)
#         if page != totalPage:
#             json_file.write(',')
#         json_file.write('\n')
#         json_file.write('\n')


# for category in data:
#     # minor adjustment to file for future use
#     with open(f"../outputs/ProductData/RawJson/{category[0]}.json", 'a') as json_file:  # Append mode
#         json_file.write('[')
#         json_file.write('\n')
#
#     for page in range(1, category[1]+1):
#         print("current page -> "+str(page))
#         api_data = make_api_request(page, url, category[0])
#         api_data = api_data.json()
#         if api_data:
#             data=api_data['products'] if 'products' in api_data else None
#             save_to_json(data, category[0], page, category[1])
#             # print(api_data)
#         else:
#             print("Failed to fetch data from API.")
#
#     # minor adjustment to file for future use
#     with open(f"../outputs/ProductData/RawJson/{category[0]}.json", 'a') as json_file:  # Append mode
#         json_file.truncate()
#         json_file.truncate()
#         json_file.write(']')
#
#     ConvertToExcel(category[0])

def InitalRequestForEachID(currateId):

    url = 'https://www.ajio.com/api/category/83'
    api_res = make_api_request(1, url, currateId)
    print("initial request for ",currateId + "  ->  status ", api_res.status_code)
    data=api_res.json()
    pages=data['pagination']['totalPages']
    if api_res.status_code == 200:
        return pages
    else:
        return None



for category in data:
    print(category)
    api_data = InitalRequestForEachID(category)
    print(api_data)
    for page in range(1,api_data+1):
        value={"categoryId":category,"pageNo":page}
        ProduceEvent(value,"category_topic")
        sleep(100)



print("Data scrapping for Categories completed.")
