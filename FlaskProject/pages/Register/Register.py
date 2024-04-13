# from flask import Blueprint, render_template
#
# # Register blueprint definition
# Register = Blueprint('Register', __name__, static_folder='static', static_url_path='/Register', template_folder='templates')
#
#
# # Routes
# @Register.route('/Register')
#
# def index():
#     return render_template('Register.html')



from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient(
    "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
db = client.MyWorkoutSchedule
customers_collection = db.Customers

# Register blueprint definition
Register = Blueprint('Register', __name__, static_folder='static', static_url_path='/Register',
                     template_folder='templates')


# Routes
@Register.route('/Register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        id = request.form.get('id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        gender = request.form.get('gender')
        birthdate = request.form.get('birthdate')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        # Check if passwords match
        if password != password_confirmation:
            error_message = "Passwords do not match. Please try again."
            return render_template('Register.html', error_message=error_message)

        errors = []
        if len(id) != 9 or not id.isdigit():
            errors.append("ID should be a 9-digit number.")
        if len(first_name) < 2 or not first_name.isalpha():
            errors.append("First name should contain at least 2 letters.")
        if len(last_name) < 2 or not last_name.isalpha():
            errors.append("Last name should contain at least 2 letters.")
        if len(phone) != 10 or not phone.isdigit():
            errors.append("Phone number should be a 10-digit number.")
        if '@' not in email or '.' not in email:
            errors.append("Email should be in the correct format.")
        if len(password) < 6:
            errors.append("Password should be at least 6 characters long.")

        if errors:
            return render_template('Register.html', errors=errors)

        # If validation passes, add user to the database

        # Check if user already exists
        existing_user = customers_collection.find_one({'ID': id})
        if existing_user:
            return render_template('Register.html', errors=["User with this ID already exists."])

        # Create a document to insert into the database
        customer_data = {
            'ID': id,
            'FirstName': first_name,
            'LastName': last_name,
            'PhoneNumber': phone,
            'Email': email,
            'Gender': gender,
            'Birthdate': birthdate,
            'Password': password
        }

        # Insert the document into the Customers collection
        customers_collection.insert_one(customer_data)
        # Store success message in session
        session['success_message'] = "Registration successful!"

        # Redirect to home page
        return redirect(url_for('Home_Page'))

    # If it's a GET request or if passwords don't match, render the registration page
    return render_template('Register.html')

