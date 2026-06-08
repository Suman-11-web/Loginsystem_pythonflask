from flask import Flask, render_template,request
import sqlite3

app=Flask(__name__)

USERNAME='SUMANM'
PASSWORD='SUMANM'

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/login', methods=["GET","POST"])
def login():
	if request.method=="POST":
		username=request.form["username"]
		password=request.form["password"]
		
		if username==USERNAME and password==PASSWORD:
			return render_template("dashboard.html")
			
		else:
			return "invalid details"
			
			
	return render_template("login.html")
	
app.run()