from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    #Hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['register_password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    # Call the save(create_user) @classmethod on User and store the user id into session
    session['user_id'] = User.create_user(data) #you can call the function, and then it becomes the ID, and session stores it
    print(session['user_id'])
    return redirect ('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']}) #you can create the data dictionary inside ()
        return render_template ('dashboard.html', user=user)
    return redirect ('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect ('/') 

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")


    # data = {
    #     'email': request.form['email'],
    #     'password': request.form['login_password']
    # }
    # user = User.get_email(data) #calls the function and then stores it in the variable
    # if not user: #you use the variable here
    #     return redirect('/')
    # if not bcrypt.check_password_hash(user.password, data['password']):
    #     return redirect ('/')
    # session['user_id'] = user.id #whenever you create a variable that is an instance of an object, you can use all its attributes. You just need to .(whatever you want to access)
    # return redirect ('/dashboard') 