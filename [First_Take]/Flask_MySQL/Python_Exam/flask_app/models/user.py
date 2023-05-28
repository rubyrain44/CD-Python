from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app import app
from flask_app.models import band
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
        self.bands = [] #the one side gets the list

#Create A User
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('python_exam').query_db(query, data)

#Request A User
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('python_exam').query_db(query, data)
        return cls(results[0])

#See if a User exists in the DB by the email
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('python_exam').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# #Get A Band
    @classmethod
    def get_user_with_bands(cls, data): ##this method should be in the model wher the first thing youre joining is
        query = """
        SELECT * FROM users 
        LEFT JOIN bands ON bands.user_id = users.id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL('python_exam').query_db(query, data)
        #because the User already has a list in it, we don't need to create another one
        one_user = cls(results[0]) #(this line generates the user) #you need to use results[0] instead of rowm because row isnt declared yet. #this should be the firat thing youre grabbing. -- youre passing the data in row, and taking only the class info and then stores it in the variable
        for row in results:
            if row['bands.id'] == None:
                return one_user #if there are no bands, then just send back the user data
            users_band = {
                "id": row['bands.id'], 
                "name": row['name'], ##anything that is shown in both tables same name, make sure you prepend the data with the table name
                "user_id": row['user_id'],
                "genre": row['genre'],
                "home_city": row['home_city'],
                "created_at": row['bands.created_at'],
                "updated_at": row['bands.updated_at']
            } #this is the rest of the data- the accessory data left over
            one_band = band.Band(users_band) #(this line generates the user) #then we pass it into the other init method for that one
            one_user.bands.append(one_band) #this is adding the bands into the list in our init
        return one_user #this is holding the bands and the founding member attached to them

#Validate Registration Form Data
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

