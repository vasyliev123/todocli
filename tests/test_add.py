import json
import todocli.commands
import todocli.storage
from unittest.mock import patch


def test_add():
    # create a temporary file with some initial data
    test_data = {'0': 'task 1', '1': 'task 2'}
    test_file = 'test.json'
    with open(test_file, 'w') as f:
        json.dump(test_data, f)

    # mock the method that writes JSON to the file
    with patch('todocli.storage.write_to_storage') as mock_write:
        # call the add function with a new task
        todocli.commands.add('task 3')

        # verify that the mock write method was called with the expected arguments
        expected = {'0': 'task 1', '1': 'task 2', '2': 'task 3'}
        mock_write.assert_called_once_with(json.dumps(expected))

    # cleanup the test file
    test_file.unlink()