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


"""1st Api call to CMC for list of crypto"""
r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=200&CMC_PRO_API_KEY=' + os.environ.get('API_KEY'))
results = r.json()
data = results['data']
"""2nd Api call to CMC for Market Stats of crypto"""
r = requests.get('https://pro-api.coinmarketcap.com//v1/global-metrics/quotes/latest?&CMC_PRO_API_KEY=' + os.environ.get('API_KEY'))
results = r.json()
global_data = results['data']

"""Check if user is logged in already Y - coin list N -signin/up"""
@app.route('/')
def index():
  if 'username' in session:
    return redirect(url_for('coin_list', username = session['username']))
  return render_template("index.html")

"""Check Mongo for usernames & password match"""
@app.route('/login', methods=["POST"])
def login():
  user = mongo.db.user
  login_user = user.find_one({'name': request.form['username']})

  if login_user:
    if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']) == True:
      session['username'] = request.form['username']
      user = mongo.db.user.find_one({'name': session['username']})
      return redirect(url_for('index', user=user))
    
  return render_template('error_page.html')

"""logout route"""
@app.route('/logout')
def logout():
  if 'username' in session:
    user = mongo.db.user
    login_user = user.find_one({'name': session['username']})
    
    if login_user:
      session.clear()
      return redirect(url_for('index'))
  return render_template('error_page.html')


"""Register page Check for available username. All usernames are unique"""
@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "POST":
    user = mongo.db.user
    exsisting_user = user.find_one({'name': request.form['username']})
    if exsisting_user is None:
      hashpassword = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
      user.insert_one({'name': request.form['username'], 'password': hashpassword, 'positions': []})
      session['username'] = request.form['username']
      return redirect(url_for('index'))
    return render_template('error_page.html')
  return render_template("register.html")


"""Coin list page info via CMC API"""
@app.route('/coin_list/<username>')
def coin_list(username):
  if 'username' in session:
    return render_template("coin_list.html", data=data, global_data=global_data)
  

"""create a holding of crypto"""
@app.route('/add_crypto/<username>')
def create_a_bag(username):
  if 'username' in session:
    _id = ObjectId()
    return render_template("create_a_bag.html", data=data, _id=_id, username = session['username'])
  return render_template('error_page.html')

"""push holding to db"""
@app.route('/add_to_bagz/<username>', methods=["POST"])
def add_to_bagz(username):
  if 'username' in session:
    user = mongo.db.user.update_one({'name': session['username']},
      {'$push': {'positions': {
      '_id': request.form.get('_id'),
      'asset': request.form.get('asset'),
      'amount': float(request.form.get('amount')), 
      'price_paid': float(request.form.get('price_paid')),
      'date_of_purchase': request.form.get('date_of_purchase'),
      'favorite': request.form.get('favorite')
     }}})
    return redirect(url_for('get_my_bagz', username = session['username']))
  return render_template('error_page.html')


"""display/read users puchases/holdings"""
@app.route('/my_crypto/<username>')
def get_my_bagz(username):
  if 'username' in session:
    user = mongo.db.user.find_one({'name': session['username']})
    return render_template('my_crypto.html', positions=user['positions'], data=data, username = session['username'])
  return render_template('error_page.html')

"""update users puchases/holdings"""
@app.route('/edit/<username>/<bag_id>')
def edit_bag(username, bag_id):
  if 'username' in session:
    user = mongo.db.user.find_one({'name': session['username']})
    positions=user['positions']
    for pos in positions:
      if pos['_id'] == bag_id:
       bag = pos
    return render_template("edit_bag.html", data=data, username = session['username'], bag_id=bag_id, bag=bag)
  return render_template('error_page.html')

  
"""update users puchases/holdings"""
@app.route('/update_bag/<username>/<bag_id>', methods=["POST"])
def update_bag(username, bag_id):
  user = mongo.db.user.update_one({'name': session['username'], 'positions._id': bag_id }, 
  {'$set':
  {
    'positions.$.asset': request.form.get('asset'),
    'positions.$.amount': float(request.form.get('amount')), 
    'positions.$.price_paid': float(request.form.get('price_paid')),
    'positions.$.date_of_purchase': request.form.get('date_of_purchase'),
    'positions.$.favorite': request.form.get('favorite')
  }})
  
  return redirect(url_for('get_my_bagz', username = session['username']))


"""add to an exsisting purchase or holding"""
@app.route('/add_to/<username>/<bag_id>')
def add_to_bag(username, bag_id):
  user = mongo.db.user.find_one({'name': session['username']})
  positions=user['positions']
  for pos in positions:
    if pos['_id'] == bag_id:
      bag = pos  
  return render_template('add_to.html', bag=bag, data=data, bag_id=bag_id)


"""adds to exsiting holding and creates an average buy price of the asset"""
@app.route('/adding_to_bag/<username>/<bag_id>', methods=["POST"])
def adding_to_bag(username, bag_id):
  user = mongo.db.user.find_one({'name': session['username']})
  positions=user['positions']
  for pos in positions:
    if pos['_id'] == bag_id:
      bag = pos
  """create avg price and set""" 
  newPrice = float(request.form.get('price_paid'))
  oldPrice = float(bag['price_paid'])
  avgPrice = (newPrice + oldPrice)/2
  user = mongo.db.user.update_one({'name': session['username'], 'positions._id': bag_id },
  {'$set':
  {
    'positions.$.price_paid': avgPrice 
  }})   

  """add to exsisting amount"""
  user = mongo.db.user.update_one({'name': session['username'], 'positions._id': bag_id }, 
  {'$inc':
  {
    'positions.$.amount': float(request.form.get('amount'))   
  }})  
  return redirect(url_for('get_my_bagz', username = session['username'], bag_id=bag_id))

"""delete users puchases/holdings"""
@app.route('/delete/<username>/<bag_id>')
def delete_bag(username, bag_id):
  user = mongo.db.user.update_one({'name': session['username']},
  {'$pull': {'positions': {'_id': bag_id}}})
  
  return redirect(url_for('get_my_bagz', username = session['username']))


"""EORROR routes for login page. When a user presses without logging in."""
@app.route('/coin_list/')
def coin_error():
  return render_template('error_page.html')


@app.route('/get_my_bagz/')
def get_my_error():
  return render_template('error_page.html')


@app.route('/create_a_bag/')
def create_error():
  return render_template('error_page.html')

app.secret_key = os.environ.get('MYSECRETKEY')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)