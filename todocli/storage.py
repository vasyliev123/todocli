import json
import os
DB_FILE = os.path.join(os.path.dirname(__file__), 'database.json')
def read_from_storage() -> dict:
    with open(DB_FILE, 'r') as f:
        contents = f.read()
        if contents == '':
            df = {}
        else:
            df = json.loads(contents)
        return df
def write_to_storage(df):
    with open(DB_FILE, 'w') as f:
        f.write(df)
