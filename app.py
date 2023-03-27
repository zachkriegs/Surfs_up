# 1. import Flask
from flask import Flask 


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
@app.route('/')
def hello_world():
    return 'Hello world'
export FLASK_APP=app.py
app.run(debug=True)