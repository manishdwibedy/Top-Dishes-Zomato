from util import constant
from Load_Zomato_Solr import loadReviews, translateReviews, loadRestaurant
from Zomato import getRestaurant

isLoadingReview = False
isLoadingRestaurant = True

def loadReview():
    New_Delhi = constant.city_id
    restrauntReviews = loadReviews.getReviews(New_Delhi, 0, 2)

    reviewList = []
    for restrauntreview in restrauntReviews:
        for review in restrauntreview:
            reviewList.append(review)

    loadReviews.addToSolr(reviewList)


    token = translateReviews.translate.getToken()
    translateReviews.translateReviews(token)

def loadRestraunt():
    resSet = loadRestaurant.getAllRestaurantID()

    restaurant_list = []
    for resID in resSet:
        restaurant_list.append(getRestaurant.getRestaurants(resID))
    loadRestaurant.addToSolr(restaurant_list)

if __name__ == '__main__':
    if isLoadingReview and not isLoadingRestaurant:
        loadReview()
    elif isLoadingRestaurant and not isLoadingReview:
        loadRestraunt()
    else:
        loadReview()
        loadRestraunt()
