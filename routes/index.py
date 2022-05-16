# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
#import pymysql
import sqlite3
import jinja2
import requests
import json

from . import routes
@routes.route('/')
def index():
    msj = {'status':'received'}
    #return jsonify(msj)
    return render_template('index.html')
