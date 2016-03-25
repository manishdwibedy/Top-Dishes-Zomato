from util import constant

def get_reviews(restraunt_id):
    print constant.zomato_base_url
    print constant.zomato_api_key

if __name__ == "__main__":
    restaurant_id = constant.restaurant_id
    get_reviews(restaurant_id)