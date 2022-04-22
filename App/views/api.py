from flask import Blueprint, redirect, render_template, request, send_from_directory,url_for
from flask_login import current_user

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    if current_user.is_authenticated:
        return redirect(url_for('word_views.returnWordPage'))
    return render_template('index.html')

