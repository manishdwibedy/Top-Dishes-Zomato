from util import constant
from solr import connection, index,query

def annotateReview(reviewID, annotations):
    conn = connection.get_connection()
    data = query.get(conn, constant.REVIEWS_COLLECTION, 'id:'+reviewID, 1)

    review = data.result.response.docs[0]

    review['food_item'] = annotations['food_list']
    review['menu_item'] = annotations['menu_list']
    review['sentiment'] = annotations['sentiment']
    review['annotated'] = True

    index.index(conn, constant.REVIEWS_COLLECTION, [review])


if __name__ == '__main__':
    annotateReview()