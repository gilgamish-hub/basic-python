#importing 
from flask import Flask

#interaction
web = Flask(__name__)



#mapping

@webroute("/")
@web.route("/home")


#inputs
def home():
    return "Welcome home"


#main

if __name__ == "__main__":
    web.run(debug=True)