from Zomato import getRestaurant
from util import constant

def getRestaurants(city_id, city_index, city_count):
    """
    Getting the reviews for 'city_count' number of restaurants in the city referred by city_id.
    The first restaurant's index would be city_index

    :param city_id: the city's ID
    :param start_city_index: the restaurant index
    :param count_city: number of restaurant
    :return:
    """
    restaurants = getRestaurant.get_restaurant_info_city(city_id, city_index, city_count)

    return restaurants

if __name__ == '__main__':
    New_Delhi = constant.city_id
    restaurants = getRestaurants(New_Delhi, 0, 2)
    pass
