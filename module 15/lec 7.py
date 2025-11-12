from flask import Flask , render_template,request


web = Flask(__name__)



@web.route("/")
@web.route("/home")


def home():
    return render_template('Register.html')


@web.route("/confirmation" ,methods = ['POST','GET'])


def register():
    if request.method =='POST':
        name =request.form['name']
        city =request.form['city']  
        phone =request.form['phone']  
        return render_template('confirmation.html',name=name,city=city,phone=phone)            


if __name__ == "__main__":
    web.run(debug=True)