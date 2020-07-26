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
# Api call for individual cryptos
r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=50&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
results = r.json()
data = results['data']
# Api call for global crypto stats
r = requests.get('https://pro-api.coinmarketcap.com//v1/global-metrics/quotes/latest?&CMC_PRO_API_KEY=7d99530e-32dc-4fff-96ee-4b3811b660de')
results = r.json()
global_data = results['data']

# Check for user session or display login
@app.route('/')
def index():
  if 'username' in session:
    return redirect(url_for('coin_list', username = session['username']))

  return render_template("index.html")

# check login values
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


# Register for new users, check for vaild username (one which has not be taken)
@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "POST":
    user = mongo.db.user
    exsisting_user = user.find_one({'name': request.form['username']})
    # if no matching username found
    if exsisting_user is None:
      hashpassword = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
      user.insert_one({'name': request.form['username'], 'password': hashpassword})
      session['username'] = request.form['username']
      return redirect(url_for('index'))
    return 'SORRY! That username is taken'
  return render_template("register.html")

# Api individual coin stat route
@app.route('/coin_list/<username>')
def coin_list(username):
  
  return render_template("coin_list.html", data=data, global_data=global_data)

#Create a purchase or holding of crypto
@app.route('/create_a_bag/<username>')
def create_a_bag(username):
  user = mongo.db.user.find_one({'name': session['username']})
  _id = ObjectId()
  return render_template('create_a_bag.html', positions=user['positions'], username = session['username'], data=data, _id=_id)

  

#Add the purchase/holding to my bags function
@app.route('/add_to_bagz/<username>', methods=["POST"])
def add_to_bagz(username):
  user = mongo.db.user.update_one({'name': session['username']},
  {'$push': {'positions': request.form.to_dict()}})
  
  return redirect(url_for('get_my_bagz', username = session['username']))

#display/read users puchases/holdings
@app.route('/get_my_bagz/<username>')
def get_my_bagz(username):
  user = mongo.db.user.find_one({'name': session['username']})
 
  return render_template('my_bagz.html', positions=user['positions'], data=data, username = session['username'])

#update users puchases/holdings
@app.route('/edit_bag/<username>/<bag_id>')
def edit_bag(username, bag_id):
  user = mongo.db.user.find_one({'name': session['username']})
  positions = user['positions']
  for bag in positions:
    if bag['_id'] == ObjectId(bag_id):
      the_bag = bag
    print(bag['_id'])  

  # the_bag = mongo.db.user.find({"positions":{"_id": ObjectId(bag_id)}})
  return render_template("edit_bag.html", bag=the_bag, data=data, username = session['username'])

#update users puchases/holdings
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

#delete users puchases/holdings
@app.route('/delete_bag/<bag_id>')
def delete_bag(bag_id):
  mongo.db.users.delete_one({'_id': ObjectId(bag_id)})
  return redirect(url_for('get_my_bagz')) 

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'), 
        port=(os.environ.get('PORT')),
        debug=True)