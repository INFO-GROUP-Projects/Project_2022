#write code to create and actually manipulate word page here
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
import random

from App.controllers import (
    createWords, 
    getWord,
)

word_views = Blueprint('word_views', __name__, template_folder='../templates')

@api_views.route('/WordPage')
def returnWordPage():  
  return render_template('wordPage.html')  