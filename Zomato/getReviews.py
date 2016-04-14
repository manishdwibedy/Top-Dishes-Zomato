import requests
import json
from util import constant

def get_reviews(restaurant_id, start = 0, count = 5):
    '''
    Getting the reviews of a restaurant
    :param restaurant_id: restaurant id
    :return: a list of review ratings and review text
    '''

    # URL to hit for getting reviews
    URL = constant.zomato_base_url + 'reviews'

    # headers needed by the API to get reviews
    headers = {
        'Accept': 'application/json',
        'user-key': constant.zomato_api_key,
        "User-agent": "curl/7.43.0"
    }

    # parameters needed by the API to get reviews
    payload = {
        'res_id': restaurant_id,
        'start': start,
        'count': count
        }

    # Hitting the API with needed headers and parameters
    response = requests.get(URL, headers=headers, params=payload)

    # Converting the response to an object
    reviewsObject = json.loads(response.text)

    # Getting all the user reviews
    reviewList = reviewsObject['user_reviews']

    # The final user reviews list
    user_reviews = []

    # Iterating over the user reviews
    for review in reviewList:
        # Convert the unicode text version of the review to ASCII
        ascii_review = review['review']['review_text'].encode('ascii','ignore')

        # An individual user review
        user_review = {
            'id': review['review']['id'],
            'res_id': restaurant_id,
            'likes': review['review']['likes'],
            'rating' : review['review']['rating'],
            'rating_text' : review['review']['rating_text'],
            'review_text': ascii_review,
            'timestamp': review['review']['timestamp'],
            'user_name': review['review']['user']['name'],
            'user_foodie_level': review['review']['user']['foodie_level'],
            'user_foodie_level_num': review['review']['user']['foodie_level_num']
        }

        # Adding to the final list of user reviews
        user_reviews.append(user_review)

    # Returning the final list of user reviews
    return user_reviews

if __name__ == "__main__":
    # The restaurant id for Impromptu
    restaurant_id = constant.restaurant_id

    # Get 5 reviews for Impromptu
    # user_reviews = get_reviews(restaurant_id)

    num_of_reviews = 10

    # Get 'num_of_reviews' reviews for Impromptu
    user_reviews = get_reviews(restaurant_id, count=num_of_reviews)
    print user_reviews

    start = 5
    user_reviews = get_reviews(restaurant_id, start, num_of_reviews)
    print user_reviews

