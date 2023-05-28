from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

# MANY
class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    # @classmethod
    # def get_all_recipes(cls):
    #     query = """
    #             SELECT * FROM recipes;
    #             """
    #     results = connectToMySQL('recipes').query_db(query)
    #     recipes = []
    #     for recipe in results:
    #         recipes.append(cls(recipe))
    #     return recipes

    @classmethod
    def get_all_recipes(cls):
        query= '''
            SELECT * FROM recipes 
            LEFT JOIN users 
            ON users.id = recipes.user_id;
            '''
        results = connectToMySQL('recipes').query_db(query)
        all_recipes_with_creator = []
        for row in results:
            one_recipe = cls(row)
            recipe_creator = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_recipe.creator = user.User(recipe_creator)
            all_recipes_with_creator.append(one_recipe)
        return all_recipes_with_creator


    @classmethod
    def get_recipe(cls, data):
        query= """
                SELECT * FROM recipes
                LEFT JOIN users
                ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        results = connectToMySQL('recipes').query_db(query, data)
        recipe = cls(results[0])
        # we don't need to loop because it's only giving us one line of a result, so we can just use results[0]
        recipe_creator = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                "email": results[0]['email'],
                "password": results[0]['password'],
                "created_at": results[0]['users.created_at'],
                "updated_at": results[0]['users.updated_at']
            }
        recipe.creator = user.User(recipe_creator)
        # referencing the recipe on line 64
        return recipe

    @classmethod
    def save_recipe(cls, data):
        query = """
                INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) 
                VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);
                """
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def edit_recipe(cls, data):
        query = """
                UPDATE recipes SET
                name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, 
                under_30=%(under_30)s, updated_at= NOW() WHERE id = %(id)s;
                """
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = """
                DELETE FROM recipes WHERE id = %(id)s;
                """
        return connectToMySQL('recipes').query_db(query, data)

# ====================================================================

# VALIDATIONS FOR RECIPE CREATION
    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False

        if len(form_data['description']) <3:
            flash("Description must be at least 3 characters.")
            is_valid = False

        if len(form_data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        return is_valid