from flask import render_template
from flask import Blueprint
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/MyWorkoutSchedule?retryWrites=true&w=majority")
db = client.MyWorkoutSchedule
WorkoutDetails_col = db.WorkoutDetails

# Login blueprint definition
MyPreviousWorkouts = Blueprint(
    'MyPreviousWorkouts',
    __name__,
    static_folder='static',
    static_url_path='/MyPreviousWorkouts',
    template_folder='templates'
)


# Routes
@MyPreviousWorkouts.route('/MyPreviousWorkouts/<customer_id>')
def MyPreviousWorkouts_page(customer_id):
    # Retrieve workouts associated with the customer ID
    workouts = WorkoutDetails_col.find({'customer_id': customer_id})

    # Pass the retrieved workouts to the template
    return render_template('MyPreviousWorkouts.html', workouts=workouts)