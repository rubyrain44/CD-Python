from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


#SERVER(HTML) > SERVER/CONTROLLER > MODEL > DB


@app.route('/')
def main_direct():
    return redirect ('/dojos')

@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template ('dojos.html', dojos=dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name'] #the left key has to match the name of the value in our query, and the right vaklue has to match the name of the value from our input
    } #if the dojo had a location value as well, and the user isn't passing us the data, we would still need a [rewuest.form] location, but it will pass in an empty value since they;re not sending it to us
    new_dojo = Dojo.save_dojo(data)
    print(new_dojo)
    return redirect ('/dojos')

@app.route ('/dojo_show/<int:dojo_id>') #you can get data 2 ways- through a url parameter or request form
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_one_dojo(data)
    print(dojo)
    return render_template ('dojo_show.html', dojo=dojo)


#a JOIN is needed when a page is requesting information from more than one table