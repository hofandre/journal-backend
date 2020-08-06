import unittest
import unittest.mock as mock
import src.database.entry_db
from src.logger.logger import get_logger

_log = get_logger(__name__)

class EntryDBTestSuite(unittest.TestCase):
    ''' Basic Tests for the database'''
    @mock.patch.object(src.database.entry_db, '_mongo')
    def test_get_entries(self, mock_db):
        ''' Tests getting all entries in the database'''
        mock_db.entries.find.return_value = ['TEST VALUE']
        ret = src.database.entry_db.get_entries()
        self.assertEqual(ret, ['TEST VALUE'])
        mock_db.entries.find.assert_called_once()
    @mock.patch.object(src.database.entry_db, '_mongo')
    @mock.patch.object(src.database.entry_db, 'get_entry_id')
    def test_add_entry(self, mock_id, mock_db):
        ''' Tests adding an entry'''
        mock_db.entries.insert_one.return_value = 'TEST'
        mock_id.return_value = -10
        entry = {'test': 'VALUE', '_id': -1}
        ret = src.database.entry_db.add_entry(entry)
        self.assertEqual(ret['_id'], -10)
        mock_db.entries.insert_one.assert_called_with({'test': 'VALUE', '_id': -10})
        mock_db.entries.insert_one.assert_called_once()
        mock_id.assert_called_once()
    @mock.patch.object(src.database.entry_db, '_mongo')
    def test_edit_entry(self, mock_db):
        ''' Tests editing an entry '''
        entry = {'test': 'VALUE', '_id': -1}
        mock_db.entries.replace_one.return_value = entry
        entry_id = -2
        ret = src.database.entry_db.edit_entry(entry, entry_id)
        mock_db.entries.replace_one.assert_called_with({'_id': -2}, entry)
        self.assertEqual(ret, entry)


if __name__ == '__main__':
    unittest.main()