import getRestaurant
import getReviews
from util import constant

def getAllReviews(city_id):
    restaurantList = getRestaurant.get_restaurants_city(city_id, 0, 10)

    reviewList = []
    for restaurant_id in restaurantList:
        reviews = getReviews.get_reviews(restaurant_id)
        reviewList.append(reviews)
    return reviewList


if __name__ == '__main__':
    New_Delhi = constant.city_id

    reviewList = getAllReviews(New_Delhi)

    print reviewList