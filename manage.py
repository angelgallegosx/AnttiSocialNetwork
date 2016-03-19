from flask.ext.script import Manager
from app import app #imports the app variable from our app package

manager = Manager(app)

@manager.command
def runworker():
    return None

@manager.command
def syncdb():
    return None

if __name__ == "__main__":
    manager.run()
