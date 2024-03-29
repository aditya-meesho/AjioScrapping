import pandas as pd
import json
from collections import defaultdict

def ConvertToExcel(filename):
    json_file = f'../outputs/ProductData/RawJson/{filename}.json'
    with open(json_file) as f:
        # Load the JSON data from the file
        data = json.load(f)
    df = pd.json_normalize(data)

    original=[]
    lis = set()
    d = defaultdict(list)

    for i in df:
        for j in df[i]:
            if j and 'code' in j:
                code = j['code']
                lis.add(code)
                original.append(code)

                data = {
                    "name": j['name'] if 'name' in j else None,
                    "averageRating": j['averageRating'] if 'averageRating' in j else None,
                    "price.value": j['price.value'] if 'price.value' in j else None,
                    "url": j['url'] if 'url' in j else None,
                    "brandTypeName": j['brandTypeName'] if 'brandTypeName' in j else None,
                    "offerPrice.formattedValue": j['offerPrice.formattedValue'] if 'offerPrice.formattedValue' in j else None
                }
                d[code].append(data)  # Append data to list associated with the code

    print(len(original))
    print(len(lis))  # Number of unique codes
    print(len(d))  # Number of unique codes in d (should match len(lis))

    d2 = {}
    for i in d:
        d2[i] = d[i][0]

    df_export = pd.DataFrame.from_dict(d2, orient='index')

    # Export the DataFrame to an Excel file
    excel_file = f'../outputs/ProductData/ExcelData/{filename}.xlsx'

    df_export.to_excel(excel_file)

    print(f"Data exported to '{excel_file}' successfully.")
