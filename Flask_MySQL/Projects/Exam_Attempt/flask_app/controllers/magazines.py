from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.magazine import Magazine

@app.route('/new')
def create_page():
    if 'user_id' in session:
        session_user = User.get_user({'id' : session['user_id']})
        return render_template('new.html', session_user=session_user)
    return redirect('/')

# FORM FIELD ---------------------------------------------
@app.route('/create_magazine', methods=['POST'])
def create_magazine_form():
    if Magazine.validate_magazine(request.form):
        Magazine.add_magazine(request.form)
        return redirect('/dashboard')
    else: 
        return redirect('/new')
# --------------------------------------------------------

@app.route('/show/<int:magazine_id>')
def view(magazine_id):
    if 'user_id' in session:
        session_user = User.get_user({'id' : session['user_id']})
        data = {
            'id': magazine_id
        }
        magazine = Magazine.get_magazine_with_user(data)
        return render_template('show.html', session_user=session_user, magazine=magazine)
    return redirect('/')

@app.route('/edit')
def edit_page():
    if 'user_id' in session:
        session_user = User.get_user({'id' : session['user_id']})
        return render_template('edit.html', session_user=session_user)
    return redirect('/')

@app.route('/delete_magazine/<int:magazine_id>')
def delete(magazine_id):
    data = {
        'id': magazine_id
    }
    Magazine.delete_magazine(data)
    return redirect('/account')