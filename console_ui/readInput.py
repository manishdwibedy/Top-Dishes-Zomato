import sys, locale
from solr import connection, query
from util import constant

def readInput():
    text = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
    return text.split(' ')

def getMatchingText(input):
    conn = connection.get_connection()
    inputQuery = ' '.join(input)
    searchQuerty = 'menu_item:' + inputQuery + '~2'

    num_of_results_response = query.get(conn, constant.REVIEWS_COLLECTION, searchQuerty, 0)

    num_of_results = num_of_results_response.result.dict['response']['numFound']

    response = query.get(conn, constant.REVIEWS_COLLECTION, searchQuerty, num_of_results)
    reviews = response.result.dict['response']['docs']

    menu_item_rating = {}
    for review in reviews:
        food_mentions = []
        for index, menu in enumerate(review['menu_item']):
            food_mention = {
                'menu_item': menu,
                'sentiment': review['sentiment'][index]
            }
            food_mentions.append(food_mention)
            pass

if __name__ == '__main__':
    words = readInput()
    # print words

    getMatchingText(words)