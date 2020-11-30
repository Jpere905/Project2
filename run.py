'''
run script file will access the app we create in that folder
If running on heroku you need to indicate where run.py is located
this is how the server knows where to initialize our app. This
creates the instance of the flask webapp

we also need a python script to create the instance of the flask app
what is a web app?
its an instance of the object class flask
from module flask, we import the class flask
we instantiate an object from this class
this object is the location  in memory where the app is.
from that object we call any HTML, we to render in any HTML page from this app
to display or request info from the user thru either GET or POST methods
'''

print("in run.py before if __name__")
from project2_files import app # as soon as it touches this, it jumps to __init__.py
print("in run.py just after import app")

if __name__ == '__main__':
    print("in run.py just inside if __name__")
    app.run(debug=True, port=8080)
