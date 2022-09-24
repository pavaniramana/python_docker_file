from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>hello this is home page</h1>"
@app.route("/contact")
def contact():
    return "<h2>This is contact page <br></h2>"
app.run(host="0.0.0.0",port = 5000)
