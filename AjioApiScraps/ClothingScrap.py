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
currateid = 'accessories-4792-56592'
outputFileName = '../outputs/women/accessories.json'
pages = 3471

all_data = []


def save_to_json(data, filename):
    with open(filename, 'a') as json_file:  # Append mode
        json.dump(data, json_file, indent=4)
        json_file.write('\n')  # Add a new line for each appended data


# current_page = 1
for i in range(1, pages):
    print(i)
    api_data = make_api_request(i, url, currateid)
    if api_data:
        save_to_json(api_data['products'], outputFileName)
        # print(api_data)
    else:
        print("Failed to fetch data from API.")

print("Data extraction completed.")
# save_to_json(all_data, f'../outputs/`${outputFileName}`.json')
