from flask import Flask
from flask_restful import Resource, Api, reqparse

###Initialise API
app = Flask(__name__)
api = Api(app)

###Data for API
DATA = {"App Name": "Health", "Version": "1.0.0"}

### Create (get) method and URL, 
class ApiData(Resource):
  def get(self):
    return DATA
api.add_resource(ApiData, '/health/')

if __name__ == "__main__":
  app.run(debug=True)





