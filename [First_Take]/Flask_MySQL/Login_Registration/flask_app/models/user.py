from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash
from flask_app import app
from flask_app.controllers import users
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('login_registration').query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_registration').query_db(query, data)
        print(cls(results[0]))
        return cls(results[0]) #calls the init method of the cls, and generate an instance of the class with the [0] data

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_registration').query_db(query, data)
        # Didn't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(data['register_password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if (data['register_password']) != (data['confirm_password']):
            flash("Passwords must match!")
            is_valid = False
        return is_valid

