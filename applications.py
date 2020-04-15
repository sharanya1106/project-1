from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/register', methods = ['POST', 'GET'])

def hello():
    if request.method == 'POST':
        res = request.form
        return render_template("result.html",result = res)
    else:
        return render_template("reg_page.html")

if __name__ =='__main__':
    app.run(debug = True)