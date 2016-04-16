from Zomato import getRestaurant
from util import constant
from solr import connection, index, query

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

def getAllRestaurantID():
    """
    Returning the restaurant IDs if a review is present
    :return:
    """
    conn = connection.get_connection()
    docs = query.get(conn, constant.REVIEWS_COLLECTION, 'id:*')

    res_ids = set()
    reviews = docs.result.dict['response']['docs']

    for review in reviews:
        res_id = review['res_id']
        res_ids.add(res_id[0])
    return res_ids

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
    # restaurants = getRestaurants(New_Delhi, 0, 2)
    restaurants = getAllRestaurantID()

    addToSolr(restaurants)
    pass
