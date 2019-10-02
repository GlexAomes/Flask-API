from models.models import *
from flask_sqlalchemy import SQLAlchemy

class DB_Controller:
    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.user_model = user_model(self.db)

    def reset(self):
        self.db.drop_all()
        self.db.create_all()

    def update(self, model):
        self.db.session.add(model)
        self.db.session.commit()

    def create_user(self, name, email):
        #new_user = create_user_model(self.db, name, email)
        new_user = self.user_model(username=name, email=email)
        self.reset()
        self.update(new_user)

        print(f"Created user: {new_user}")

    def query_all_users(self):
        print(f" > QUERY ALL USERS:\n------------------\n{self.user_model.query.all()}\n------------------")