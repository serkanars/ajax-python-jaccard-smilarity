from flask import Flask, request, jsonify
from jaccard import *

app = Flask(__name__)

@app.route('/api/', methods = ['POST'])
def index():
	response = request.get_json()
	text1 = response['message']
	text2 = response['message2']

	print(text1, text2)

	score = jaccard(text1 , text2)

	return jsonify({'output' : score})


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(debug=True)