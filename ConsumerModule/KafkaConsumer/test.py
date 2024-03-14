import csv

# Open the CSV file for reading
count=0
s=set()
l=[]
# with open('../clothing-4461-74581.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     with open('data.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#     # Iterate over each row in the CSV file
#         for row in reader:
#             # print(row[0])
#             if row[0] in s:
#                 continue
#             else:
#                 s.add((row[0]))
#                 writer.writerow(row)
#             # s.add(row[0])
#             # l.append(row[0])
#             # count=count+1
#
#               # Open file in append mode
#
#


with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        # print(row[0])
        count=count+1
            # s.add(row[0])
            # l.append(row[0])
            # count=count+1

            # Open file in append mode

print(count)
print(len(s))
print(len(l))