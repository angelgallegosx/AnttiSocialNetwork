from app import app
from flask import Flask, render_template, request, jsonify

@app.route('/')
def index():
    user = {'nickname': 'stranger'}
    return render_template('index.html', title='Antti-Social Network', user=user)

@app.route('/Statistics')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=["GET", "POST"])
def login():

	error=None

	if request.method == "POST":
		return "Hello"

	return "None"

@app.route('/update_data', methods=["POST"])
def update_data():

	print request.values

	return jsonify({"message:" : "OK"})

# Run method start the flask server
if __name__ == '__main__':
    app.run(debug=True)
