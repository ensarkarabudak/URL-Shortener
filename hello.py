from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	name="Dostum"
	age=15
	return render_template('index.html', name=name, age=age)

@app.route("/register", methods=['POST','GET'])
def register():
	if request.method=='POST':
		url=request.form['url']
		post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format('')
		payload = {'longUrl': url}
		headers = {'content-type': 'application/json'}
		cevap = requests.post(post_url, data=json.dumps(payload), headers=headers)
		return render_template('user_details.html',cevap=cevap)  
	else:
		return render_template('register.html')

if __name__ == "__main__":
    app.run()