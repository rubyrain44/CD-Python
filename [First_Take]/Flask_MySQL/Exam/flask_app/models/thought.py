from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app import app
from flask_app.models import user
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Thought: 
    def __init__(self, data):
        self.id = data['id']
        self.thought = data['thought']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    #Grab All Sightings, with Users attached
    @classmethod
    def get_all_thoughts_with_users(cls):
        query = """
        SELECT * FROM thoughts 
        JOIN users ON thoughts.user_id = users.id;
        """
        results = connectToMySQL('exam').query_db(query)
        all_users_thoughts = []
        for row in results:
            single_thought = cls(row)
            print(single_thought)
            thought_poster = {
                "id": row['users.id'], 
                "first_name": row['first_name'], 
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            single_thought.creator = user.User(thought_poster)
            all_users_thoughts.append(single_thought)
        return all_users_thoughts

    # @classmethod
    # def get_single_thought(cls, data):
    #     query = """
    #     SELECT * FROM thoughts
    #     LEFT JOIN users ON thoughts.user_id = users.id
    #     WHERE users.id = %(id)s;
    #     """
    #     results = connectToMySQL('exam').query_db(query, data)
    #     single_thought = cls(results[0])
    #     thought_poster = {
    #         "id": results[0]['users.id'], 
    #         "first_name": results[0]['first_name'], 
    #         "last_name": results[0]['last_name'],
    #         "email": results[0]['email'],
    #         "password": results[0]['password'],
    #         "created_at": results[0]['users.created_at'],
    #         "updated_at": results[0]['users.updated_at']
    #     }
    #     single_thought.creator = user.User(thought_poster)
    #     return single_thought