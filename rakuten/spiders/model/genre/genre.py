import os
import json

class Genre:

    def __init__(self):
        ROOT_PATH = os.path.dirname(__file__)
        f = open(ROOT_PATH + '/genre.json')
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
