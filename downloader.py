import requests
import re
import os
from model import auth
from model import genre
from time import sleep

def download_genre():
    base_url = 'https://app.rakuten.co.jp/services/api/BooksGenre/Search/20121128?format=json&booksGenreId=001'
    param = make_get_param()
    url = base_url + param
    response = requests.get(url)
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/genre/genre.json')
    with open(file_name, 'w') as f:
        f.write(response.text)

def download(elements="page,largeImageUrl,salesDate,isbn", formatVersion=2, pages=100, sort="-releaseDate"):
    base_url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?'
    param = make_get_param(formatVersion=formatVersion, sort=sort, elements=elements)
    base_url = base_url + param
    for page in range(1, pages+1):
        str_page = "&page=" + str(page)
        url = base_url + str_page
        response = requests.get(url)
        file_name = "model/data/item/json/item{}.json".format(str(page))
        with open(file_name, 'w') as f:
            f.write(response.text)
        sleep(1.5)

def make_get_param(formatVersion="", sort="", elements=""):
    str_applicationId = "&applicationId=" + auth.Auth().get_applicationId()
    str_booksGenreId = "&booksGenreId=" + genre.Genre().get_booksGenreId()
    str_sort = "&sort=" + sort
    str_formatVersion = "&formatVersion=" + str(formatVersion)
    str_elements = "&elements=" + elements
    param = str_applicationId + str_booksGenreId + str_sort + str_formatVersion + str_elements
    return param

if __name__ == "__main__":
    download()
