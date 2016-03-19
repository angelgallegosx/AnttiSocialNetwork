from app import app
import database_utils

# Meanwhile
import os
import psycopg2
import urlparse
#--

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

	#print request.values
	try:
		userID = request.form.get("user_id")
		domain = request.form.get("domain")
		start = request.form.get("start")
		end = request.form.get("end")	
	except Exception, e:
		raise e
	
	#db = database()
	#cur = db.get_cursor()
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	conn = psycopg2.connect(
			database = url.path[1:],
			user = url.username,
			password = url.password,
			host = url.hostname,
			port = url.port
	)
	cur = conn.cursor()

	cur.execute(" INSERT INTO public.data(\"user_id\", \"domain\", \"toDate\", \"fromDate\") VALUES (%s, %s, %s, %s)", (userID, domain, start, end) )
	conn.commit()

	string = userID + " " + domain + " " + start + " " + end 

	return jsonify({"message:" : "OK", "I received":string})

@app.route('/db_test')
def test():

	rows = cur.fetchall()

	for row in rows:
		print row

	conn.close()

	return str(rows[0])

# Run method start the flask server
if __name__ == '__main__':
    app.run(debug=True)
