from flask import Flask, jsonify, render_template, redirect
from flask_cors import CORS
from markupsafe import escape
from dotenv import load_dotenv

from .database.db import get_base, get_engine, get_db
from .models.user import User

import os


load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db = next(get_db())


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    get_base().metadata.create_all(bind=get_engine())
    app.run(debug=True)
