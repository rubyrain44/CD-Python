from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "shh"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def user_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['Language'] = request.form['Language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)