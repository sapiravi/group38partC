# from flask import Blueprint
# from flask import render_template, redirect, url_for
#
#
# # HomePage blueprint definition
# HomePage = Blueprint(
#     'HomePage',
#     __name__,
#     static_folder='static',
#     static_url_path='/HomePage',
#     template_folder='templates'
# )
#
#
# # Routes
# @HomePage.route('/HomePage')
# def Home_Page():
#     return render_template('HomePage.html')
#
#

from flask import Blueprint, render_template, request, redirect, url_for, session

# Home blueprint definition
HomePage = Blueprint('HomePage', __name__, static_folder='static', static_url_path='/HomePage', template_folder='templates')


# Routes
@HomePage.route('/HomePage', methods=['GET', 'POST'])
def Home_Page():
    # success_message = session.pop('success_message', None)
    return render_template('HomePage.html')


# success_message=success_message
