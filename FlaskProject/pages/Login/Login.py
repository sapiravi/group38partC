# from flask import Blueprint, request, current_app, jsonify, session
# from flask import render_template, redirect, url_for
# from pymongo import MongoClient
#
# cluster = MongoClient(
#     "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
# db = cluster.MyWorkoutSchedule
# customers_collection = db.Customers
#
# Login = Blueprint(
#     'Login',
#     __name__,
#     static_folder='static',
#     static_url_path='/Login',
#     template_folder='templates'
# )
#
#
# # Routes
# @Login.route('/Login', methods=['GET''POST'])
# def login_page():
#     if request.method == 'POST':
#         # Get form data
#         id = request.form.get('id')
#         password = request.form.get('password')
#
#         # Check if user exists in the Customers collection
#         customer = customers_collection.find_one({'ID': id, 'Password': password})
#
#         # Print customer data to verify if correct data is retrieved
#         print("Customer data:", customer)
#
#         if customer:
#             # Redirect to the home page if login is successful
#             return redirect(url_for('Home_Page'))
#         else:
#             # Render login page with error message
#             error_message = "ID or password is incorrect."
#             return render_template('Login.html', error_message=error_message)
#
#
#     # If it's a GET request, render the login page
#     return render_template('Login.html')
#
#
#
#
#

from flask import Blueprint, request, current_app, redirect, url_for, render_template, session
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
db = client.MyWorkoutSchedule
customers_collection = db.Customers

Login = Blueprint(
    'Login',
    __name__,
    static_folder='static',
    static_url_path='/Login',
    template_folder='templates'
)


@Login.route('/Login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # Get form data
        user_id = request.form.get("id")
        password = request.form.get("password")

        print(f"Login attempt with ID: {user_id} and password: {password}")

        # Check if user exists in the Customers collection
        customer = customers_collection.find({'ID': user_id, 'Password': password})

        if customer:
            # Store user ID in session
            session['user_id'] = user_id
            # Redirect to the home page if login is successful
            return redirect(url_for('Home_Page'))
        else:
            # Render login page with error message
            error_message = "ID or password is incorrect."
            return render_template('Login.html', error_message=error_message)

    # If it's a GET request, render the login page
    return render_template('Login.html')

#
# import logging
# from flask import Blueprint, request, current_app, redirect, url_for, render_template
#
# Login = Blueprint(
#     'Login',
#     __name__,
#     static_folder='static',
#     static_url_path='/Login',
#     template_folder='templates'
# )
#
# logger = logging.getLogger(__name__)
#
# @Login.route('/Login', methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'POST':
#         # Get form data
#         id = request.form.get("id")
#         password = request.form.get("password")
#
#         logger.info(f"Login attempt with ID: {id} and password: {password}")
#
#         # Check if user exists in the Customers collection
#         try:
#             customer = current_app.Customers_col.find_one({'ID': id, 'Password': password})
#         except Exception as e:
#             logger.error(f"Error accessing MongoDB: {e}")
#             return render_template('error.html', error_message="An error occurred. Please try again later.")
#
#         if customer:
#             logger.info(f"Login successful for ID: {id}")
#             # Redirect to the home page if login is successful
#             return redirect(url_for('Home_Page'))
#         else:
#             logger.warning(f"Login failed for ID: {id}")
#             # Render login page with error message
#             error_message = "ID or password is incorrect."
#             return render_template('Login.html', error_message=error_message)
#
#     # If it's a GET request, render the login page
#     return render_template('Login.html')
