from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	name="Dostum"
	age=15
	return render_template('index.html', name=name, age=age)

@app.route("/register", methods=['POST','GET'])
def register():
	if request.method=='POST':
		first_name=request.form['first_name']
		return render_template('user_details.html', first_name=first_name)
	else:
		return render_template('register.html')

if __name__ == "__main__":
    app.run()