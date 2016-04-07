import requests
import json
from util import constant

def get_restaurants_city(city_id, start = 0, count = 5):
    '''
    Getting the list of restaurant in a city
    :param city_id: city ID
    :param start: starting index of restaurant
    :param count: count of restaurant returned
    :return: a list of restaurants
    '''

    # URL to hit for getting restaurants
    URL = constant.zomato_base_url + 'search'

    # headers needed by the API to get restaurants
    headers = {
        'Accept': 'application/json',
        'user-key': constant.zomato_api_key,
        "User-agent": "curl/7.43.0"
    }

    # parameters needed by the API to get restaurants
    payload = {
        'entity_id': city_id,
        'entity_type': 'city',
        'start': start,
        'count': count
        }

    # Hitting the API with needed headers and parameters
    response = requests.get(URL, headers=headers, params=payload)

    # Converting the response to an object
    restaurantsObject = json.loads(response.text)

    # Getting all the user reviews
    restaurantsList = restaurantsObject['restaurants']

    # The final restaurant ID list
    restaurants_id_list = []

    # Iterating over the user reviews
    for restaurant in restaurantsList:
        # Get the restaurant ID
        res_id = restaurant['restaurant']['R']['res_id']

        # Adding to the final list of restaurant IDs
        restaurants_id_list.append(res_id)

    # Returning the final list of restaurants ID
    return restaurants_id_list

if __name__ == "__main__":
    # The city id for New Delhi
    restaurant_id = constant.city_id

    num_of_restaurants = 10

    # Get 'num_of_restaurants' restaurants in New Delhi
    restaurants_id_list = get_restaurants_city(restaurant_id, count=num_of_restaurants)
    print restaurants_id_list

