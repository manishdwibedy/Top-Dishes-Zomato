from util import constant
from Load_Zomato_Solr import loadReviews, translateReviews

New_Delhi = constant.city_id
restrauntReviews = loadReviews.getReviews(New_Delhi, 0, 2)

reviewList = []
for restrauntreview in restrauntReviews:
    for review in restrauntreview:
        reviewList.append(review)

loadReviews.addToSolr(reviewList)


token = translateReviews.translate.getToken()
translateReviews.translateReviews(token)