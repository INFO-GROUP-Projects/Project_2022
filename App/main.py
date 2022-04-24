import os
import json
from flask import Flask, jsonify,flash,redirect, render_template, url_for,request 
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
from App.controllers.auth import login_user, logout_user
from App.controllers.user import validate_User

login_manager = LoginManager()

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from App.database import init_db, get_migrate

from App.controllers import (
    setup_jwt,
    word,
    create_user,
    init_words
)

from App.models import (
    login,
    User,
    SignUp,
    LogIn
)

from App.views import (
    user_views,
    api_views,
    word_views
)

views = [
    user_views,
    api_views,
    word_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    app.debug = True
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app, views)
    init_db(app)
    setup_jwt(app)
    login_manager.init_app(app)
    app.app_context().push()
    return app


app = create_app()

@app.route('/api/users', methods = ['GET'])
def getAllUsers():
    u = User.query.all()
    if u is None:
        return []
    uList = [us.toDict() for us in u]
    return jsonify(uList)

@app.route('/login')
def getLoginPage():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return redirect(url_for('word_views.returnWordPage'))
    form = LogIn()
    return render_template('login.html',form =form)

@app.route('/login', methods = {'POST'})
def loginAction():
    form = LogIn()
    if form.validate_on_submit():
        data = request.form
        user = validate_User(data['username'], data['password'])
        if user is not None:  
            flash('Login successful')
            login_user(user,True)
            return redirect(url_for('word_views.returnWordPage'))
    else:
        print(form.errors)
        flash('CSRF-Token Error')
        return redirect(url_for('loginAction'))
    flash('Invalid credentials')
    return redirect(url_for('loginAction'))


@app.route('/logout')
def logoutActions():
    logout_user()
    flash('Logged Out')
    return redirect(url_for('api_views.get_api_docs'))

@app.route('/signup')
def getSignUpPage():
    if current_user.is_authenticated:
        flash('You cannot create an account while logged in please log out first')
        return redirect(url_for('word_views.returnWordPage'))
    form = SignUp()
    return render_template('signup.html',form = form)

@app.route('/signup', methods=['POST'])
def signUpAction():
    form = SignUp()
    if form.validate_on_submit():
        data = request.form 
        msg = create_user(data['username'],data['password'],data['email'])
        if msg == "Error":
            flash('Error in creating account')
            return redirect(url_for('getSignUpPage'))
        else:
            flash('Account Created!')
    else:
        print(form.errors)
        flash('Form Error')
        return redirect(url_for('getSignUpPage'))
    return redirect(url_for('loginAction'))


#@app.route('/api/init')
#def instance_words():
   # init_words()

migrate = get_migrate(app)


