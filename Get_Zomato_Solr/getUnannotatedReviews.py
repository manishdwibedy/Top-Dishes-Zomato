from solr import connection, query
from util import constant

def getUntaggedReviews():
    conn = connection.get_connection()
    data = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:false', 1)

    reviewsList = data.result.response.docs

    if len(reviewsList) == 1:
        return reviewsList[0]['hindi'][0]
    else:
        return None


if __name__ == '__main__':
    reviews = getUntaggedReviews()
    pass