from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    user = {'nickname': 'stranger'}
    return render_template('index.html', title='Antti-Social Network', user=user)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=["GET", "POST"])
def login(user):

	return None

@app.route('/update_Data', methods=["POST"])
def store_data(data):

	return None

# Run method start the flask server
if __name__ == '__main__':
    app.run(debug=True)
