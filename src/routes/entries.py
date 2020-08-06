import flask
from flask_restplus import Resource, Api
import src.database.entry_db as db
from src.routes.models import entry_model
from src.logger.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/entries')
class EntriesRoute(Resource):
    @api.response(200, 'Success', entry_model)
    def get(self):
        ''' Retrieves all journal entries in the database'''
        _log.debug('In the get fn')
        try:
            entry_list = db.get_entries()
        except:
            return 'Database Error', 500
        else:
            _log.debug(entry_list)
            return entry_list, 200
    @api.doc(body=entry_model)
    @api.response(201, 'Entry Created', entry_model)
    @api.response(400, 'Invalid Request')
    @api.response(500, 'Database Error')
    def post(self):
        ''' Adds an entry to the database '''
        try:
            entry = db.add_entry(flask.request.get_json(force=True))
        except:
            return 'Database Error', 500
        else:
            return entry, 201

@api.route('/entries/<string:entry_id>')
class EntryRoute(Resource):
    @api.response(200, 'Success', entry_model)
    def put(self, entry_id):
        ''' Replaces an entry at a given id with the one in the request body'''
        ''' Adds an entry to the database '''
        _log.debug(entry_id)
        try:
            entry = db.edit_entry(flask.request.get_json(force=True), entry_id )
            _log.debug(entry)
        except:
            return 'Database Error', 500
        else:
            return flask.request.get_json(force=True), 200