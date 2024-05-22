#!/usr/bin/env python3
import os
import dash
from dash import html
from flask import Flask, jsonify, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from wtforms import Form, StringField, validators, DateField, TextAreaField
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
#Form processing imports
from wtforms.validators import DataRequired
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models.models import Student




password = 'rooted@123'
encoded_pswd = quote(password, safe='')



app = Flask(__name__)

#Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://students:{encoded_pswd}@localhost/vla_project'
db = SQLAlchemy(app)
# Creating the tables
with app.app_context():
    db.create_all()
    
app.config['SECRET_KEY'] = password

csrf = CSRFProtect(app)




#import db models from models
from models.models import *

#Initialize Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# Dash layout
dash_app.layout = html.Div([
    html.H1('Dash in Flask'),
    # more Dash components here
    ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/Dashboard')
def Dashboard():
    return render_template('Dashboard.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/help&support')
def help():
    return render_template('help&support.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/learning_path')
def learning_path():
    return render_template('learning_path.html')

@app.route('/Library')
def Library():
    return render_template('Library.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
    
@app.route('/study')
def study():
    return render_template('study.html')
    
@app.route('/practice')
def practice():
    return render_template('practice.html') 
    
@app.route('/profile')
def profile():
    return render_template('profile.html')   
    
@app.route('/math')
def math():
    return render_template('math.html')    
    
@app.route('/physics')
def physics():
    return render_template('physics.html')    
    
@app.route('/advanced_math')
def advanced_math():
    return render_template('advanced_math.html')
    
@app.route('/signup')
def signup():
    return render_template('signup.html')         
    
@app.route('/subjects')    
def subjects():
	return render_template('subjects.html')
    
@app.route('/bug_report')
def bug_report():
	return render_template('bug_report.html')    
       
    
@app.route('/interactive_simulations')
def interactive_simulations():
    return render_template('interactive_simulations.html')
    
@app.route('/quiz_management')
def quiz_management():
    # Retrieve data for quizzes from the database
    #quizzes = retrieve_quizzes_from_database()
    return render_template('quiz_management.html')#, quizzes=quizzes)    
    

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
 
@app.route('/manage_users')
def manage_users():
    # Your code to render the template or return JSON data
    return render_template('admin/manage_users.html')
  
@app.route('/manage_subjects')
def manage_subjects():
    # Your code to render the template or return JSON data
    return render_template('admin/manage_subjects.html')

@app.route('/manage_animations')
def manage_animations():
    # Your code to render the template or return JSON data
    return render_template('admin/manage_animations.html')

@app.route('/manage_quiz')
def manage_quiz():
    # Your code to render the template or return JSON data
    return render_template('admin/manage_quiz.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')  
    
@app.route('/manage_library')
def manage_library():
    return render_template('progress.html') 
    

'''Test Insertion 2 '''

@app.route('/subject', methods=['POST'])
def add_subject():
    if request.method == 'POST':
        subject_name = request.form['subject_name']
        description = request.form['description']

        # Create a new Subject object
        new_subject = Subject(subject_name, description)

        # Add object to the session and commit changes
        db.session.add(new_subject)
        db.session.commit()
        return 'Subject added successfully!'
    return render_template('index.html')
    
@app.route('/subject', methods=['POST'])
def add_subject():
    if request.method == 'POST':
        subject_name = request.form['subject_name']
        description = request.form['description']

        # Create a new Subject object
        new_subject = Subject(subject_name, description)

        # Add object to the session and commit changes
        db.session.add(new_subject)
        db.session.commit()
        return 'Subject added successfully!'
    return render_template('index.html')
    
@app.route('/users_input', methods=['POST'])
def add_student():
    if request.method == 'POST':
        student_name = request.form['student_name']
        contact = request.form['contact']
        class_name = request.form['class_name']
        school = request.form['school']
        doj = request.form['doj']

        # Create a new Subject object
        new_student = Student(student_name, contact, class_name, school, doj)

        # Add object to the session and commit changes
        db.session.add(new_student)
        db.session.commit()
        return 'Subject added successfully!'
    return render_template('index.html')    




#create tables if running the script directly
if __name__ == '__main__':
    # Creating the tables
   # with app.app_context():
    #    db.create_all()

    # Running the Flask app
    app.config['DEBUG'] = True
    app.run(debug=True, host='0.0.0.0', port=5000)

