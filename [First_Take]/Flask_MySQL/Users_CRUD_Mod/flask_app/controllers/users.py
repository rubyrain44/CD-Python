from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument
app = Flask(__name__) 

#Main Page - Redirects to the Full User List
@app.route('/')
def main_redirect():
    return redirect ('/read_all')

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
            # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
        # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    # ... do other things
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")

#RENDER TEMPLATES
@app.route('/read_all')
def show_all_users():
    users = User.get_all() #users holds all the users that our query returned back to us
    print(users)
    return render_template('read_all.html', all_users = users) #we create a variable that allows the data to appear on html

@app.route('/create')
def create_page():
    return render_template('create.html')

#Add User Processing Page
@app.route('/posting', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    user = User.save(data)
    print(user)
    return redirect(f'/read_one/{ user }')

@app.route('/read_one/<int:user_id>')
def show_user(user_id): # ^ this and what goes into the value and parameter in the dictionary must match
    data = {
        'id': user_id
    }
    user = User.get_one(data)
    print(user)
    return render_template('read_one.html', user = user)

@app.route('/user_edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id': user_id,
    }
    user = User.get_one(data)
    print(user)    
    return render_template('user_edit.html', user=user)

@app.route('/updating/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.update(data)
    return redirect(f'/read_one/{ user_id }')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id': user_id,
    }   
    User.delete(data)
    return redirect('/read_all')


if __name__=="__main__":
    app.run(debug=True)