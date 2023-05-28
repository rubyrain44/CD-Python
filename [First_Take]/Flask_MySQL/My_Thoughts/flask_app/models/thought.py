from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

class Thought:
    def __init__(self, data):
        self.id = data['id']
        self.thought = data['thought']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def create_thought(cls, data):
        query = "INSERT INTO thoughts (thought, user_id) VALUES (%(thought)s, %(user_id)s);"
        return connectToMySQL('thoughts').query_db(query, data)

    #Grab All Sightings, with Users attached
    @classmethod
    def get_all_thoughts(cls): ##this method should be in the model wher the first thing youre joining is
        query = """
        SELECT * FROM users 
        JOIN thoughts ON thoughts.user_id = users.id;
        """
        results = connectToMySQL('thoughts').query_db(query)
        all_users_thoughts = [] #to hold our many
        for row in results:
            single_thought = cls(row)
            thought_poster = {
                "id" : row['id'], 
                "first_name" : row['first_name'], 
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            single_thought.creator = user.User(thought_poster)
        return all_users_thoughts #All the sightings in the database, with the user who created each attached
