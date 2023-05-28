# from flask import render_template, redirect, request, session, flash
# from flask_app import app
# from flask_bcrypt import Bcrypt 
# bcrypt = Bcrypt(app)
# from flask_app.models.thought import Thought
# from flask_app.models.user import User

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         user = User.get_user({'id' : session['user_id']})
#         return render_template ('dashboard.html', logged_user=user)
#     return redirect ('/')

# @app.route('/create', methods=['POST'])
# def create():
#     data = {
#         'thought' : request.form['thought'],
#         'user_id' : session['user_id']
#     }
#     Sighting.create_sighting(data)
#     return redirect('/dashboard')

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