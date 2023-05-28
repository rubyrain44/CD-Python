from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.memo = data['memo']
        self.sasquatchs = data['sasquatchs']
        self.location = data['location']
        self.date = data['date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

#Create New Sighting
    @classmethod
    def create_sighting(cls, data):
        query = "INSERT INTO sightings (memo, sasquatchs, location, date, user_id) VALUES (%(memo)s, %(sasquatchs)s, %(location)s, %(date)s, %(user_id)s);"
        return connectToMySQL('sasquatch_sightings').query_db(query, data)

#Grab All Sightings, with Users attached
    @classmethod
    def get_all_sightings_with_users(cls): ##this method should be in the model wher the first thing youre joining is
        query = """
        SELECT * FROM sightings 
        JOIN users ON sightings.user_id = users.id;
        """
        results = connectToMySQL('sasquatch_sightings').query_db(query)
        all_users_sightings = [] #to hold our many
        for row in results:
            single_sighting = cls(row)
            print(single_sighting)
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
            all_users_sightings.append(single_sighting)
        return all_users_sightings #All the sightings in the database, with the user who created each attached

    @classmethod
    def get_single_sighting(cls, data):
        query = """
        SELECT * FROM sightings
        LEFT JOIN users ON sightings.user_id = users.id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL('sasquatch_sightings').query_db(query, data)
        single_sighting = cls(results[0])
        sasquatch_observer = {
            "id": results[0]['users.id'], 
            "first_name": results[0]['first_name'], 
            "last_name": results[0]['last_name'],
            "email": results[0]['email'],
            "password": results[0]['password'],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at']
        }
        single_sighting.creator = user.User(sasquatch_observer)
        return single_sighting #holding the creator and the single sighting

    @classmethod
    def update_sighting(cls, data):
        query = """
        UPDATE sightings 
        SET memo = %(memo)s, sasquatchs = %(sasquatchs)s, location = %(location)s WHERE id = %(id)s;
        """
        return connectToMySQL('sasquatch_sightings').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s"
        return connectToMySQL('sasquatch_sightings').query_db(query, data)