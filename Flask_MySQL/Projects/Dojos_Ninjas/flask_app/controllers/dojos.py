from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo_form():
    data = {
        'name': request.form['name']
    }
    dojo_id = Dojo.save_dojo(request.form)
    return redirect(f'/dojo/{ dojo_id }')

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_one_dojo(data)
    return render_template('dojo.html', dojo=dojo)



