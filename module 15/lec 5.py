# bringing html into flask


#importing 
from flask import Flask,render_template

#interaction
web = Flask(__name__)



#mapping

@web.route("/")
@web.route("/homepage")


#inputs
def homepage():
    return render_template("Register.html")


#main

if __name__ == "__main__":
    web.run(debug=True)