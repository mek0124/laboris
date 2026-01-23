# app.py - Updated version
from flask import Flask, jsonify, url_for, redirect, render_template
from flask_cors import CORS
from dotenv import load_dotenv

from app.routes.dashboard import dashboard_bp

import os


load_dotenv()


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(dashboard_bp)


@app.route('/')
def index():
    user = None

    if not user:
        return render_template('welcome.html')
    
    return render_template('auth/login.html')


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True)