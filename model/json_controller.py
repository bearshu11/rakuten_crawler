import os
import json
import datetime as dt
from base import Base
from PIL import Image
from io import BytesIO
from item import Item
import requests
from time import sleep


class JsonController(Base):

    def __init__(self):
        super().__init__()
        self.data = []
        for i in range(1,101):
            child_path = 'item/json/item{}.json'.format(i)
            f = open(os.path.join(self.DATA_ROOT, child_path))
            tmp = json.load(f)
            self.data.extend(tmp["Items"])

    def get_items(self):
        items = []
        for dic in self.data:
            item = Item(dic)
            items.append(item)
        return items


if __name__ == "__main__":
    json_controller = JsonController()
    items = json_controller.get_items()
    for item in items:
        response = requests.get(item.image_url)
        image = Image.open(BytesIO(response.content))
        path = 'data/item/images/{0}_{1}.png'.format(item.date, id(item))
        image.save(path, 'png')
        sleep(1)
