from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__) 

@app.route('/')
def main_redirect():
    return redirect ('/read_all')

@app.route('/read_all')
def allusers():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/create')
def create_page():
    return render_template('create.html')

@app.route('/posting', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)