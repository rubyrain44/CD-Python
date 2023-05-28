from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import recipe

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
        self.recipes = []
        # self.number_of_recipes = 0

    @classmethod
    def get_single_users_recipes(cls, data):
        query = """
                SELECT * FROM users
                LEFT JOIN recipes
                ON recipes.user_id = users.id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL('recipes').query_db(query, data)
        single_user = cls(results[0])
        for row in results:
            single_users_recipes = {
                'id': row['recipes.id'],
                'name': row['name'],
                'description': row['description'],
                'instructions': row['instructions'],
                'date_made': row['date_made'],
                'under_30': row['under_30'],
                'user_id': row['user_id'],
                'created_at': row['recipes.created_at'],
                'updated_at': row['recipes.updated_at']
            }
            one_recipe = recipe.Recipe(single_users_recipes)
            single_user.recipes.append(one_recipe)
            # single_user.number_of_recipes += 1 (this is how you can update the number_of_recipes in User)
            # this is the line that adds each recipe and adds it to the list
        # single_user.number_of_recipes = len(single_user.recipes) = (this way shows the length of recipes in the recipe [] list)
        return single_user

# LOGIN METHODS===================================================================
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# ================================================================================== 

# VALIDATIONS FOR REGISTRATION
    @staticmethod
    def validate_user(data):
        is_valid = True
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