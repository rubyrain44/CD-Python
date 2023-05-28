from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.band import Band

#Main Login Page
@app.route('/')
def index():
    return render_template ('index.html')

#Registration Form
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

#Dashboard - Success Page
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        bands = Band.get_all_bands_with_users()
        print(bands)
        return render_template ('dashboard.html', login_user=user, bands=bands)
    return redirect ('/')

#Logout - Clears Session
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect ('/') 

#Login - Users Already Created Form
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

################################################################

@app.route('/mybands')
def get_users_bands():
    if 'user_id' in session:
        data = {
            'id' : session['user_id']
        }
        user = User.get_user_with_bands(data) #passing back a user with bands
        return render_template ('mybands.html', login_user=user) #this user object is holding the list
    return redirect ('/')
    ##It is seeing the user_id in the route. What am I missing to get the data to pass and the page to load?


@app.route('/sighting')
def add_band():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        return render_template('sighting.html', login_user=user)
    return redirect ('/')

@app.route('/create_band', methods=['POST'])
def create_band():
    data = {
        'name' : request.form['band_name'],
        'genre' : request.form['music_genre'],
        'user_id' : session['user_id'],
        ##How do you get the user_id to pass into the form? Is that why it won't save to DB?
        'home_city' : request.form['home_city']
    }
    Band.create_band(data)
    return redirect('/dashboard')

@app.route('/edit/<int:band_id>')
def edit_band(band_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id' : band_id
        }
        band = Band.get_a_band(data)
        return render_template('edit.html', login_user=user, band=band)
    return redirect ('/')

@app.route('/edit_band/<int:band_id>', methods=['POST'])
def update_user(band_id):
    data = {
        'id': band_id,
        'name': request.form['band_name'],
        'genre' : request.form['music_genre'],
        'home_city' : request.form['home_city']
    }
    Band.update(data)
    return redirect('/dashboard')

@app.route('/delete/<int:band_id>')
def delete_band(band_id):
    data = {
        'id': band_id
    }
    Band.delete(data)
    return redirect('/dashboard')
