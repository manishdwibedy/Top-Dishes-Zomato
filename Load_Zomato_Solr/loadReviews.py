from util import constant
from Zomato import getBulkReviews
from solr import connection, index
import json

def getReviews(city_id, city_index, city_count):
    """
    Getting the reviews for 'city_count' number of restaurants in the city referred by city_id.
    The first restaurant's index would be city_index

    :param city_id: the city's ID
    :param start_city_index: the restaurant index
    :param count_city: number of restaurant
    :return:
    """
    reviewList = getBulkReviews.getAllReviews(city_id, city_index, city_count)

    return reviewList

def getRestrauntReviews(res_id):
    return getBulkReviews.getReviewByRestaurant(res_id)

def addToSolr(reviews):
    """
    Add the reviews to the solr index
    :param reviews: the reviews to be index
    :return: Nothing
    """
    conn = connection.get_connection()
    index.index(conn, constant.REVIEWS_COLLECTION, reviews)

def loadFromFile():
    with open('reviewData/reviews_799.txt') as data_file:
        data = json.load(data_file)

        addToSolr(data)

if __name__ == '__main__':
    # New_Delhi = constant.city_id
    # restrauntReviews = getReviews(New_Delhi, 0, 2)
    #
    # reviewList = []
    # for restrauntreview in restrauntReviews:
    #     for review in restrauntreview:
    #         reviewList.append(review)
    #
    # addToSolr(reviewList)
    loadFromFile()