from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login1.html")
data={'amulya':'123','vicky':'456','aaron':'prince'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pswd=request.form['password']
    if name1 not in data:
	    return render_template('login1.html',info='Invalid Username')
    else:
        if data[name1]!=pswd:
            return render_template('login1.html',info='Invalid Password try again later')
        else:
	         return render_template('home.html',name=name1)

if __name__ == '__main__':
    app.run()