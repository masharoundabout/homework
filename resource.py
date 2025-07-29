import os

def picture_path(val):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, 'tests/resources', val)