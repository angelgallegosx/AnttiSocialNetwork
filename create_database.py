import sqlite3

# It creates the database if it doesn't exist
with sqlite3.connect("database.db") as connection:
	# Allow to work with the database
	c = connection.cursor()
	
	c.execute(
