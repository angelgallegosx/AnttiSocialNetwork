from app import app
from datetime import date, timedelta
import json

# Meanwhile
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import urlparse
#--

from flask import Flask, render_template, request, jsonify
try:
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	conn = psycopg2.connect(
			database = url.path[1:],
			user = url.username,
			password = url.password,
			host = url.hostname,
			port = url.port
	)
except Exception, e:
	print "Cannot connect to the database"


#conn.close()

@app.route('/')
def index():
    user = {'nickname': 'stranger'}
    return render_template('index.html', title='Antti-Social Network', user=user)

@app.route('/statistics/<int:nDays>')
def statistics(nDays):

	#cur.execute("SELECT * FROM public.data WHERE ")

	fromDate = date.today() - timedelta(days=nDays)
	
	cur = conn.cursor(cursor_factory=RealDictCursor)
	cur.execute("SELECT * FROM public.data WHERE fromDate >= %s", (fromDate) )

	#return json.dumps(cur.fetchall(), indent=2)
	#rows = cur.fetchall()
	return "Hello"
    #return render_template('welcome.html')

@app.route('/login', methods=["GET", "POST"])
def login():

	error=None

	if request.method == "POST":
		return "Hello"

	return "None"

@app.route('/update_data', methods=["POST"])
def update_data():

	#print request.values
	data = request.get_json()
	try:
		"""
		userID = request.form.get("user_id")
		domain = request.form.get("domain")
		start = request.form.get("start")
		end = request.form.get("end")	
		"""
		# res = requests.post("https://antti-socialnetwork.herokuapp.com/update_data", json.dumps(data), headers={'Content-type':'application/json'})
		userID = data.get("user_id")
		domain = data.get("domain")
		start = data.get("start")
		end = data.get("end")	
		
	except Exception, e:
		raise e
	
	#db = database()
	#cur = db.get_cursor()
	cur = conn.cursor()
	cur.execute(" INSERT INTO public.data(\"user_id\", \"domain\", \"toDate\", \"fromDate\") VALUES (%s, %s, %s, %s)", (userID, domain, start, end) )
	conn.commit()

	string = userID + " " + domain + " " + start + " " + end 

	return jsonify({"message:" : "OK", "Received":string})

# Run method start the flask server
if __name__ == '__main__':
    app.run(debug=True)
