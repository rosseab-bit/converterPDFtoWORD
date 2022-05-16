# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
#import pymysql
from flask import send_from_directory
import sqlite3
import jinja2
import json
import os
from routes import *
from flask import Blueprint
from werkzeug.utils import secure_filename

#ysql = json.loads(open('conf.d/mysql.json').read())
UPLOAD_FOLDER = 'temp/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sh'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.secret_key = 'mysecretkey'
app.register_blueprint(routes)



if __name__ == '__main__':
    app.jinja_env.filters['zip'] = zip
    app.run(host="localhost", port = 5000, debug = True)
