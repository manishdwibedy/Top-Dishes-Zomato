from flask import Flask, render_template, jsonify, request
from Get_Zomato_Solr import getUnannotatedReviews
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/annotate')
def annotator():
    return render_template('annotations.html')

@app.route('/getReview')
def getReviews():
    reviewWord = getUnannotatedReviews.getUntaggedReviews()

    if reviewWord is None:
        reviewWord = []

    return jsonify(results=reviewWord)

@app.route('/saveAnnotation', methods=['PUT'])
def saveAnnotation():
    annotations = request.get_json()

    if len(annotations['annotations']) > 0:
        annotationList = annotations['annotations']

        for annotation in annotationList:
            print 'Food Item - ' + str(annotation['foodItem'])
            print 'Menu Item - ' + annotation['menuItem']
            print 'Sentiment - ' + annotation['sentiment']
        result = {'status': 'Done'}
    else:
        result = {'status': 'Missing Data'}
    return jsonify(results=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')