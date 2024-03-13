import os
import json
file_path = '../outputs/CategoryId/categoryId.txt'  # Replace 'your_file.txt' with the actual file path
data_list = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Remove trailing newline characters and whitespace
        elements = line.split()
        stripped_elements = [element[2:-2] for element in elements]
        data_list.append(stripped_elements[0])



DirectCuratedId=set()
IndirectCuratedId=set()

for i in data_list:
    items=i.split('/')
    if items[1]=='s':
        DirectCuratedId.add(items[2])
    else:
        IndirectCuratedId.add('/'.join(items))

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

file_path_DirectCuratedId = '../outputs/FilteredCategoryId/directCurateId.json'
file_path_IndirectCuratedId = '../outputs/FilteredCategoryId/indirectCurateId.json'
os.makedirs(os.path.dirname(file_path_DirectCuratedId), exist_ok=True)
os.makedirs(os.path.dirname(file_path_IndirectCuratedId), exist_ok=True)
for i in IndirectCuratedId:
    print(i)
with open(file_path_IndirectCuratedId, "w+") as json_file:
    json.dump(IndirectCuratedId, json_file, indent=4,cls=SetEncoder)

with open(file_path_DirectCuratedId, "w+") as json_file:
    json.dump(DirectCuratedId, json_file, indent=4,cls=SetEncoder)