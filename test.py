from flask import Flask,url_for,request,render_template
from markupsafe import escape,Markup

app = Flask(__name__)
#fake = Faker()

@app.route("/")
def index():
    greeting = "Hello"
    return Markup('<strong>index %s!</strong>') % greeting

@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route("/login/<username>/<int:id>")
def login(username, id):
    return f"<p> User {escape(username)} is logged in, {id}</p>"

# @app.route("/fake-data")
# def get_fake_data():
#     fname = fake.name()
#     faddress = fake.address()
#     return f"Fake Name: {fname}<br>Fake Address: {faddress}"


with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
