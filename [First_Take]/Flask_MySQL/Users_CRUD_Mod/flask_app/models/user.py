#This file is the one that will be displayed on "read_all". It creates an instance of the data in our database Users.
from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

# Say we want to categorize flash messages into different labels or buckets. We can utilize categories by passing a second argument in the flash function:
# flash("Email cannot be blank!", 'email')


#Method that queries the database for all users and returns all of them into the variable Users which holds the dictionaries.
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results: 
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data): #everything needs cls, data
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data) #needs query and data
        user = cls(results[0]) #you want to use the index so you can use that particular dictionary thats inside the list
        return user

#Method to save the data being sent from the user input to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s , NOW(), NOW());"
        return connectToMySQL('users_schema').query_db(query, data)

    # password method:  
    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
    #     return connectToMySQL("mydb").mysql.query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

#Method to update the data being sent from the user input to the database
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

#Method to delete the data being sent from the user input to the database
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)