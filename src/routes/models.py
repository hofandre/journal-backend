from flask_restplus import fields, Model, Api

api = Api()

entry_model = Model('Entry', {
    '_id': fields.Integer,
    'date': fields.DateTime,
    'title': fields.String,
    'content': fields.String
})