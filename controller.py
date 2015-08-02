from flask import Flask, render_template, request, redirect, url_for
import json, httplib2, urllib

app = Flask(__name__)

@app.route("/")
def hello():
    return "Created new event"

@app.route("/new")
def new_event():
	return render_template('new_event.html')

@app.route("/create", methods=['POST'])
def create_new_event():
	data ={
		'event_name': request.form['event_name'],
		'event_desc': request.form['event_desc'],
		'latitude'	: request.form['position_lat'],
		'longitude'	: request.form['position_long']
	}
	header = {'Content-type':'application/json'}
	h = httplib2.Http()
	resp, content = h.request("http://45.55.27.229:9000", method="POST", body=urllib.urlencode(data), headers=header)

	print "Content received: "+content
	print request.form['event_name']+" "+request.form['event_desc']+" "+request.form['position_lat']+" "+request.form['position_long']
	return redirect(url_for('hello'))

@app.route("/login", methods=['POST'])
def login():
	return

@app.route("/logout", methods=['POST'])
def logout():
	return

if __name__ == "__main__":
    app.run(debug=True)