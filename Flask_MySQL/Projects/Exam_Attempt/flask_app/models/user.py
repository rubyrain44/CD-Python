from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import magazine

# ONE
class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.magazines = []

# UPDATE USER METHOD-------------------------------
    @classmethod
    def update_user(cls, data):
        query = """
                UPDATE users SET
                first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at= NOW() 
                WHERE id = %(user_id)s;
                """
        return connectToMySQL('exam_attempt').query_db(query, data)

# LOGIN METHODS===================================================================
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('exam_attempt').query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('exam_attempt').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('exam_attempt').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# ================================================================================== 

# VALIDATIONS FOR REGISTRATION
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
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


    @staticmethod
    def validate_user_update(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid