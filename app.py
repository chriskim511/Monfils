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
		if p != None:
			if p["password"] == password:
				render_template("login.html")
				#render_template();"""
		else:
			return render_template("failedlogin.html")
	else:
		return render_template("login.html");

@app.route("/register", methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print username
		print password
		if username=="" or password=="":
			return render_template("failedregister.html")
		else:
			newacc = {"username" : username, "password": password}
			accounts.insert(newacc)
			return render_template("login.html")
	else:
		return render_template("Register.html")




if (__name__) == "__main__":
	app.debug = True
	app.run()
