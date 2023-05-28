#This file is the one that will be displayed on "read_all". It creates an instance of the data in our database Users.
from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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