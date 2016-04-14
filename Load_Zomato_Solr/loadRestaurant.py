from Zomato import getRestaurant
from util import constant
from solr import connection, index

def getRestaurants(city_id, city_index, city_count):
    """
    Getting the restaurant info for 'city_count' number of restaurants in the city referred by city_id.
    The first restaurant's index would be city_index

    :param city_id: the city's ID
    :param start_city_index: the restaurant index
    :param count_city: number of restaurant
    :return:
    """
    restaurants = getRestaurant.get_restaurant_info_city(city_id, city_index, city_count)

    return restaurants

def addToSolr(restaurants):
    """
    Add the restaurants to the solr index
    :param restaurants: the restaurants to be index
    :return: Nothing
    """
    conn = connection.get_connection()
    index.index(conn, constant.RESTAURANTS_COLLECTION, restaurants)
    pass


if __name__ == '__main__':
    New_Delhi = constant.city_id
    restaurants = getRestaurants(New_Delhi, 0, 2)

    addToSolr(restaurants)
    pass
