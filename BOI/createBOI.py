from solr import connection, query
from util import constant


def getReviews():
    """
    Getting the annotated reviews
    :return: the list of reviews
    """

    conn = connection.get_connection()

    response = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:true')

    reviews = response.result.dict['response']['docs']
    return reviews

if __name__ == '__main__':
    getReviews()