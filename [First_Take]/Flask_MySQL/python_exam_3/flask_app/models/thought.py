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

#Create New Thought
    @classmethod
    def create_thought(cls, data):
        query = "INSERT INTO thoughts (thought, user_id) VALUES (%(thought)s, %(user_id)s);"
        return connectToMySQL('my_thoughts').query_db(query, data)


    # @classmethod
    # def get_single_sighting(cls, data):
    #     query = """
    #     SELECT * FROM sightings
    #     LEFT JOIN users ON sightings.user_id = users.id
    #     WHERE users.id = %(id)s;
    #     """
    #     results = connectToMySQL('sasquatch_sightings').query_db(query, data)
    #     single_sighting = cls(results[0])
    #     sasquatch_observer = {
    #         "id": results[0]['users.id'], 
    #         "first_name": results[0]['first_name'], 
    #         "last_name": results[0]['last_name'],
    #         "email": results[0]['email'],
    #         "password": results[0]['password'],
    #         "created_at": results[0]['users.created_at'],
    #         "updated_at": results[0]['users.updated_at']
    #     }
    #     single_sighting.creator = user.User(sasquatch_observer)
    #     return single_sighting #holding the creator and the single sighting

    # @classmethod
    # def update_sighting(cls, data):
    #     query = """
    #     UPDATE sightings 
    #     SET memo = %(memo)s, sasquatchs = %(sasquatchs)s, location = %(location)s WHERE id = %(id)s;
    #     """
    #     return connectToMySQL('sasquatch_sightings').query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM sightings WHERE id = %(id)s"
    #     return connectToMySQL('sasquatch_sightings').query_db(query, data)