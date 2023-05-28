from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash
from flask_app import app
from flask_app.models import sighting
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
        self.sightings = []

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('sasquatch_sightings').query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('sasquatch_sightings').query_db(query, data)
        print(cls(results[0]))
        return cls(results[0]) #calls the init method of the cls, and generate an instance of the class with the [0] data

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('sasquatch_sightings').query_db(query, data)
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

###############################

#Grab All Sightings, with Users attached
    @classmethod
    def get_all_sightings_with_users(cls): ##this method should be in the model wher the first thing youre joining is
        query = """
        SELECT * FROM users 
        JOIN sightings ON sightings.user_id = users.id;
        """
        results = connectToMySQL('sasquatch_sightings').query_db(query)
        all_users_sightings = [] #to hold our many
        for row in results:
            single_sighting = cls(row)
            sasquatch_observer = {
                "id": row['users.id'], 
                "first_name": row['first_name'], 
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            single_sighting.creator = user.User(sasquatch_observer)
        return all_users_sightings #All the sightings in the database, with the user who created each attached
