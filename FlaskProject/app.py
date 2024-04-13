# # from flask import Flask
# #
# # ###### App setup
# # app = Flask(__name__)
# # app.config.from_pyfile('settings.py')
# #
# # ###### Pages
# #
# #
# # ## Login
# # from pages.Login.Login import login
# #
# # app.register_blueprint(login)
# #
# # ## Personal Datails
# # from pages.PersonalDetails.PersonalDetails import PersonalDetail
# #
# # app.register_blueprint(PersonalDetail)
# #
# # ## MyPreviousWorkouts
# # from pages.MyPreviousWorkouts.MyPreviousWorkouts import MyPreviousWorkouts
# #
# # app.register_blueprint(MyPreviousWorkouts)
# #
# # ## Register
# # from pages.Register.Register import Register
# #
# # app.register_blueprint(Register)
# # #
# # # ## Page error handlers
# # # from pages.page_error_handlers.page_error_handlers import page_error_handlers
# # #
# # # app.register_blueprint(page_error_handlers)
# # #
# # # ###### Components
# # # ## Main MyPreviousWorkouts
# # # from components.main_menu.main_menu import main_menu
# # #
# # # app.register_blueprint(main_menu)
# # #
# # #
# # # if __name__ == '__main__':
# # #     app.run(debug=True)
# #
# # from flask import Flask, redirect, url_for
# # from flask import render_template
# #
# # app = Flask(__name__)
# #
# #
# #
# #
# # @app.route('Login')
# # def login():
# #     return render_template(login.html)
#
# from flask import Flask, render_template, jsonify, request, session, redirect, url_for
#
#
# from pages.HomePage.HomePage import HomePage
# from pages.Login.Login import Login
# from pages.MyPreviousWorkouts.MyPreviousWorkouts import MyPreviousWorkouts
# from pages.PersonalDetails.PersonalDetails import PersonalDetails
# from pages.Register.Register import Register
#
# app = Flask(__name__)
# app.config.from_pyfile('settings.py')
#
# # Blueprint registration
# app.register_blueprint(Login, url_prefix='/Login')
# app.register_blueprint(HomePage, url_prefix='/HomePage')
# app.register_blueprint(PersonalDetails, url_prefix='/PersonalDetails')
# app.register_blueprint(MyPreviousWorkouts, url_prefix='/MyPreviousWorkouts')
# app.register_blueprint(Register, url_prefix='/Register')
#
# # Route for the login page
# def get_user_name(user_id):
#     # Retrieve user data from the database based on user ID
#     user_data = Customers_col.find_one({'ID': user_id})
#
#     # Concatenate first name and last name to form full name
#     full_name = f"{user_data['FirstName']} {user_data['LastName']}" if user_data else None
#     return full_name
#
# @app.route('/Login', methods=['GET', 'POST'])
# @app.route('/')
# def login_page():
#     return render_template('Login.html')
#
#
# @app.route('/HomePage')
# @app.route('/HomePage.html')
# def Home_Page():
#     # Retrieve user ID from session
#     user_id = session.get('user_id')
#     # Retrieve user name using the user ID
#     user_name = get_user_name(user_id)
#     return render_template('HomePage.html', user_name=user_name)
# def logout():
#     # Remove user ID from session
#     session.pop('user_id', None)
#     # Redirect to the login page
#     return redirect(url_for('login_page'))
#
# @app.route('/PersonalDetails')
# def PersonalDetails_page():
#     return render_template('PersonalDetails.html')
#
# # Route to update personal details
# @app.route('/update_personal_details', methods=['POST'])
# def update_personal_details():
#     data = request.json
#
#     # Extract user ID and updated details from the request
#     user_id = data.get('ID')
#     updated_details = {
#         'FirstName': data.get('FirstName'),
#         'LastName': data.get('LastName'),
#         'PhoneNumber': data.get('PhoneNumber'),
#         'Email': data.get('Email'),
#         'Gender': data.get('Gender'),
#         'Birthdate': data.get('Birthdate'),
#         'Password': data.get('Password')  # Update other fields as needed
#     }
#
#     try:
#         # Update the user's personal details in the database
#         Customers_col.update_one({'ID': user_id}, {'$set': updated_details})
#         return jsonify({'success': True, 'message': 'Personal details updated successfully'})
#     except Exception as e:
#         return jsonify({'success': False, 'message': str(e)}), 500
#
# @app.route('/Register')
# def Register_page():
#     return render_template('Register.html')
#
# @app.route('/MyPreviousWorkouts')
# def MyPreviousWorkouts_page():
#     return render_template('MyPreviousWorkouts.html')
#
#
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
#
# uri = "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#
# # Create a new client and connect to the server
# cluster = MongoClient(uri, server_api=ServerApi('1'))
#
#
#
# # Test database connection
# try:
#     client = MongoClient("mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     db = client.MyWorkoutSchedule  # Change to your actual database name
#     print("Connected to MongoDB")
# except Exception as e:
#     print("Failed to connect to MongoDB:", e)
#
#
# def create_database():
#     db = cluster["mydatabase"]
#     print("Database created successfully!")
#
#
# mydatabase=cluster['MyWorkoutSchedule']
# Members_col= mydatabase['Members']
# # Customers_col: Collection
# Customers_col= mydatabase['Customers']
#
# Branch_col= mydatabase['Branch']
# Workouts_col= mydatabase['Workouts']
# WorkoutDetails_col= mydatabase['WorkoutDetails']
#
# # WorkoutDetails
# # Define your list of new documents
# WorkoutDetails_col_list = [
#     {'Date': '03/05/2024', 'Time': '17:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Zumba'},
#     {'Date': '03/07/2024', 'Time': '18:30', 'Branch': 'Studio Life', 'Workout': 'Pilates'},
#     {'Date': '03/09/2024', 'Time': '16:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Yoga'},
#     {'Date': '03/11/2024', 'Time': '19:00', 'Branch': 'Studio Life', 'Workout': 'CrossFit'},
#     {'Date': '03/13/2024', 'Time': '20:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Spinning'},
#     {'Date': '03/15/2024', 'Time': '17:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Zumba'},
#     {'Date': '03/17/2024', 'Time': '18:30', 'Branch': 'Studio Life', 'Workout': 'Pilates'},
#     {'Date': '03/19/2024', 'Time': '16:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Yoga'},
#     {'Date': '03/21/2024', 'Time': '19:00', 'Branch': 'Studio Life', 'Workout': 'CrossFit'},
#     {'Date': '03/23/2024', 'Time': '20:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Spinning'}
# ]
# def check_duplicate(collection, new_document):
#     existing_doc = collection.find_one({
#         'Date': new_document['Date'],
#         'Time': new_document['Time'],
#         'Branch': new_document['Branch'],
#         'Workout': new_document['Workout']
#     })
#
#     return existing_doc is not None
#
# # Iterate over each document and insert it into the collection if it's not a duplicate
# # for doc in WorkoutDetails_col_list:
# #     if not check_duplicate(WorkoutDetails_col, doc):
# #         WorkoutDetails_col.insert_one(doc)
# #         print("New document inserted successfully.")
# #     else:
# #         print("Document already exists. Skipping insertion.")
#
# def add_workout_details():
#     # Retrieve new workout details from the request
#     data = request.json
#
#     # Validate the data (perform any necessary checks)
#
#     # Check for duplicates
#     existing_workout = WorkoutDetails_col.find_one(data)
#     if existing_workout:
#         return jsonify({'error': 'Workout details already exist'}), 400
#
#     # Insert the new workout details into the database
#     WorkoutDetails2={'Date': '04/23/2024', 'Time': '20:00', 'Branch': 'Studio Tel-Aviv', 'Workout': 'Spinning'}
#     WorkoutDetails_col.insert_one(WorkoutDetails2)
#
#
#
#
# # Workouts
# def update_workouts(collection, data_list):
#     # Get the list of existing names in the collection
#     existing_names = [doc['Name'] for doc in collection.find({}, {'Name': 1})]
#
#     # Filter out data_list to exclude documents with existing names
#     filtered_data_list = [data for data in data_list if data['Name'] not in existing_names]
#
#     if filtered_data_list:
#         # Insert filtered documents
#         collection.insert_many(filtered_data_list)
#         print(f"{len(filtered_data_list)} new workouts inserted successfully.")
#     else:
#         print("No new workouts to insert.")
#
# # Define your Workouts_col_list
# Workouts_col_list = [
#     {'Name': 'Zumba'},
#     {'Name': 'Pilates'},
#     {'Name': 'Yoga'},
#     {'Name': 'Crossfit'},
#     {'Name': 'Spinning'}
# ]
#
# # Call the function to update records in the Workouts collection
# update_workouts(Workouts_col, Workouts_col_list)
#
#
# # Branch
# def update_branches(collection, data_list):
#     # Get the list of existing names in the collection
#     existing_names = [doc['Name'] for doc in collection.find({}, {'Name': 1})]
#
#     # Filter out data_list to exclude documents with existing names
#     filtered_data_list = [data for data in data_list if data['Name'] not in existing_names]
#
#     if filtered_data_list:
#         # Insert filtered documents
#         collection.insert_many(filtered_data_list)
#         print(f"{len(filtered_data_list)} new branches inserted successfully.")
#     else:
#         print("No new branches to insert.")
#
# # Define your Branch_col_list
# Branch_col_list = [
#     {'Name': 'Studio Life', 'City': 'Ashdod'},
#     {'Name': 'Studio Tel-aviv', 'City': 'Tel-aviv'}
# ]
#
# # Call the function to update records in the Branch collection
# update_branches(Branch_col, Branch_col_list)
#
#
# # Customers
# def update_records(collection, data_list):
#     for data in data_list:
#         # Check if a document with the same ID already exists
#         existing_doc = collection.find_one({'ID': data['ID']})
#
#         if existing_doc:
#             print(f"Document with ID {data['ID']} already exists. Skipping insertion.")
#         else:
#             # Insert the document if it doesn't already exist
#             collection.insert_one(data)
#             print(f"New document with ID {data['ID']} inserted successfully.")
#
#
#
#
# # Define your Customers_col_list
# Customers_col_list = [
#     {
#         'ID': '123456789',
#         'FirstName': 'John',
#         'LastName': 'Doe',
#         'PhoneNumber': '5551234567',
#         'Email': 'john.doe@example.com',
#         'Gender': 'Male',
#         'Birthdate': '1990-05-15',
#         'Password': 'password1'
#     },
#     {
#         'ID': '234567890',
#         'FirstName': 'Jane',
#         'LastName': 'Smith',
#         'PhoneNumber': '5552345678',
#         'Email': 'jane.smith@example.com',
#         'Gender': 'Female',
#         'Birthdate': '1985-08-22',
#         'Password': 'password2'
#     },
#     {
#         'ID': '345678901',
#         'FirstName': 'Michael',
#         'LastName': 'Johnson',
#         'PhoneNumber': '5553456789',
#         'Email': 'michael.johnson@example.com',
#         'Gender': 'Male',
#         'Birthdate': '1988-12-10',
#         'Password': 'password3'
#     }
# ]
#
# # Call the function to update records in the Customers collection
# # update_records(Customers_col, Customers_col_list)
#
#
#
#
#
# # Members_col.insert_one(my_dict)
# # # message = cluster.list_database_names()
# # message = mydatabase.list_collection_names()
#
# members_data= [
#     {'name': 'hey', "address": "John", "rating": "2"},
#     {'name': 'lof', "address": "vv", "rating": "2"}
#
# ]
# Members_col.insert_many(members_data)
# message = mydatabase.list_collection_names()
#
# # members_data= [
# #     {"ID": 123456789, "FirstName": "John", "LastName": "Doe", "PhoneNumber": "5551234567",
# #      "Email": "john.doe@example.com", "Gender": "Male", "Birthdate": "1990-05-15", "Password": "password1"},
# #     {"ID": 234567890, "FirstName": "Jane", "LastName": "Smith", "PhoneNumber": "5552345678",
# #      "Email": "jane.smith@example.com", "Gender": "Female", "Birthdate": "1985-08-22", "Password": "password2"}
# #
# # ]
# # Members_col.insert_many(members_data)
# # message = mydatabase.list_collection_names()
#
#
# # @app.route('/mongodb')
# # def mongodb_func():
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient

from pages.HomePage.HomePage import HomePage
from pages.Login.Login import Login
from pages.MyPreviousWorkouts.MyPreviousWorkouts import MyPreviousWorkouts
from pages.PersonalDetails.PersonalDetails import PersonalDetails
from pages.Register.Register import Register

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Blueprint registration
app.register_blueprint(Login, url_prefix='/Login')
app.register_blueprint(HomePage, url_prefix='/HomePage')
app.register_blueprint(PersonalDetails, url_prefix='/PersonalDetails')
app.register_blueprint(MyPreviousWorkouts, url_prefix='/MyPreviousWorkouts')
app.register_blueprint(Register, url_prefix='/Register')

# Route for the login page
@app.route('/Login', methods=['GET', 'POST'])
@app.route('/')
def login_page():
    return render_template('Login.html')


@app.route('/HomePage')
@app.route('/HomePage.html')
def Home_Page():
    # Retrieve user ID from session
    user_id = session.get('user_id')
    # Retrieve user name using the user ID
    user_name = get_user_name(user_id)
    return render_template('HomePage.html', user_name=user_name)

def logout():
    # Remove user ID from session
    session.pop('user_id', None)
    # Redirect to the login page
    return redirect(url_for('login_page'))

@app.route('/PersonalDetails')
def PersonalDetails_page():
    # Assuming you have a session variable user_id set with the current user's ID
    user_id = session.get('user_id')
    # Fetch user details from MongoDB Atlas based on user_id
    user_details = get_user_name(user_id)
    user_i_d = get_user_id(user_id)
    user_phone = get_user_phone(user_id)
    user_email = get_user_email(user_id)
    user_gender = get_user_gender(user_id)
    user_firstname = get_user_firstname(user_id)
    user_lastname = get_user_lastname(user_id)
    user_birthdate = get_user_birthdate(user_id)

    # Pass user_details to the template context
    return render_template('PersonalDetails.html', user_details=user_details, user_i_d=user_i_d
                           ,user_phone=user_phone, user_email=user_email, user_gender=user_gender,
                           user_firstname=user_firstname, user_lastname=user_lastname, user_birthdate=user_birthdate)


@app.route('/update_details', methods=['POST'])
def update_details():
    # Retrieve the data from the form
    user_id = request.form.get('id')
    user_phone = request.form.get('phone')
    user_email = request.form.get('email')
    user_gender = request.form.get('gender')
    user_firstname = request.form.get('firstname')
    user_lastname = request.form.get('lastname')
    user_birthdate = request.form.get('birthdate')

    # Update the data in the database
    Customers_col.update_one({'ID': user_id}, {'$set': {'Phone': user_phone}})
    Customers_col.update_one({'ID': user_id}, {'$set': {'Email': user_email}})
    Customers_col.update_one({'ID': user_id}, {'$set': {'Gender': user_gender}})
    Customers_col.update_one({'ID': user_id}, {'$set': {'FirstName': user_firstname}})
    Customers_col.update_one({'ID': user_id}, {'$set': {'LastName': user_lastname}})
    Customers_col.update_one({'ID': user_id}, {'$set': {'Birthdate': user_birthdate}})
    # Update other fields in a similar way

    # Redirect back to the PersonalDetails page
    return redirect(url_for('PersonalDetails_page'))

@app.route('/Register')
def Register_page():
    return render_template('Register.html')

@app.route('/MyPreviousWorkouts')
def MyPreviousWorkouts_page():
    return render_template('MyPreviousWorkouts.html')

# MongoDB connection setup
uri = "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri)
db = cluster.MyWorkoutSchedule
Customers_col = db.Customers
WorkoutDetails_col = db.WorkoutDetails


# Function to retrieve user's full name from the database
def get_user_name(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    full_name = f"{user_data['FirstName']} {user_data['LastName']}" if user_data else None
    return full_name

def get_user_id(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_i_d = f"{user_data['ID']} " if user_data else None
    return user_i_d

def get_user_phone(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_phone = f"{user_data['PhoneNumber']} " if user_data else None
    return user_phone

def get_user_email(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_email = f"{user_data['Email']} " if user_data else None
    return user_email

def get_user_gender(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_gender = f"{user_data['Gender']} " if user_data else None
    return user_gender

def get_user_firstname(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_firstname = f"{user_data['FirstName']} " if user_data else None
    return user_firstname

def get_user_lastname(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_lastname = f"{user_data['LastName']} " if user_data else None
    return user_lastname

def get_user_birthdate(user_id):
    user_data = Customers_col.find_one({'ID': user_id})
    user_birthdate = f"{user_data['Birthdate']} " if user_data else None
    return user_birthdate

WorkoutDetails_col.update_one({'_id': '65fc350446da350f8b7673e7'}, {'$set': {'customer_id': '65fc3622079ef9a650bd3c2c'}})
WorkoutDetails_col.update_one({'_id': '65fc350446da350f8b7673e7'}, {'$set': {'customer_id': '65fc3d6d96ca50557f7f0baa'}})
WorkoutDetails_col.update_one({'_id': '65fc3a0eb763730f8fbf464e'}, {'$set': {'customer_id': '65fc3622079ef9a650bd3c2c'}})
WorkoutDetails_col.update_one({'_id': '65fc3a0eb763730f8fbf464e'}, {'$set': {'customer_id': '65fc3d6d96ca50557f7f0baa'}})
WorkoutDetails_col.update_one({'_id': '65fc3a0eb763730f8fbf464f'}, {'$set': {'customer_id': '65fc3622079ef9a650bd3c2c'}})
WorkoutDetails_col.update_one({'_id': '65fc3a0eb763730f8fbf464f'}, {'$set': {'customer_id': '65fc3d6d96ca50557f7f0baa'}})


# Function to add workout details to the database
@app.route('/add_workout_details', methods=['POST'])
def add_workout_details():
    data = request.json
    existing_workout = WorkoutDetails_col.find_one(data)
    if existing_workout:
        return jsonify({'error': 'Workout details already exist'}), 400
    else:
        WorkoutDetails_col.insert_one(data)
        return jsonify({'success': True, 'message': 'Workout details added successfully'})

if __name__ == '_main_':
    app.run(debug=True)