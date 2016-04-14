import getRestaurant
import getReviews
from util import constant

def getAllReviews(city_id, start_city_index, count_city):
    """
    Getting the reviews for 'count_city' number of restaurants in the city referred by city_id.
    The first restaurant's index would be start_city_index

    :param city_id: the city's ID
    :param start_city_index: the restaurant index
    :param count_city: number of restaurant
    :return:
    """
    restaurantList = getRestaurant.get_restaurant_id_city(city_id, start_city_index, count_city)

    reviewList = []
    for restaurant_id in restaurantList:
        reviews = getReviews.get_reviews(restaurant_id)
        reviewList.append(reviews)
    return reviewList


if __name__ == '__main__':
    New_Delhi = constant.city_id

    reviewList = getAllReviews(New_Delhi, 0, 10)

    print reviewList