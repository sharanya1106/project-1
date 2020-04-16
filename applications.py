from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def test():
    return '<h1>Please add register to the html link</h1>'

@app.route('/register', methods = ['POST', 'GET'])

def register_method():
    if request.method == 'POST':
        res = request.form
        print(res)
        return render_template("result.html",result = res)
    else:
        return render_template("reg_page.html")

if __name__ =='__main__':
    app.run(debug = True)