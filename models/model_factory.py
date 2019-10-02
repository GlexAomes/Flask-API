def user_model(db):
    class User(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username
    
    return User


class ModelFactory:
    factories = {}

    def __init__(self, db):
        self.db = db

    @staticmethod
    def addFactory(self, id, ModelFactory):
        ModelFactory.factories[id] = ModelFactory
    
    @staticmethod
    def createModel(self, id):
        if not id in ModelFactory.factories.keys():
            #ModelFactory.factories[id] = eval(id + '.Factory()')
        #return ModelFactory.factories[id].create()
            ModelFactory.factories[id] = eval(f'_metaclass')
        return ModelFactory.factories[id](self.db)

class Model(object): pass

### --- DB MODELS -> Can move into separate modules as per catagorization needs


class User(Model):
    def __repr__(self):
        return "Yeet"

    class Factory:
        def create(self): return Circle()

def user_metaclass(db):
    class User(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
                return '<User %r>' % self.username
    
    return User

