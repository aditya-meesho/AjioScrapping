import os
import json
import logging

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


file_path = '../outputs/CategoryId/AllcategoryId.json'
data_list = []
DirectCuratedId = set()
IndirectCuratedId = set()

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

for i in data:
    for j in i:
        if len(j) != 0:
            data_list.extend(j)

for i in data_list:
    category_link = i.split('/')
    if category_link[1] == 's':
        DirectCuratedId.add(category_link[2])
    else:
        IndirectCuratedId.add(i)

file_path_DirectCuratedId = '../outputs/FilteredCategoryId/directCurateId.json'
file_path_IndirectCuratedId = '../outputs/FilteredCategoryId/indirectCurateId.json'
os.makedirs(os.path.dirname(file_path_DirectCuratedId), exist_ok=True)
os.makedirs(os.path.dirname(file_path_IndirectCuratedId), exist_ok=True)

with open(file_path_IndirectCuratedId, "w+") as json_file:
    json.dump(IndirectCuratedId, json_file, indent=4, cls=SetEncoder)

with open(file_path_DirectCuratedId, "w+") as json_file:
    json.dump(DirectCuratedId, json_file, indent=4, cls=SetEncoder)

logging.info("all categories data filtered")
