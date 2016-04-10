from flask import Flask, render_template, jsonify, request
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
    review = 'The concept is totally unscripted as the name suggests. The live kitchen is really awesome here. Pick up your own veggies with your favourite toppings and sause and your food is ready. You can see the live kitchen. The ambience is really offbeat and you cannot compare it to any restaurant in Gurgaon. Especially on evening it is very romantic place for couples.'
    words = re.sub("[^\w]", " ",  review).split()

    return jsonify(results=words)

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