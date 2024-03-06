import requests
import json

def make_api_request(current_page):
    url = 'https://www.ajio.com/api/category/83'
    params = {
        'currentPage': current_page,
        'pageSize': 45,
        'format': 'json',
        'query': '%3Arelevance',
        'sortBy': 'relevance',
        'curated': 'true',
        'curatedid': 'footwear-4792-56591',
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
all_data = []
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
# current_page = 1
for i in range(1,1135):
    print(i)
    api_data = make_api_request(i)
    if api_data:
        all_data.extend(api_data['products'])
        # print(api_data)
    else:
        print("Failed to fetch data from API.")

save_to_json(all_data, '../outputs/men/footwear.json')