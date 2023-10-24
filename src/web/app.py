from flask import Flask, render_template, request
import requests  # You may need to install this library using pip
from db import get_db, close_db
import sqlalchemy
from logger import log

app = Flask(__name__)
app.teardown_appcontext(close_db)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bounce")
def bounce():
    url = request.args.get('url')  # Get the URL from the query parameters
    if url:
        try:
            response = requests.get(url)  # Make the GET request
            response.raise_for_status()  # Check if the request was successful
            return response.text  # Return the body of the response
        except requests.RequestException as e:
            return f"An error occurred: {e}", 400  # Return an error message if the request fails
    else:
        return "No URL provided", 400  # Return an error message if no URL is provided
