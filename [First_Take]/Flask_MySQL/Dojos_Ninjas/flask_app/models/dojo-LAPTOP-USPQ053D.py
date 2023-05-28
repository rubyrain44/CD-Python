from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo)) #basically, calls on the Class __init__ , then passes the data
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data) #ANYTIME you have a %()s make sure you pass data, always.

        # cls - refers to the class Dojo(), also same as saying Dojo(). 
        # data - 