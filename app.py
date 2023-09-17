from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = 'code'

@app.route("/hello")
def index():
	yourName='what is your name?'
	return render_template("index.html",name=yourName)

# {{}} and {% %} are the templateing languagee with flask

@app.route("/greet",methods =["POST"])
def greet():
	name = request.form.get('name_input')
	greeting = f'Hi, {name}!'
	return render_template("index.html", greeting=greeting)


if __name__ == '__main__':
	app.run()


"""

pip install gunicorn
echo > Procfile(here p is capital)
web: gunicorn app:app

...................

pip freeze > requirements.txt
pip install MarkupSafe( MarkupSafe==2.0.1)


and lastly send it github.com

now deployment



"""
