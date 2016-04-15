from flask import Flask, render_template, jsonify, request
from Get_Zomato_Solr import getUnannotatedReviews
from Load_Zomato_Solr import annotateReview

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

    return jsonify(results=reviews, id=id)

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
                food += fooditem + ' '

            # Save the annotations
            food_list.append(food)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')