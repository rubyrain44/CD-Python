from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Magazine:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None



# GET ALL METHODS --------------------------------------
    @classmethod
    def get_all_magazines(cls):
        query = """
                SELECT * FROM magazines;
                """
        results = connectToMySQL('exam_attempt').query_db(query)
        magazines = []
        for magazine in results:
            magazines.append(cls(magazine))
        return magazines

    @classmethod
    def get_all_magazines_with_user(cls):
        query = """
                SELECT * FROM magazines
                LEFT JOIN users
                ON users.id = magazines.user_id;
                """
        results = connectToMySQL('exam_attempt').query_db(query)
        all_magazines_with_creator = []
        for row in results:
            one_magazine = cls(row)
            magazine_creator = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            one_magazine.creator = user.User(magazine_creator)
            all_magazines_with_creator.append(one_magazine)
        return all_magazines_with_creator


# GET SINGLE METHODS --------------------------------------
    @classmethod
    def get_magazine(cls, data):
        query = """
                SELECT * FROM magazines
                WHERE id = %(id)s;
                """
        results = connectToMySQL('exam_attempt').query_db(query, data)
        return cls(results[0])
        
    @classmethod
    def get_magazine_with_user(cls, data):
        query = """
                SELECT * FROM magazines
                LEFT JOIN users
                ON magazines.user_id = users.id
                WHERE magazines.id = %(id)s;
                """
        results = connectToMySQL('exam_attempt').query_db(query, data)
        magazine = cls(results[0])
        magazine_creator = {
            'id': results[0]['users.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            "email": results[0]['email'],
            "password": results[0]['password'],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at']
            }
        magazine.creator = user.User(magazine_creator)
        return magazine


# OTHER METHODS -------------------------------------------

    @classmethod
    def add_magazine(cls, data):
        query = """
                INSERT INTO magazines
                (title, description, user_id) VALUES
                (%(title)s, %(description)s, %(user_id)s);
                """
        return connectToMySQL('exam_attempt').query_db(query, data)

    @classmethod
    def edit_magazine(cls, data):
        query = """
                UPDATE magazines SET
                title=%(title)s, description=%(description)s, updated_at = NOW ()
                WHERE id = %(id)s;
                """
        return connectToMySQL('exam_attempt').query_db(query, data)

    @classmethod
    def delete_magazine(cls, data):
        query = """
                DELETE FROM magazines
                WHERE id = %(id)s;
                """
        return connectToMySQL('exam_attempt').query_db(query, data)

# ====================================================================

# VALIDATIONS FOR MAGAZINE CREATION
    @staticmethod
    def validate_magazine(form_data):
        is_valid = True
        if len(form_data['title']) < 2:
            flash("Title must be at least 2 characters.")
            is_valid = False

        if len(form_data['description']) < 10:
            flash("Description must be at least 10 characters long.")
            is_valid = False
        return is_valid