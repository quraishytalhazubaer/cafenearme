from datetime import datetime

from bson import Binary, ObjectId
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import os
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your_secret_key'
client = MongoClient('mongodb://localhost:27017/')
db_t = client.teachers
db_s = client.student
db = client['blog_db']
posts_collection = db['posts']
favourite_table = db["mainfavourite"]
comments_collection = db['comments']
app.config['UPLOAD_FOLDER'] = 'static/images'
app.debug = True

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    print('Success')
    app.run(host='127.0.0.1', port=8000)
    # serve(app, host='127.0.0.1', port=5002)
    # serve(app, host='0.0.0.0', port=80)
