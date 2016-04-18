from solr import connection, query, index
import translate
from util import constant

def translateReview(token, original):
    """
    Translating the review into hindi.
    :param token: the token to be used for translation
    :param original: the original review text in English
    :return: the review in Hindi
    """
    language = constant.lang
    try:
        hindiReview = translate.translate(token, original, language)
        return hindiReview
    except:
        print 'Error!'
        return 'Error in translation. Please edit manually, if needed'


def translateReviews(token):
    """
    Translating all the reviews in the solr instance
    :param token: the token to be used for translation
    :return: Nothing
    """
    conn = connection.get_connection()
    data = query.get(conn, constant.REVIEWS_COLLECTION, 'annotated:false', 60)

    reviewsList = data.result.response.docs

    translatedReviewList = []
    for review in reviewsList:
        review_original = review['review_text'][0]
        hindiReview = translateReview(token, review_original)

        # Removed the quotes
        hindiReview = hindiReview[2:-1]

        # If the review has ... at the n
        if hindiReview.endswith('...'):
            hindiReview = hindiReview[:-3]

        review['hindi'] = hindiReview
        translatedReviewList.append(review)
    index.index(conn, constant.REVIEWS_COLLECTION, translatedReviewList)


if __name__ == '__main__':
    token = translate.getToken()
    translateReviews(token)
    pass