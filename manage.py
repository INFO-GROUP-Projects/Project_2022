from manager import Manager

manager = Manager()

@manager.command
def get_users():
    print(get_all_users_json())