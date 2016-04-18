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

def createFoodDict(food_item_list):
    """
    Create a dictionary where the first word is key and the complete word is the value
    :param food_item_list: the list of food items
    :return: the dictionary of food items
    """
    food_dict = {}
    for food_item in food_item_list:
        words = food_item.split(' ')
        first_word = words[0]
        food_dict[first_word] = food_item
    return food_dict


def createBOI():
    """
    Creating the BOI annotations
    :return: list of reviews with the BOI tags
    """
    reviews = getReviews()

    BOI_reviews = []

    for review in reviews:
        food_item_list = review['food_item']
        hindi_review = review['hindi'][0]


        # food_items = dict((food_item,1) for food_item in food_item_list)
        food_items = createFoodDict(food_item_list)
        review_words = hindi_review.split(' ')

        BOI_list = []

        review_words_enumerator = enumerate(review_words)
        for index, review_word in review_words_enumerator:
            seperated_word_list = getUnannotatedReviews.seperatePunctuations(review_word)

            for word in seperated_word_list:
                if word == '':
                    continue
                if word in food_items:
                    menu_length = len(food_items[word].split(' '))
                    if menu_length > 1:
                        BOI_list.append(word + '/B')
                        for counter in range(index+1, index+menu_length):
                            next_word = review_words_enumerator.next()
                            BOI_list.append(next_word[1] + '/I')
                            index +=1
                    else:
                        BOI_list.append(word+'/B')
                else:
                    BOI_list.append(word+'/O')
        BOI_reviews.append(' '.join(BOI_list))

    return BOI_reviews

if __name__ == '__main__':
    BOI_list = createBOI()

    print BOI_list