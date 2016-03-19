from app import app
import os
import psycopg2
import urlparse

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

@app.route('/db_test')
def test():

	# Connect to the database. The enviroment variable is on the Heroku servers 
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)

	cur = conn.cursor()

	cur.execute("SELECT data.\"fromDate\",data.\"toDate\",data.domain FROM public.data WHERE user_id = 'test'")

	rows = cur.fetchall()

	for row in rows:
		print row

	return rows[0]

# Run method start the flask server
if __name__ == '__main__':
    app.run(debug=True)
