from flask import Flask

# create the application object
app = Flask(__name__)

# Import the Driver
from app import routes
