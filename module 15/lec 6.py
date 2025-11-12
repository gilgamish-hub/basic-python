from flask import Flask , render_template

web = Flask(__name__)
@web.route("/")
@web.route("/home")


def home():
    return render_template("Register.html")



if __name__ =="__main__":
    web.run(debug=True)
