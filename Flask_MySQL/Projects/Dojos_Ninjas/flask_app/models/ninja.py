from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.age = data['age']
            self.dojo_id = data['dojo_id']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninjas in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        ninja = cls(results[0])
        return ninja

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def edit_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)