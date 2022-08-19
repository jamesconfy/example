from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
import dotenv

dotenv.load_dotenv(".env")

migrate = Migrate()
db = SQLAlchemy()

appEnv = os.environ.get("SERVER")
appConfig = ""
if appEnv == "development":
    from config import DevConfig
    appConfig = DevConfig
else:
    from config import ProdConfig
    appConfig = ProdConfig

def create_app(appConfig=appConfig):
    exampleApp = Flask('example')
    exampleApp.config['APPLICATION_ROOT']  = '/v1'
    exampleApp.config.from_object(appConfig)
    migrate.init_app(app=exampleApp, db=db, render_as_batch=True, compare_type=True)
    db.init_app(exampleApp)

    with exampleApp.app_context():
        from example import routes
        db.create_all()

    return exampleApp