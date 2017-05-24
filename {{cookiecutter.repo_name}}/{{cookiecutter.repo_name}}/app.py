from flask import Flask, request
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib

from {{cookiecutter.repo_name}}.pipeline import predict_k

model = joblib.load("./model.pkl")

app = Flask(__name__)
api = Api(app, version='1.0', title='{{cookiecutter.project_name}}',
          description='{{cookiecutter.project_short_description}}')
ns = api.namespace('{{cookiecutter.repo_name}}', description='{{cookiecutter.project_short_description}}')


@ns.route('/predict')
class Predictor(Resource):
    def post(self):
        data = request.json
        #TODO Implement
        raise NotImplementedError


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
