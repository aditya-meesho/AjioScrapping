import requests
import json
import os
from ApiRequest import make_api_request
import logging

ValidCurateID = []
InvalidCurateID = []
url = 'https://www.ajio.com/api/category/83'


def save_to_json(data, filename):
    with open(filename, 'a') as json_file:
        json.dump(data, json_file, indent=4)
        json_file.write('\n')


def InitalRequestForEachID(curateIdList):
    global url
    for i in curateIdList:
        currateId = i
        api_res = make_api_request(1, url, currateId)
        logging.info(currateId + "  ->  ", api_res.status_code)
        data = api_res.json()
        pages = data['pagination']['totalPages']
        if api_res.status_code == 200:
            ValidCurateID.append([i, pages])
        else:
            InvalidCurateID.append(i)


json_file_path = '../outputs/FilteredCategoryId/directCurateId.json'
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

InitalRequestForEachID(data)
logging.info("ApiURLInitialCheck , success")

file_path_ValidCuratedId = '../outputs/FilteredCategoryId/Valid_Ids/ValidCuratedID.json'
file_path_InvalidCuratedId = '../outputs/FilteredCategoryId/Invalid_Ids/InvalidCuratedID.json'
os.makedirs(os.path.dirname(file_path_ValidCuratedId), exist_ok=True)
os.makedirs(os.path.dirname(file_path_InvalidCuratedId), exist_ok=True)
sorted_ValidCurateID = sorted(ValidCurateID, key=lambda x: x[1])
with open(file_path_InvalidCuratedId, "w+") as json_file:
    json.dump(InvalidCurateID, json_file, indent=4)

with open(file_path_ValidCuratedId, "w+") as json_file:
    json.dump(sorted_ValidCurateID, json_file, indent=4)

logging.info("ApiURLInitialCheck , data exported successfully")
