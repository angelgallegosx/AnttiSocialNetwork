class database():

	def __init__(self):

		# Connect to the database. The enviroment variable is on the Heroku servers 
		self.urlparse.uses_netloc.append("postgres")
		self.url = urlparse.urlparse(os.environ["DATABASE_URL"])
		self.conn = None

	def connect(self):
		
		self.conn = psycopg2.connect(
			database=url.path[1:],
			user=url.username,
			password=url.password,
			host=url.hostname,
			port=url.port
		)

	def disconnect(self):
		self.conn = None

	def get_cursor(self):
		if conn == None:
			connect()
		
		cur = conn.cursor()		

		return cur
	
