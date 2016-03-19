class database():

	def __init__(self):

		# Connect to the database. The enviroment variable is on the Heroku servers 
		urlparse.uses_netloc.append("postgres")
		self.url = urlparse.urlparse(os.environ["DATABASE_URL"])
		self.conn = None

	def connect(self):
		
		self.conn = psycopg2.connect(
			database = self.url.path[1:],
			user = self.url.username,
			password = self.url.password,
			host = self.url.hostname,
			port = self.url.port
		)

	def disconnect(self):
		self.conn = None

	def get_cursor(self):
		if conn == None:
			self.connect()
		
		cur = conn.cursor()		

		return cur
	
