from flask import Blueprint
from flask import render_template, redirect, url_for, request, jsonify,session
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
db = client.MyWorkoutSchedule
customers_collection = db.Customers

PersonalDetails = Blueprint(
    'PersonalDetails',
    __name__,
    static_folder='static',
    static_url_path='/PersonalDetails',
    template_folder='templates'
)

@PersonalDetails.route('/PersonalDetails')
def PersonalDetails_page():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))

    user_id = session['user_id']
    user_details = customers_collection.find_one({'user_id': user_id})

    return render_template('PersonalDetails.html', user_details=user_details)

@PersonalDetails.route('/update_personal_details', methods=['POST'])
def update_personal_details():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))

    user_id = session['user_id']

    if request.method == 'POST':
        data = request.form.to_dict()
        customers_collection.update_one({'user_id': user_id}, {'$set': data})
        return jsonify({'success': True, 'message': 'Details updated successfully'})

# from flask import Flask, render_template, jsonify, request, session, redirect, url_for
# from pymongo import MongoClient
#
# app = Flask(__name__)
# app.config.from_pyfile('settings.py')
#
# # Database connection
# client = MongoClient("mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
# db = client.MyWorkoutSchedule
# Customers_col = db.Customers
#
# # Homepage - Redirects to Login
# @app.route('/')
# def index():
#     return redirect(url_for('login_page'))
#
# # Logout route
# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     return redirect(url_for('login_page'))
#
# # PersonalDetails page - GET and POST methods
# @app.route('/PersonalDetails', methods=['GET', 'POST'])
# def PersonalDetails_page():
#     if 'user_id' not in session:
#         return redirect(url_for('login_page'))
#
#     user_id = session['user_id']
#     if request.method == 'POST':
#         # Handle updating personal details
#         updated_details = {
#             'FirstName': request.form['FirstName'],
#             'LastName': request.form['LastName'],
#             'PhoneNumber': request.form['PhoneNumber'],
#             'Email': request.form['Email'],
#             'Gender': request.form['Gender'],
#             'Birthdate': request.form['Birthdate']
#         }
#         Customers_col.update_one({'ID': user_id}, {'$set': updated_details})
#         return jsonify({'success': True, 'message': 'Details updated successfully'})
#     else:
#         user_details = Customers_col.find_one({'ID': user_id})
#         return render_template('PersonalDetails.html', user_details=user_details)
#
# # Home_Page route
# @app.route('/Home_Page')
# def Home_Page():
#     if 'user_id' not in session:
#         return redirect(url_for('login_page'))
#     else:
#         user_id = session['user_id']
#         user_details = Customers_col.find_one({'ID': user_id})
#         user_name = f"{user_details['FirstName']} {user_details['LastName']}" if user_details else None
#         return render_template('HomePage.html', user_name=user_name)
#
# # Login page - GET and POST methods
# @app.route('/Login', methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'POST':
#         # Handle login logic here
#         # Assuming login is successful and user ID is obtained
#         user_id = "user_id_placeholder"
#         session['user_id'] = user_id
#         return redirect(url_for('Home_Page'))
#     else:
#         return render_template('Login.html')
#
# # Database connection
# client = MongoClient("mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
# db = client.MyWorkoutSchedule
# Customers_col = db.Customers
#
# if __name__ == '_main_':
#     app.run(debug=True)