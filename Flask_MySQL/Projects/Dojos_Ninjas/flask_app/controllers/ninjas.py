from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/create_ninja')
def create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos=dojos)

@app.route('/create_new_ninja', methods=["POST"])
def create_new_ninja_form():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save_ninja(data)
    return redirect(f"/dojo/{ data['dojo_id'] }")