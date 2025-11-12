# Hyperlinks 


#  importing
from flask import Flask


app = Flask(__name__)

# mapping 

@app.route("/")


# inputs
def first():
    return render_template("home.html")



# main
if __name__ == "__main__":
    app.run()