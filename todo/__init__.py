import os

from flask import Flask

def create_app():       # Se crea para hacer testing
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'mikey', # Es importante cambiar ya que se puede atacar facilmente la app
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE')
    ) # Nos sirve para hacer sesiones llamada "cookie"

    from . import db

    db.init_app(app)
    
    from . import auth
    from . import todo
    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'Hola como tas?'
    
    return app