import csv

# Open the CSV file for reading
with open('../Outputs/beauty-4384-57431.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over each row in the CSV file
    for row in reader:
        print(row)  # Print each row