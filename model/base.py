import os
import json


class Base():

    def __init__(self):
        self.APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.DATA_ROOT = os.path.join(self.APP_ROOT, 'model/data')
