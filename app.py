import os
import requests
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=40&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
results = r.json()
data = results['data']


@app.route('/')
@app.route('/create_a_bag')
def create_a_bag():
  return render_template("create_a_bag.html", data=data)


@app.route('/get_my_bagz')
def get_my_bagz():
    
  return render_template("users.html", users=mongo.db.users.find())

@app.route('/add_to_bagz', methods=["POST"])
def add_to_bagz():
  users=mongo.db.users
  users.insert_one(request.form.to_dict())
  return redirect(url_for('get_my_bagz'))


@app.route('/coin_list')
def coin_list(): 
  
  return render_template("coin_list.html", data=data)
  


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)