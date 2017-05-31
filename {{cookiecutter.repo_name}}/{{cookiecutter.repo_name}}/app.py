import logging

from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
from healthcheck import HealthCheck, EnvironmentDump
from sklearn.externals import joblib
from {{cookiecutter.repo_name}}.data import DEFAULT_DATA_PATH
from

{{cookiecutter.repo_name}}
import __version__

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)
cors = CORS(app)
api = Api(app, version='__version__', title='{{cookiecutter.project_name}}',
          description='{{cookiecutter.project_short_description}}')
ns = api.namespace('{{cookiecutter.repo_name}}', description='{{cookiecutter.project_name}}')
request_model = api.model('Input data', {
    'data': fields.String(description='Data to predict', required=True)
})
response_model = api.model('Result', {
    'result': fields.String(description="Result"),
})


health = HealthCheck(app, "/healthcheck")
envdump = EnvironmentDump(app, "/environment")


@ns.route('/predict')
class Predictor(Resource):
    @api.expect(request_model, validate=False)
    @api.response(200, 'Success', response_model)
    def post(self):
        data = request.json
        # TODO Implement
        raise NotImplementedError


logging.info("Reading the model from {}".format(DEFAULT_DATA_PATH))
model = joblib.load(DEFAULT_DATA_PATH)

if __name__ == "__main__":
    logging.info("Starting the server")
    app.run(host='0.0.0.0', debug=True, port=8080)
