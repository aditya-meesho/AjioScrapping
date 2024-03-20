
import csv

# Define the new record to be added
new_record = ['pid','pid2','product_name','avg_rating','price','comp_category','product_url','image_urls','brands','discount_price','others']

# Path to the CSV file
csv_file_path = '../Outputs/jewellery-4461-75481.csv'

# Read existing records from the CSV file
existing_records = []
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    existing_records = list(csv_reader)

# Insert the new record at the beginning
existing_records.insert(0, new_record)

# Write the modified records back to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(existing_records)

#
# # folder_path = '../Outputs/footwear-4792-56592.csv'
# folder_path = '../Outputs/data.csv'
#
# s1=set()
# with open(folder_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#     # Process each row as needed
#
#         # Replace single quotes with double quotes
#         corrected_json_str = row[6].replace("'", '"')
#
#         # Load JSON
#         try:
#             d = json.loads(corrected_json_str)
#             if d['l2']=='Footwear':
#                 print(d['l2'])
#             s1.add(row[0])
#         except json.JSONDecodeError:
#             print("Error: Invalid JSON format")
#
#         # Increment count if needed
#         count += 1
#
# print(count)
# # print(len(s))
# # print(len(l))
# Pid,Pid2,product_name,avg_rating,price,comp_category,product_url,image_urls,brands,discount_price,others