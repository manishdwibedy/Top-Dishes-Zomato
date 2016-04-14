import requests
import json
from util import constant

def get_restaurant_id_city(city_id, start = 0, count = 5):
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

def get_restaurant_info_city(city_id, start = 0, count = 5):
    '''
    Getting the list of restaurants in a city
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
    restaurants_list = []

    # Iterating over the user reviews
    for restaurant in restaurantsList:
        # Get the restaurant ID
        res_data = restaurant['restaurant']
        restaurant_info = {
            'res_id': res_data['id'],
            'name': res_data['name'],
            'cuisines': res_data['cuisines'],
            'menu_url': res_data['menu_url'],
            'price_range': res_data['price_range'],
            'rating': res_data['user_rating']['aggregate_rating'],
            'rating_text': res_data['user_rating']['rating_text'],
            'votes': res_data['user_rating']['votes'],
            'delivers': res_data['is_delivering_now'],
            'online_delivery': res_data['has_online_delivery'],
            'cost_for_two': res_data['average_cost_for_two']
        }
        # Adding to the final list of restaurant IDs
        restaurants_list.append(restaurant_info)

    # Returning the final list of restaurants ID
    return restaurants_list

if __name__ == "__main__":
    # The city id for New Delhi
    restaurant_id = constant.city_id

    num_of_restaurants = 2

    get_restaurant_info_city(restaurant_id, count=num_of_restaurants)

    # Get 'num_of_restaurants' restaurants in New Delhi
    restaurants_id_list = get_restaurant_id_city(restaurant_id, count=num_of_restaurants)
    print restaurants_id_list

