from flask import Blueprint, render_template

# main_menu blueprint definition
main_menu = Blueprint('main_menu', __name__, static_folder='static', static_url_path='/main_menu', template_folder='templates')

main_menu.route('/PersonalDetails')
def personal_details():
    return render_template('PersonalDetails.html')

main_menu.route('/MyPreviousWorkouts')
def my_previous_workouts():
    return render_template('MyPreviousWorkouts.html')

main_menu.route('/Logout')
def logout():
    return render_template('Login.html')

main_menu.route('/WorkoutSchedule')
def workout_schedule():
    return render_template('WorkoutSchedule.html')

main_menu.route('/MyFutureWorkouts')
def my_future_workouts():
    return render_template('MyFutureWorkouts.html')