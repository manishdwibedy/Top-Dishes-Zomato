from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/annotate')
def annotator():
    return render_template('annotations.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')