
from App.controllers.user import create_user
from App.controllers.signUp import *
from flask import Blueprint, render_template, jsonify, request, send_from_directory,flash,url_for,redirect
from flask_jwt import jwt_required

signup_views = Blueprint('user_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template


@signup_views.route('/signup', methods=['POST'])
def singUp():
  form = SignUp() 
  if form.validate_on_submit():
    data = request.form 
    create_user(data['username'],data['password'])
    flash('Account Created!')
    return redirect(url_for('index'))
