import os
import requests
from flask import Flask, render_template, render_template, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
# @app.route('/get_users')
# def get_users():
    
#     return render_template("users.html", users=mongo.db.users.find())

@app.route('/coin_list')
def coin_list():
  r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=10&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
  results = r.json()
  data = results['data']
  return render_template("coin_list.html", data=data)
  


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)