from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'

@app.route('/play')
def play():
    return render_template("index.html", times=2)

@app.route('/play/<int:x>')
def playx(x):
    return render_template("index.html", times=x)

@app.route('/play/<int:x>/<string:y>')
def playxcolor(x, y):
    return render_template("index.html", times=x, color=y)

if __name__=="__main__": 
    app.run(debug=True)