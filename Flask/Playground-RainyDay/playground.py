from flask import Flask, render_template

app = Flask(__name__) 


@app.route('/play')
def index():
    return render_template('play.html')

@app.route('/play/<int:num>/<string:color>')
def play_multiplier(num, color):
    return render_template('play.html', num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)