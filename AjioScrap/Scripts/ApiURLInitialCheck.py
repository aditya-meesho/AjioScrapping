import requests
import json
import os
from ApiRequest import make_api_request

ValidCurateID = []
InvalidCurateID=[]
def save_to_json(data, filename):
    with open(filename, 'a') as json_file:  # Append mode
        json.dump(data, json_file, indent=4)
        json_file.write('\n')  # Add a new line for each appended data

def InitalRequestForEachID(curateIdList):
    for i in curateIdList:
        url = 'https://www.ajio.com/api/category/83'
        currateId = i
        api_res = make_api_request(1, url, currateId)
        print(currateId + "  ->  ", api_res.status_code)
        data=api_res.json()
        pages=data['pagination']['totalPages']
        if api_res.status_code == 200:
            ValidCurateID.append([i,pages])
        else:
            InvalidCurateID.append(i)



json_file_path = '../outputs/FilteredCategoryId/directCurateId.json'
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

InitalRequestForEachID(data)



file_path_ValidCuratedId = '../outputs/FilteredCategoryId/Valid_Ids/ValidCuratedID.json'
file_path_InvalidCuratedId = '../outputs/FilteredCategoryId/Invalid_Ids/InvalidCuratedID.json'
os.makedirs(os.path.dirname(file_path_ValidCuratedId), exist_ok=True)
os.makedirs(os.path.dirname(file_path_InvalidCuratedId), exist_ok=True)

with open(file_path_InvalidCuratedId, "w+") as json_file:
    json.dump(InvalidCurateID, json_file, indent=4)

with open(file_path_ValidCuratedId, "w+") as json_file:
    json.dump(ValidCurateID, json_file, indent=4)