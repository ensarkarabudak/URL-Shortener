from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
	if request.method=='POST':
		url=request.form['url']
		post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format('')
		payload = {'longUrl': url}
		headers = {'content-type': 'application/json'}
		cevap = requests.post(post_url, data=json.dumps(payload), headers=headers)
		cevap=cevap.json()
		return render_template('url.html',cevap=cevap)  
	else:
		return render_template('index.html')

if __name__ == "__main__":
    app.run()