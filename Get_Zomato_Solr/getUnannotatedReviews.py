from solr import connection, query
from util import constant
import re

# The characters that would be seperated
chars = set('-!$%^&*()_+|~=`{}\[\]:;<>?,.\/')

def seperatePunctuations(word):
    """
    Seperating the punctuations
    :param word: the word, where we would search for any punctuations
    :return: a list of seperated words, if any. Otherwise single element list is returned
    """
    seperatedWords = []
    if any((c in chars) for c in word):
        insertedSpace = re.sub(r'(.*)([-!$%^&*()_+|~=`{}\[\]:";<>?,.\/])(.*)', r"\1 \2 \3",  word).strip()
        spaces = insertedSpace.split(' ')
        for spaceText in spaces:
            seperatedWords.append(spaceText)
    elif word.endswith(u'\u0964'):
        seperatedWords.append(word[:-1])
        seperatedWords.append(u'\u0964')
    else:
        seperatedWords.append(word)
    return seperatedWords

def getUntaggedReviews():
    conn = connection.get_connection()
    data = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:false', 1)

    reviewsList = data.result.response.docs

    if len(reviewsList) == 1:
        hindi = reviewsList[0]['hindi'][0]
        words = hindi[2:-1].split(' ')
        reviewText = []
        for word in words:
            without_seperatePunctuations = seperatePunctuations(word)
            for word_w in without_seperatePunctuations:
                reviewText.append(word_w)
        return {
            'id': reviewsList[0]['id'],
            'res_id': reviewsList[0]['res_id'],
            'review': reviewText
        }
    else:
        return None


if __name__ == '__main__':
    reviews = getUntaggedReviews()
    pass