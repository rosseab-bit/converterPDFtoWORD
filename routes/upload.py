# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask import send_file
from flask import send_from_directory
#import pymysql
import sqlite3
import jinja2
import requests
import json
from pdf2docx import Converter
from werkzeug.utils import secure_filename
from . import routes

@routes.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save('temp/' + filename)
        pdf_file_path='temp/'
        docx_file_path='temp/'
        c=Converter('temp/' + filename)
        c.convert('temp/'+ filename)
        path='temp/'+filename
        #f.save(secure_filename(f.filename))
        #return ender_template('index.html'), send_file(path, as_attachment=True)
        return download(filename=filename)


@routes.route('/temp/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='/temp', filename=filename)
