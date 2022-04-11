from manager import Manager
from  flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

appFlask = Flask(__name__)

db = SQLAlchemy(appFlask)
migrate = Migrate(appFlask, db)



manager = Manager(appFlask)

@manager.command
def get_users():
    print(get_all_users_json())