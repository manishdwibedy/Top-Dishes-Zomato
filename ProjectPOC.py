from util import constant
from getZomatoReviews import get_reviews
from translateReviews import translate, getToken
from spellingCorrection import correctSpelling

restaurant_id = constant.restaurant_id

# Get 5 reviews for Impromptu
user_reviews = get_reviews(restaurant_id)

token = getToken()

for review in user_reviews:
    print 'English version -'
    print review

    print 'Corrected spelling - '
    correctedSpelling = correctSpelling(review['review_text'])
    print correctSpelling

    print 'Hindi version -'
    print translate(token=token, text=correctedSpelling,destinationLanguage='hi')

