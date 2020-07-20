import bcrypt
import os
import requests
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=50&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
results = r.json()
data = results['data']

r = requests.get('https://pro-api.coinmarketcap.com//v1/global-metrics/quotes/latest?&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
results = r.json()
global_data = results['data']


@app.route('/')
@app.route('/login')
def login():
  if 'username' in session:
    return 'You are logged in as '+ session['username']
  return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "POST":
    user = mongo.db.user
    exsisting_user = user.find_one({'name': request.form['username']})
    # if no matching username found
    if exsisting_user is None:
      hashpassword = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
      user.insert({'name': request.form['username'], 'password': hashpassword})
      session['username'] = request.form['username']
      return redirect(url_for('login'))
    return 'SORRY! That username is taken'
  return render_template("register.html")

@app.route('/coin_list')
def coin_list():
   return render_template("coin_list.html", data=data, global_data=global_data)


@app.route('/create_a_bag')
def create_a_bag():
  return render_template("create_a_bag.html", data=data)


@app.route('/add_to_bagz', methods=["POST"])
def add_to_bagz():
  users=mongo.db.users
  users.insert_one(request.form.to_dict())
  return redirect(url_for('get_my_bagz'))


@app.route('/get_my_bagz')
def get_my_bagz():
    
  return render_template("my_bagz.html", users=mongo.db.users.find(), data=data)


@app.route('/edit_bag/<bag_id>' )
def edit_bag(bag_id):
  the_bag = mongo.db.users.find_one({"_id": ObjectId(bag_id)})
    
  return render_template("edit_bag.html", bag=the_bag, data=data)


@app.route('/update_bag/<bag_id>', methods=["POST"])
def update_bag(bag_id):
  bag = mongo.db.users
  bag.update({'_id': ObjectId(bag_id)},
  {
    'assets': request.form.get('assets'),
    'amount': request.form.get('amount'),
    'price_paid': request.form.get('price_paid'),
    'date_of_purchase': request.form.get('date_of_purchase')
  })
  return redirect(url_for('get_my_bagz'))


@app.route('/delete_bag/<bag_id>')
def delete_bag(bag_id):
  mongo.db.users.delete_one({'_id': ObjectId(bag_id)})
  return redirect(url_for('get_my_bagz')) 

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)