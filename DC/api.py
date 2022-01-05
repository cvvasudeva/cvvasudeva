from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class product(Resource):
    def get(self):
        return{
            'product': ['Ice cream',
                        'Chocolate',
                        'Fruit']
        }
api.add_resource(Product, '/')

if __name__=='__mail__':
    app.run(host='0.0.0.0', port=80, debug=True)