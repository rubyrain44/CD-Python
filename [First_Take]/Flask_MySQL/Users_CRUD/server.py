from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__) 

#Main Page - Redirects to the Full User List
@app.route('/')
def main_redirect():
    return redirect ('/read_all')


#RENDER TEMPLATES
@app.route('/read_all')
def show_all_users():
    users = User.get_all() #users holds all the users that our query returned back to us
    print(users)
    return render_template('read_all.html', all_users = users) #we create a variable that allows the data to appear on html

@app.route('/create')
def create_page():
    return render_template('create.html')

#Add User Processing Page
@app.route('/posting', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    user = User.save(data)
    print(user)
    return redirect(f'/read_one/{ user }')

@app.route('/read_one/<int:user_id>')
def show_user(user_id): # ^ this and what goes into the value and parameter in the dictionary must match
    data = {
        'id': user_id
    }
    user = User.get_one(data)
    print(user)
    return render_template('read_one.html', user = user)

@app.route('/user_edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id': user_id,
    }
    user = User.get_one(data)
    print(user)    
    return render_template('user_edit.html', user=user)

@app.route('/updating/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.update(data)
    return redirect(f'/read_one/{ user_id }')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id': user_id,
    }   
    User.delete(data)
    return redirect('/read_all')


if __name__=="__main__":
    app.run(debug=True)