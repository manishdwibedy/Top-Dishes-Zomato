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

    user_reviews = []
    for review in reviewList:
        user_review = {
            'rating' : review['review']['rating'],
            'review_text' : review['review']['review_text']
        }
        user_reviews.append(user_review)

    return user_reviews

if __name__ == "__main__":
    restaurant_id = constant.restaurant_id
    print get_reviews(restaurant_id)