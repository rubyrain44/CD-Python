from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app import app
from flask_app.models import user
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Band: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.genre = data['genre']
        self.home_city = data['home_city']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None #the many side would get the creator because it references the one. none is an empty placeholder.
                        ##this holds the whole user object, not just the id like above, so you can reference more of their info
        
#Create A Band
    @classmethod
    def create_band(cls, data):
        query = "INSERT INTO bands (name, user_id, genre, home_city) VALUES (%(name)s, %(user_id)s, %(genre)s, %(home_city)s);"
        ##How do you get the user_id to pass into the form?
        return connectToMySQL('python_exam').query_db(query, data)

#Get All Bands
    @classmethod
    def get_a_band(cls, data):
        query = "SELECT * FROM bands WHERE id = %(id)s;" #%()s ALWAYS NEEDS DATA. EVERYWHERE. PUT IT ^here there everywher
        results = connectToMySQL('python_exam').query_db(query, data)
        return cls(results[0])

# #Get A Band
    @classmethod
    def get_all_bands_with_users(cls): ##this method should be in the model wher the first thing youre joining is
        query = """
        SELECT * FROM bands 
        JOIN users ON bands.user_id = users.id;
        """ #you can add a where to specify the user
        results = connectToMySQL('python_exam').query_db(query)
        #one side stays outside the loop
        #the many goes in the loop
        all_users_bands = [] #to hold our many
        for row in results:
            one_band = cls(row) #(this line generates the band) #this should be the firat thing youre grabbing. -- youre passing the data in row, and taking only the class info and then stores it in the variable
            band_founding_member = {
                "id": row['users.id'], 
                "first_name": row['first_name'], ##anything that is shown in both tables same name, make sure you prepend the data with the table name
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            } #this is the rest of the data- the accessory data left over
            one_band.creator = user.User(band_founding_member) #this is adding the user object onto the bands creator 
            all_users_bands.append(one_band) #when the loop is finished, its taking the band, and the user who created it, and adding all that data into our list
        return all_users_bands #this is holding the bands and the founding member attached to them

#Validate Registration Form Data
    @staticmethod
    def validate_band(data):
        is_valid = True # we assume this is true
        if len(data['band_name']) < 2:
            flash("Band name must be at least 2 characters.")
            is_valid = False
        if len(data['music_genre']) < 2:
            flash("Music genre must be at least 2 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET name = %(name)s, genre = %(genre)s, home_city = %(home_city)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('python_exam').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM bands WHERE id = %(id)s"
        return connectToMySQL('python_exam').query_db(query, data)


# #Get A Band
#     @classmethod
#     def get_band(cls, data):
#         query = """
#         SELECT * FROM users
#         LEFT JOIN bands ON bands.user_id = users.id 
#         WHERE users.id = %(id)s;
#         """
#         results = connectToMySQL('python_exam').query_db(query, data)
#         band = cls(results[0])
#         for row in results: 
#             if row['users.id'] == None:
#                 return band
#             data = { 
#                 "id" : row['users.id'],
#                 "name" : row['name'],
#                 "user_id" : row['user_id'],
#                 "genre" : row['genre'],
#                 "home_city" : row['home_city'],
#                 "created_at" : row['users.created_at'],
#                 "updated_at" : row['users.updated_at']
#             } 
#             band.bands.append(band.Band(data))
#         return band