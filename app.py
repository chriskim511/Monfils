from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.chrisndbrian
accounts = db.one

app = Flask(__name__)
@app.route("/")
@app.route("/login", methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		p = accounts.find_one({"username": username})
		if p != None :
			if p["password"] == password:
				render_template();
	else:
		return render_template("login.html");

@app.routej("/register")
def register():
	




if (__name__) == "__main__":
	app.debug = True
	app.run()
