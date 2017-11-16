import os
import json
import datetime as dt
from base import Base
from PIL import Image
from io import BytesIO
import requests
from time import sleep
import re


class Item():

    def __init__(self, dic):
        self.isbn = dic["isbn"]
        self.date = self._process_date(dic["salesDate"])
        if "largeImageUrl" in dic.keys():
            self.image_url = dic["largeImageUrl"].split("?")[0]


    def _process_date(self, str_date):
        # print(str_date)
        if "頃" in str_date:
            if "日" in str_date:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月%d日頃")
            else:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月頃")
        elif "旬" in str_date:
            if "中" in str_date:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月中旬")
            elif "上" in str_date:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月上旬")
            elif "下" in str_date:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月下旬")
        elif "日" in str_date:
            date_time = dt.datetime.strptime(str_date,"%Y年%m月%d日")
        elif not "日" in str_date:
            if "月" in str_date:
                date_time = dt.datetime.strptime(str_date,"%Y年%m月")
            else:
                date_time = dt.datetime.strptime(str_date,"%Y年")
        date = dt.date(date_time.year, date_time.month, date_time.day)
        return date
