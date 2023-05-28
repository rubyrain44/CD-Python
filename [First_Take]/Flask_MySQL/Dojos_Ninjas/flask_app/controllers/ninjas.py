from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#You get data two ways: request.form or through the url parameter

@app.route ('/ninjas')
def ninja_page():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template ('ninjas.html', dojos=dojos)

@app.route ('/posting', methods=['POST'])
def create_ninja():
    data = { #this is a dictionary
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojos'] #pulling the id in here
    }
    ninja = Ninja.save_ninja(data) #(this grabs thde ID of the last thing created) - Inserts don't return anything else other than ID, so the insert query will insert the data into the database, and only kick back the ID to the variable that is going to hold the data that we sent into our class method.
    #^^ you don't need this if you have no reason to store the ninja informnation anything. Like if we need the ninja ID anywhere for this page.
    print(ninja)
    return redirect (f"/dojo_show/{ data['dojo_id'] }") #dict['key'], (could have also done request.form['dojs'])
                                #OR {request.form['dojos']}
