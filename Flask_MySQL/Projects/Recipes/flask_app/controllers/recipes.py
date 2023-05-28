from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


# MAIN PAGE - DASHBOARD
@app.route('/recipes')
def dashboard():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        recipes = Recipe.get_all_recipes()
        return render_template ('recipes.html', user=user, recipes=recipes)
    return redirect ('/')

@app.route('/view_recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id': recipe_id
        }
        recipe = Recipe.get_recipe(data)
        return render_template ('view_recipe.html', user=user, recipe=recipe)
    return redirect('/')

@app.route('/create_recipe')
def create_recipe():
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        return render_template('create_recipe.html')
    return redirect('/')


# FORM FIELD ---------------------------------------------
@app.route('/create', methods=['POST'])
def create_recipe_form():
    if Recipe.validate_recipe(request.form):
        recipe_id = Recipe.save_recipe(request.form)
        return redirect(f'/view_recipe/{ recipe_id }')
    else: 
        return redirect('/create_recipe')
# --------------------------------------------------------


@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' in session:
        user = User.get_user({'id' : session['user_id']})
        data = {
            'id': recipe_id
        }
        recipe = Recipe.get_recipe(data)
        return render_template('edit_recipe.html', user=user, recipe=recipe)
    return redirect ('/')


# FORM FIELD ---------------------------------------------
@app.route('/edit', methods=['POST'])
def edit():
    if Recipe.validate_recipe(request.form):
        recipe = Recipe.edit_recipe(request.form)
        return redirect(f'/view_recipe/{ request.form["id"] }')
    else: 
        return redirect(f'/edit_recipe/{ request.form["id"] }')
# --------------------------------------------------------


@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect('/recipes')


# BONUS: VIEW ALL CREATORS RECIPES
@app.route('/one_user_recipes/<int:recipes_user_id>')
def one_user_recipes(recipes_user_id):
    if 'user_id' in session:
        logged_user = User.get_user({'id' : session['user_id']})
        data = {
            'id': recipe_user_id
        }
        recipe_user = User.get_single_users_recipes(data)
        return render_template('one_user_recipes.html', recipe_user=recipe_user, logged_user=logged_user)
    return redirect ('/')