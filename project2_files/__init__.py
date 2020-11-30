'''
why is this called __init__.py?
becauase run.py, when executed, will always look for an file that contains __init__.py
automatically looks for this file to find any attributes, objects, methods
therefore this is where we must INSTANTIATE the object of the Flask class
'''
from flask import Flask
print("in __init__.py before app = Flask(...)")

# now we will create an object from our flask
# will hold the information of the object in memory
# creating an instance of Flask
app = Flask(__name__)
print("in __init__.py just after app = Flask(...)")

#setting some cookies and security measures
app.config["SECRET_KEY"] = "cop4813"
print("in __init__.py just after app.config")
# import routes
# a .py script that contains the functions that will eventually call the
# pages from the web app
from project2_files import routes