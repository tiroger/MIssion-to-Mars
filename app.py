# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection locally
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_info = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    return render_template('scrape.html')


if __name__ == "__main__":
    app.run(debug=True)
