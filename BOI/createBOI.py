from solr import connection, query
from util import constant
from Get_Zomato_Solr import getUnannotatedReviews

def getReviews():
    """
    Getting the annotated reviews
    :return: the list of reviews
    """

    conn = connection.get_connection()

    response = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:true')

    reviews = response.result.dict['response']['docs']
    return reviews

def createBOI():
    """
    Creating the BOI annotations
    :return: Nothing
    """
    reviews = getReviews()

    for review in reviews:
        food_item_list = review['food_item']
        hindi_review = review['hindi'][0]


        food_items = dict((food_item,1) for food_item in food_item_list)
        review_words = hindi_review.split(' ')

        BOI_list = []
        for review_word in hindi_review.split(' '):
            seperated_word_list = getUnannotatedReviews.seperatePunctuations(review_word)

            for word in seperated_word_list:
                if word == '':
                    continue
                if word in food_items:
                    BOI_list.append(word+'/B')
                else:
                    BOI_list.append(word+'/O')

if __name__ == '__main__':
    createBOI()