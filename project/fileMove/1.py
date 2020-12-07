import requests
import os
from bs4 import BeautifulSoup

def findFile(url):
    directory = []
    for i in findFile2(url):
        if '/' in i:
            directory.append(i)
        else:
            filename.append(i)
            file_dir.append(url+i)
    if directory:
        for i in directory:
            findFile(url+i)
    return file_dir

def findFile2(purpose):
    purpose = purpose
    url = "http://172.17.43.16:8001/" + purpose
    res = requests.get(url).content
    with open('test.html', 'wb') as f:
        f.write(res)
    soup = BeautifulSoup(res, 'lxml')
    s = soup.select('td a')
    dir = []
    for i in s:
        if i.get("href") is not None:
            dir.append(i.get("href"))
    return dir

filename = []
file_dir = []
findFile('video/')
print(file_dir)