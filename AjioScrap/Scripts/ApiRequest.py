import requests
def make_api_request(current_page, url, currateid,timeout=10):
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

    response = requests.get(url, params=params,timeout=timeout)
    return response
