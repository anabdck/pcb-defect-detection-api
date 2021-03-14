from flask import Flask
from flask_script import Manager, Server

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
manager.add_command("runserver", Server())
server = Server(host="0.0.0.0", port=9000)

from app.controllers import default
