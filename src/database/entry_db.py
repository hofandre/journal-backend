import os
import pymongo
from src.logger.logger import get_logger

_log = get_logger(__name__)

_mongo = pymongo.MongoClient(os.environ.get('MONGO_URI_POC')).simple

def get_entries():
    lst = _mongo.entries.find({'title': {'$exists': True}})
    return list(lst)

def get_entry_id():
    return  _mongo.entries.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                           {'$inc': {'count': 1}},
                                           return_document=pymongo.ReturnDocument.AFTER)['count']

def add_entry(entry):
    ''' Adds a new entry in the database '''
    entry['_id'] = get_entry_id()
    _mongo.entries.insert_one(entry)
    return entry

def edit_entry(entry, entry_id):
    ''' Edits a entry in the database '''
    query = {'_id': int(entry_id)}
    try:
        new_entry = _mongo.entries.replace_one(query, entry)
    except Exception as err:
        _log.exception(err)
    return new_entry

if __name__ == '__main__':
    print(_mongo)
    _mongo.entries.drop()
    _mongo.entries.insert_one({'_id': 'UNIQUE_COUNT', 'count': 0})