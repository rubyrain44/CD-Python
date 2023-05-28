from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.thought import Thought

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['register_password'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    session['user_id'] = User.create_user(data)
    print(session['user_id'])
    return redirect ('/dashboard')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect ('/') 

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

############################################

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        thoughts = Thought.get_all_thoughts_with_users()
        print(thoughts)
        return render_template ('dashboard.html', logged_user=user, thoughts=thoughts)
    return redirect ('/')

@app.route('/create', methods=['POST'])
def create():
    data = {
        'thought' : request.form['thought'],
        'user_id' : session['user_id']
    }
    Thought.create_thought(data)
    return redirect('/dashboard')

# @app.route('/edit')
# def edit():
#     if 'user_id' in session:
#         user = User.get_user({'id' : session['user_id']})
#         return render_template ('edit.html', logged_user=user)
#     return redirect ('/')

# @app.route('/view')
# def view():
#     if 'user_id' in session:
#         user = User.get_user({'id' : session['user_id']})
#         return render_template ('view.html', logged_user=user)
#     return redirect ('/')

# @app.route('/delete')
# def delete():
#     if 'user_id' in session:
#         user = User.get_user({'id' : session['user_id']})
#     return redirect ('/')