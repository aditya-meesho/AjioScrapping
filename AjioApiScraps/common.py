import requests
import json


def make_api_request(current_page, url, currateid):
    # url = 'https://www.ajio.com/api/category/83'
    params = {
        # 'fields':'SITE',
        'currentPage': current_page,
        'pageSize': 45,
        'format': 'json',
        'query': '%3Arelevance',
        'sortBy': 'relevance',
        'curated': 'true',
        'curatedid': currateid,
        'gridColumns': 3,
        'facets': '',
        'advfilter': 'true',
        'platform': 'Desktop',
        'showAdsOnNextPage': 'true',
        'is_ads_enable_plp': 'true',
        'displayRatings': 'true'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None


# Example usage:
url = 'https://www.ajio.com/api/category/83'
currateid = 'grooming-4384-57431'
outputFileName = '../outputs/men/Grooming.json'
pages = 40

all_data = []

with open(outputFileName, 'a') as json_file:  # Append mode
    json_file.write('[')
    json_file.write('\n')

def save_to_json(data, filename,page):
    for i in data:
        lis.append(i)
    with open(filename, 'a') as json_file:  # Append mode
        json.dump(data, json_file, indent=4)
        if page!=pages-1:
            json_file.write(',')
        json_file.write('\n')  # Add a new line for each appended data

lis=[]
current_page = 1
for i in range(1, pages):
    print(i)
    api_data = make_api_request(i, url, currateid)
    if api_data:
        save_to_json(api_data['products'], outputFileName,i)
        # print(api_data)
    else:
        print("Failed to fetch data from API.")

# api_data = make_api_request(1, url, currateid)
# if api_data:
#     save_to_json(api_data['products'], outputFileName)

with open(outputFileName, 'a') as json_file:  # Append mode
    json_file.truncate()
    json_file.truncate()
    json_file.write(']')
    # json_file.write('\n')

print(len(lis))
print("Data extraction completed.")
# save_to_json(all_data, f'../outputs/`${outputFileName}`.json')
