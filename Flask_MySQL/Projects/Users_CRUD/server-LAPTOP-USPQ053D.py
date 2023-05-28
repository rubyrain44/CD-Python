from flask import Flask, redirect, render_template, request
from user import User

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template('read_all.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add_new', methods=['POST'])
def add_new_user():
    data = {
        "first_name": request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save_user(data)
    return redirect('/users')

@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
        'id' : user_id,
    }
    user = User.get_one(data)
    return render_template('read_one.html', user=user)
    
@app.route('/edit/<int:user_id>')
def edit(user_id):
    data = {
        'id' : user_id,
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/edit_user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        'email': request.form['email']
    }
    User.edit_user(data)
    return redirect(f'/show/{ user_id }')


if __name__ == '__main__':
    app.run(debug=True)