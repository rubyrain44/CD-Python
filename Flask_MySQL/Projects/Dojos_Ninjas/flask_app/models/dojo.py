from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "dojo_id": row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(data))
        return dojo

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def edit_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(dojo_id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)