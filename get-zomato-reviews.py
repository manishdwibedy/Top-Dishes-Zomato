import requests
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
    print response.text

if __name__ == "__main__":
    restaurant_id = constant.restaurant_id
    get_reviews(restaurant_id)