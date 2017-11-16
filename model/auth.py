import json
import os
from .base import Base

class Auth(Base):

    def __init__(self):
        super().__init__()
        f = open(os.path.join(self.DATA_ROOT, 'auth/auth.json'))
        self.data = json.load(f)

    def get_applicationId(self):
        return self.data["applicationId"]
