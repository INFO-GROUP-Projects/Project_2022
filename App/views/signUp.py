from App.controllers.user import create_user
from App.controllers.signUp import create_form
from flask import Blueprint, render_template, jsonify, request, send_from_directory,flash,url_for,redirect
from flask_jwt import jwt_required

from App.models.user import User

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup')
def signup():
  form = create_form() 
  return render_template('signup.html', form = form) # pass form object to template


@signup_views.route('/signup', methods=['POST'])
def signUpAction():
  form = create_form()
  if form.validate_on_submit():
    data = request.form 
    create_user(data['username'],data['password'])
    flash('Account Created!')
    return redirect(url_for('index'))
