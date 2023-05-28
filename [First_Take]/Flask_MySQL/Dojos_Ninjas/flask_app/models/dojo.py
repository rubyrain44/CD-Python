from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models import ninja #lowercase is importing the file, not the class

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = [] #this is a list, we need this for our ninjas to be stored into after running our query

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data): 
        query = """
            SELECT * FROM dojos 
            LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
            """ #this is only showing us the things, but we're not storing it yet
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo_instance = cls(results[0]) #this is passing up to the class Dojo and creating an instance. Without a space for the ninjas, they won't get saved.
        # pprint(results, sort_dicts=False, width=1)
        for row in results: #refers to the specfic row of the dictionary coming back
            if row['ninjas.id'] == None: #this helps to avoid getting Null data, it would send back the Dojo data, and just ignore the ninja stuff
                return dojo_instance
            data = { #row must match in both places, and it will update the information passing through, but those things that are named the same in both places like id and created/updated at, you must __. the table you are wanting the information saved from.
                "id" : row['ninjas.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "dojo_id" : row['dojo_id'],
                "created_at" : row['ninjas.created_at'],
                "updated_at" : row['ninjas.updated_at']           
            } #this is for the ninja information
            dojo_instance.ninjas.append(ninja.Ninja(data)) #this matches the dojo we made on line 29, the ninjas matches up the line inside our constructor on line 10. The stuff inside the parenthesis is 
            #code is read inner most ()'s. So we're starting with our data first, going into our Ninja class by using the lowercase ninja file to access it. Then we append to the ninjas in our current model, and the empty list on our dojo object. 
        return dojo_instance

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data)