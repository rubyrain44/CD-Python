from flask import Flask, redirect, render_template, request
from user import User

app = Flask(__name__)
app.secret_key = "secret_key"


if __name__ == '__main__':
    app.run(debug=True)