from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def form():
    session['form_data'] = 'form_data'
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_form():
    session['your_name'] = request.form['your_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment_box'] = request.form['comment_box']
    print(session['fav_language'])
    return redirect('/results')    

@app.route('/results')
def results():
    return render_template("results.html")  

if __name__=="__main__": 
    app.run(debug=True)