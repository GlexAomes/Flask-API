import math

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin

from task_delegator import *
from db_controller import *

### --- CONFIGS AND MISC

errors = {
    'PageNotFound': {
        'message':'Looks like the endpoint you are looking for does not exist, please double check your queries.',
        'status': 404,
    },
}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app, catch_all_404s=True, errors=errors) # after CORS, catch_all_404s not working

### --- CLASSES AND ENDPOINTS

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello, World!'}, 200
    
    def post(self):
        req_json = request.get_json()
        return {'sent':req_json}, 201

class Sqrt(Resource):
    def get(self, num):
        return {'result':math.sqrt(num)}, 200

class Fib(Resource):
    def get(self, num):
        if num > 950:
            return {
            'message':'I like your curious exploration but, there is a recursion depth limit. Look it up. And no, I am not increasing it, keep it below 951.',
        }, 500

        task = Tasker()
        task.fib(num)
        return {
            'result':task.RESPONSE,
            'time':task.TIME,
        }, 200

### --- Add Resources

api.add_resource(HelloWorld, '/')
api.add_resource(Sqrt, '/sqrt/<int:num>')
api.add_resource(Fib, '/fib/<int:num>')

### --- Database Controller

dbc = DB_Controller(app)
dbc.create_user('Glex', 'glexaomes@gmail.com')
dbc.query_all_users()

### --- Headless Entry Point

if __name__ == '__main__':
    app.run(debug=True)