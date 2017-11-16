import os
import json
from .base import Base

class Genre(Base):

    def __init__(self):
        super().__init__()
        f = open(os.path.join(self.DATA_ROOT, 'genre/genre.json'))
        self.data = json.load(f)

    def get_booksGenreId(self, booksGenreName="写真集・タレント"):
        booksGenreId = "-1"
        for child in self.data["children"]:
            if child["child"]["booksGenreName"] == booksGenreName:
                booksGenreId = child["child"]["booksGenreId"]
                break
        if booksGenreId == "-1":
            print("not exist")
        return booksGenreId
