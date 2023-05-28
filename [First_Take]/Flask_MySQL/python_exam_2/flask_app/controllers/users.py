from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.sighting import Sighting

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

##############################

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        sightings = Sighting.get_all_sightings_with_users()
        print(sightings)
        return render_template ('dashboard.html', user=user, sightings=sightings)
    return redirect ('/')

@app.route('/create')
def create_sighting():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        return render_template('create.html', user=user)
    return redirect ('/')

@app.route('/report', methods=['POST'])
def report():
    data = {
        'memo' : request.form['memo'],
        'sasquatchs' : request.form['sasquatchs'],
        'location' : request.form['location'],
        'date' : request.form['date'],
        'user_id' : session['user_id']
    }
    Sighting.create_sighting(data)
    return redirect('/dashboard')

@app.route('/view/<int:sighting_id>')
def view_sighting(sighting_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id' : sighting_id
        }
        sighting = Sighting.get_single_sighting(data)
        return render_template('view.html', user=user, sighting=sighting)
    return redirect ('/')

@app.route('/edit/<int:sighting_id>')
def edit_sighting(sighting_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id' : sighting_id
        }
        sighting = Sighting.get_single_sighting(data)
    return render_template('edit.html', user=user, sightings=sighting)

@app.route('/edit/<int:sighting_id>', methods=['POST'])
def edit(sighting_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id' : sighting_id,
            'memo' : request.form['memo'],
            'sasquatchs' : request.form['sasquatchs'],
            'location' : request.form['location'],
            'date' : request.form['date']
        }
        Sighting.update_sighting(data)
    return redirect('/dashboard')

@app.route('/delete/<int:sighting_id>', methods=["POST"])
def delete_band(sighting_id):
    data = {
        'id': sighting_id
    }
    Sighting.delete(data)
    return redirect('/dashboard')