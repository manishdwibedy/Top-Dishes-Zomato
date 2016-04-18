from flask import Flask, render_template, jsonify, request
from Get_Zomato_Solr import getUnannotatedReviews
from Load_Zomato_Solr import annotateReview
from Get_Zomato_Solr.getMenu import getMenuItems
from Matching.match import partialMatch, fuzzyMatch, substringMatch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/annotate')
def annotator():
    return render_template('annotations.html')

@app.route('/getReview')
def getReviews():
    data = getUnannotatedReviews.getUntaggedReviews()

    reviews = data['review']
    id = data['id']
    if reviews is None:
        reviews = []

    return jsonify(results=reviews, id=id, res_id=data['res_id'][0])

@app.route('/saveAnnotation', methods=['PUT'])
def saveAnnotation():
    data = request.get_json()
    reviewID = data['reviewID']
    if len(data['annotations']) > 0:
        annotationList = data['annotations']

        food_list = []
        menu_list = []
        sentiment_list = []

        for annotation in annotationList:

            # Computing the food item
            food = ''
            for fooditem in annotation['foodItem']:
                food += fooditem.strip() + ' '

            # Save the annotations
            food_list.append(food.strip())
            menu_list.append(annotation['menuItem'])
            sentiment_list.append(annotation['sentiment'])

            print 'Food Item - ' + str(annotation['foodItem'])
            print 'Menu Item - ' + annotation['menuItem']
            print 'Sentiment - ' + annotation['sentiment']

        annotations = {
            'food_list': food_list,
            'menu_list': menu_list,
            'sentiment': sentiment_list
        }
        annotateReview.annotateReview(reviewID, annotations)

        result = {'status': 'Done'}
    else:
        result = {'status': 'Missing Data'}
    return jsonify(results=result)

@app.route('/getMenu', methods=['PUT'])
def getMenu():
    data = request.get_json()

    # Extracting the data from the request
    food_mentions = data['food_item_selected']
    reviewId = data['reviewID']
    restaurantID = data['restaurantID']

    # Getting the menu items for the given restaurant
    menuItems = getMenuItems(str(restaurantID))

    # Join the individual word to make the food item
    food_item = ' '.join(food_mentions)

    # Getting the matches by fuzzy matching and partial matching
    matches_fuzzy = fuzzyMatch(food_item, menuItems)
    matches_partial = partialMatch(food_item, menuItems)
    matches_substring = substringMatch(food_item, menuItems)

    # Creating the matching list
    matches = set()
    for match in matches_fuzzy:
        matches.add(match)

    for match in matches_partial:
        matches.add(match)

    for match in matches_substring:
        matches.add(match)

    return jsonify(results=list(matches))

if __name__ == '__main__':
    app.run(host='0.0.0.0')