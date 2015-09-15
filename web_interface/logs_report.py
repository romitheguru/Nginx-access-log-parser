import MySQLdb
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

db = MySQLdb.connect('localhost','root','sha1','Logs_Statistics')
cursor = db.cursor()


app = Flask(__name__)

@app.route('/home/')
def home():
	return render_template('index.html')

@app.route('/home/logs')
def logs():
	cursor.execute('select * from logs')
	entries = [dict(key=r[1],value=r[2]) for r in cursor.fetchall()]
	return render_template('logs.html',entries=entries)

@app.route('/home/status/frequency')
def status():
	cursor.execute('select * from httpstatus')
	entries = [dict(key=r[1],value=r[2]) for r in cursor.fetchall()]
	return render_template('status.html',entries=entries)

@app.route('/home/pageviews')
def views():
	cursor.execute('select * from Pageviews')
	entries = [dict(key=r[1],value=r[2]) for r in cursor.fetchall()]
	return render_template('pageviews.html',entries=entries)

@app.route('/home/visits')
def visits():
	cursor.execute('select * from UniqueVisits')
	entries = [dict(key=r[1],value=r[2]) for r in cursor.fetchall()]
	return render_template('visits.html',entries=entries)	
	

if __name__ == '__main__':
	app.run()
