from flask import Flask, render_template, jsonify
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
    review = 'Coffee was decent, but not memorable enough to become a regular.'
    words = re.sub("[^\w]", " ",  review).split()

    return jsonify(results=words)

if __name__ == '__main__':
    app.run(host='0.0.0.0')