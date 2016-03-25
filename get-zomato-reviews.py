import requests
import json
from util import constant

def get_reviews(restaurant_id):
    '''
    Getting the reviews of a restaurant
    :param restaurant_id: restaurant id
    :return: Nothing
    '''
    URL = constant.zomato_base_url + 'reviews'
    print constant.zomato_api_key

    headers = {
        'Accept': 'application/json',
        'user-key': constant.zomato_api_key,
        "User-agent": "curl/7.43.0"
    }

    payload = {'res_id': restaurant_id}

    print 'Starting'
    response = requests.get(URL, headers=headers, params=payload)

    reviewsObject = json.loads(response.text)

    reviewList = reviewsObject['user_reviews']

    for review in reviewList:
        print review['review']['rating']
        print review['review']['review_text']

    # print response.text

if __name__ == "__main__":
    restaurant_id = constant.restaurant_id
    get_reviews(restaurant_id)