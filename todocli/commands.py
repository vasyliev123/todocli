import pandas as pd
import pprint
import logging
import json
from todocli import utils
from todocli.storage import read_from_storage, write_to_storage
from todocli.task import Task
def add(task, due_date=None):

    task = Task(task, due_date)
    df = read_from_storage()    
    l = len(df)
    df[str(l)] = task.to_dict()
    df = json.dumps(df)
    write_to_storage(df)
    

def list():
    df = read_from_storage()
    utils.print_dictionary(df)

def remove(pos):
    df =read_from_storage()
    df.pop(pos)
    df = utils.rearange_items(df)
    df = json.dumps(df)
    write_to_storage(df)
    print(f"Task {pos} is removed")
