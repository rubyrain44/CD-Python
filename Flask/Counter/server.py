from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['visits'] += 2 - 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)