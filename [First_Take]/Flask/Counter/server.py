from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def render_counter():
    if 'visits' in session:
        session['visits'] += 1
        print('key exists!')
        print(session['visits'])
    else:
        session['visits'] = 1 
        print("key 'key_name' does NOT exist")
    return render_template("index.html")

@app.route('/add')
def add_counter():
    if 'visits' in session:
        session['visits'] += 2 -1
        print('key exists!')
        print(session['visits'])
    return redirect('/')

@app.route('/addmore', methods=['POST'])
def addmore_counter():
    if 'visits' in session:
        session['visits'] += int(request.form['visitcount']) -1
        print('key exists!')
        print(session['visits'])
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    print('BYE FELICIA!')
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)


# session is a dictionary

