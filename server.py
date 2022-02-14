from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'secret info'

@app.route('/')
def index():
    return render_template("index.html")
# ///////////////////////////////////////////////////////////////////

@app.route('/users', methods=["POST"])
def users_post():
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    return redirect("/afterPost")
# /////////////////////////////////////////////////////////////////////
@app.route('/afterPost')
def from_post():
    return render_template("second.html", name = session['name'], location= session['location'], language= session['language'], comment= session['comment'])


if __name__=="__main__":
    app.run(debug=True, port=5001)

