from flask import Flask



web = Flask(__name__)


@web.route("/")

def home():
    return "Welcome to flask"

if __name__ =="__main__":
    web.run(debug=True)