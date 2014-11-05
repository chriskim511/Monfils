from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.chrisndbrian
accounts = db.one
profile = db.two

app = Flask(__name__)
@app.route("/")
@app.route("/login", methods = ['GET','POST'])
def login():
	return render_template("login.html");

@app.route("/register", methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print username
		print password
		if username=="" or password=="":
			return redirect('/failedregister')
		else:
			newacc = {"username" : username, "password": password}
			accounts.insert(newacc)
			return redirect('/login')
	else:
		return render_template("Register.html")

@app.route("/failedlogin")
def failedlogin():
	return render_template("failedlogin.html")

@app.route("/failedregister")
def failedregister():
	return render_template("failedregister.html")

@app.route("/index", methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		p = accounts.find_one({"username": username})
		if p != None:
			if p["password"] == password:
				return render_template("index.html")
				#render_template();"""
			else:
				return render_template("login.html")
		else:
			return redirect('/failedlogin')
			

if (__name__) == "__main__":
	app.debug = True
	app.run()
