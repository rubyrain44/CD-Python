from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User

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
    user_id = User.save_user(request.form)
    print(user)
    return redirect(f'/show/{ user_id }')

@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
        'id' : user_id,
    }
    user = User.get_one(data)
    return render_template('read_one.html', user=user)
    
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id' : user_id,
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/edit_user', methods=['POST'])
def edit():
    # data = {
    #     "id": user_id,
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     'email': request.form['email']
    # }
    User.edit_user(request.form)
    return redirect(f'/show/{ request.form["user_id"] }') 
    #the stuff in the [' '] is the name of the form input youre referencing

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id': user_id,
    }
    User.delete_user(data)
    return redirect('/users')

