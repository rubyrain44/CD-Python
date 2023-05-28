# pip install pipenv -- Installs globally (only needed once person system)
# pipenv install flask -- Installs flask
# pipenv install PyMySQL flask -- Install PyMySQL flask
# exit -- To exit (or Ctrl+C)
# pipenv install flask flask-bcrypt
#RUN PY SERVER.PY YA IDIOT!

# BOOTSTRAP LINK -- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

############################################################################

#[FOLDER] flask_app

    #[FOLDER] config
            # mysqlconnection.py

    #[FOLDER] controllers
        #Create a .py file named after what ever we are controlling in a pluralization form.
        # Move all the @app.route functions into the controller file.
        from flask import render_template, redirect, request, session, flash
        from flask_app import app
        from flask_app.models.filename import Filename

    #[FOLDER] models
        from flask_app.config.mysqlconnection import connectToMySQL
        import re	# the regex module
        from flask import flash
        from flask_bcrypt import Bcrypt 
        from flask_app import app
        bycrypt = Bcrypt(app)

    #[FOLDER] static
        #[FOLDER] css
        #[FOLDER] img
        #[FOLDER] js

    #[FOLDER] templates

        class Example:
            def __init__(self,data):
                self.id = data['id']
                self.name = data['name']
                self.bun = data['bun']
                self.meat = data['meat']
                self.calories = data['calories']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']

    #[file] __init__.py
        from flask import Flask
        app = Flask(__name__)
        app.secret_key = "shhhhhh"

#[file] server.py
    #server.py
        from flask_app import app
        from flask_app.controllers import Filename

        if __name__=="__main__":
            app.run(debug=True)