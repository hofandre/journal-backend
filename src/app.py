from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource
from src.routes.entries import EntriesRoute, EntryRoute
from src.routes.models import entry_model

api = Api()
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

api.init_app(app, version='0.0', title='Proof of Concept Journal Backend',
             description='Back End persistence for the Proof of Concept Journal Application')

api.models[entry_model.name] = entry_model
api.add_resource(EntriesRoute, '/entries')
api.add_resource(EntryRoute, '/entries/<string:entry_id>')