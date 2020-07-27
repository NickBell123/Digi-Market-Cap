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
r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=50&CMC_PRO_API_KEY=' + os.environ.get('API_KEY'))
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
    
  return'Inavaild username or password'    

"""Reg page Check for available username. All usernames are unique"""
@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "POST":
    user = mongo.db.user
    exsisting_user = user.find_one({'name': request.form['username']})
    if exsisting_user is None:
      hashpassword = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
      user.insert_one({'name': request.form['username'], 'password': hashpassword})
      session['username'] = request.form['username']
      return redirect(url_for('index'))
    return 'SORRY! That username is taken'
  return render_template("register.html")


"""Coin list page info via CMC API"""
@app.route('/coin_list/<username>')
def coin_list(username):
  
  return render_template("coin_list.html", data=data, global_data=global_data)

"""create a holding of crypto"""
@app.route('/create_a_bag')
def create_a_bag():
  _id = ObjectId()
  return render_template("create_a_bag.html", data=data, _id=_id)

"""push holding to db"""
@app.route('/add_to_bagz/<username>', methods=["POST"])
def add_to_bagz(username):
  user = mongo.db.user.update_one({'name': session['username']},
  {'$push': {'positions': request.form.to_dict()}})
  
  return redirect(url_for('get_my_bagz', username = session['username']))

"""display/read users puchases/holdings"""
@app.route('/get_my_bagz/<username>')
def get_my_bagz(username):
  user = mongo.db.user.find_one({'name': session['username']})
 
  return render_template('my_bagz.html', positions=user['positions'], data=data, username = session['username'])

"""update users puchases/holdings"""
@app.route('/edit_bag/<username>/<bag_id>')
def edit_bag(username, bag_id):
  user = mongo.db.user.find_one({'name': session['username']})
  positions=user['positions']
  for pos in positions:
    if pos['_id'] == bag_id:
      bag = pos
  
  return render_template("edit_bag.html", data=data, username = session['username'], bag_id=bag_id, bag=bag)

"""update users puchases/holdings"""
@app.route('/update_bag/<username>/<bag_id>', methods=["POST"])
def update_bag(username, bag_id):
  user = mongo.db.user.update_many({'name': session['username'], 'positions._id': bag_id }, 
  {'$set':
  {
    'positions.$.asset': request.form.get('asset'),
    'positions.$.amount': request.form.get('amount'), 
    'positions.$.price_paid': request.form.get('price_paid'),
    'positions.$.date_of_purchase': request.form.get('date_of_purchase')
  }})
  
  return redirect(url_for('get_my_bagz', username = session['username']))

"""delete users puchases/holdings"""
@app.route('/delete_bag/<username>/<bag_id>')
def delete_bag(username, bag_id):
  user = mongo.db.user.update_one({'name': session['username']},
  {'$pull': {'positions': {'_id': bag_id}}})
  print(user)
  return redirect(url_for('get_my_bagz', username = session['username'])) 

if __name__ == '__main__':
    app.secret_key = os.environ.get('MYSECRETKEY')
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)