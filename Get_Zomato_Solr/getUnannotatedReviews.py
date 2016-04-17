from solr import connection, query
from util import constant
import re

def seperatePunctuations():
    pass
def getUntaggedReviews():
    conn = connection.get_connection()
    data = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:false', 1)

    reviewsList = data.result.response.docs

    if len(reviewsList) == 1:
        hindi = reviewsList[0]['hindi'][0]
        words = hindi.split(' ')
        reviewText = []
        for word in words:
            chars = set('-!$%^&*()_+|~=`{}\[\]:;<>?,.\/')
            if any((c in chars) for c in word):
                insertedSpace = re.sub(r'(.*)([-!$%^&*()_+|~=`{}\[\]:";<>?,.\/])(.*)', r"\1 \2 \3",  word).strip()
                spaces = insertedSpace.split(' ')
                for spaceText in spaces:
                    reviewText.append(spaceText)
            else:
                reviewText.append(word)
        return {
            'id': reviewsList[0]['id'],
            'review': reviewText
        }
    else:
        return None


if __name__ == '__main__':
    reviews = getUntaggedReviews()
    pass