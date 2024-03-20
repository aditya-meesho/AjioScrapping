import csv
import json

# Define the path to your CSV file
csv_file_path = "../Outputs/data.csv"
csv_file_path2 = "../Outputs/footwear-4792-56592.csv"
csv_file_path3 = "../Outputs/jewellery-4461-75481.csv"


count=0
main_data=set()
scrapped_data=set()

with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        json_data=row[6]
        if not json_data:
            print("Empty JSON data. Skipping row.")
            continue

        try:
            parsed_data = json.loads(json_data)

            # l1 = parsed_data.get('l1')
            l2 = parsed_data.get('l2')
            # l3 = parsed_data.get('l3')

            # Process the data as needed
            # print("l1:", l1)
            # print("l2:", l2)
            if l2=='Silver Jewellery':
                main_data.add(row[21])
            # print("l3:", l3)

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data in row: {e}. Skipping row.")
            continue



# with open(csv_file_path2, mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for row in csv_reader:
#         json_data=row[5]
#         json_string = json_data.replace("'", '"')
#         if not json_data:
#             print("Empty JSON data. Skipping row.")
#             continue
#
#         try:
#             # print(json_string)
#             parsed_data = json.loads(json_string)
#
#             # l1 = parsed_data.get('l1')
#             l2 = parsed_data.get('l2')
#             # l3 = parsed_data.get('l3')
#
#             # Process the data as needed
#             # print("l1:", l1)
#             # print("l2:", l2)
#             if l2=='Footwear':
#                 scrapped_data.add(row[1])
#             # print("l3:", l3)
#
#         except json.JSONDecodeError as e:
#             print(f"Error parsing JSON data in row: {e}. Skipping row.")
#             continue

with open(csv_file_path3, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        json_data=row[5]
        json_string = json_data.replace("'", '"')
        if not json_data:
            print("Empty JSON data. Skipping row.")
            continue

        try:
            # print(json_string)
            parsed_data = json.loads(json_string)

            # l1 = parsed_data.get('l1')
            l2 = parsed_data.get('l2')
            # l3 = parsed_data.get('l3')

            # Process the data as needed
            # print("l1:", l1)
            # print("l2:", l2)
            if l2=='Silver Jewellery':
                scrapped_data.add(row[1])
            # print("l3:", l3)

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data in row: {e}. Skipping row.")
            continue

print(len(main_data))
print((len(scrapped_data)))
print(len(scrapped_data.intersection(main_data)))