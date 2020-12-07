'''
下载FTP文件
日期:2020-12-3
'''

from urllib.parse import quote
import requests
import os
from bs4 import BeautifulSoup

'''
    #下载文件，文件将被下载到运行程序时路径
    baseUrl:下载地址基本URL
    extentialUrl:list,文件相对于url的相对地址，利用findFile方法查询
'''
def down(baseUrl,extentialUrl,pt=os.path.abspath('.')):
    os.chdir(pt)
    for downUrl in extentialUrl:
        # 拆分文件名以及目录名
        res = downUrl.rsplit('/',1)
        #判读路径是否存在，不存在则创建
        if not os.path.exists(os.path.abspath('.')+"\\"+res[0].replace('/','\\')):
            os.makedirs(os.path.abspath('.')+"\\"+res[0].replace('/','\\'))
        #判断本地文件是否存在，不存在则下载
        if not os.path.isfile(downUrl):
            re1 = requests.request(method="GET", url=baseUrl + quote(downUrl))
            with open(downUrl,"wb") as file:
                file.write(re1.content)
        else:
            print(downUrl+"已存在")

'''
    #递归，调用findFile2方法查找所有文件地址
    url:基础目录
    return file_dir：list，全局变量，所有文件的相对于基础url的相对路径

'''
def findFile(baseUrl,url):
    directory = []
    for i in findFile2(baseUrl,url):
        #判断是否带有'/'，带有的是目录
        if '/' in i:
            directory.append(i)
        #不是目录就保存在全局变量中
        else:
            filename.append(i)
            file_dir.append(url+i)
    #如果当前目录下还有目录，则递归查询
    if directory:
        for i in directory:
            findFile(baseUrl,url+i)
    return file_dir

'''
    #传入目录查询当前路径下的目录和文件
    #利用 beautifulsoup 查找所有 td下的a标签，找出href属性值
    purpose:目标目录
    return dir:list,返回所有该目录下的目录及文件
'''
def findFile2(baseUrl,purpose):
    url = baseUrl + purpose
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

if __name__ == '__main__':
    #请求基础url
    baseUrl="http://172.17.43.16:8001/"
    #目标目录,例如：'apps/',下载apps/目录下所有文件，为空时表示查询系统所有文件，
    purpose = ''
    #全局变量
    filename = [] #所有文件名
    file_dir = [] #所有文件相对基础url的路径
    #传入空目录以基础url查找所有文件
    findFile(baseUrl,purpose)
    #所有文件相对路径
    print(file_dir)
    #所有文件名
    print(filename)
    #执行下载
    pt = input("需要下载在当前路径么，如果指定路径请输入具体路径：")
    try:
        if pt is not None:
            if not os.path.exists(pt):
                os.makedirs(pt)
                down(baseUrl, file_dir, pt)
            else:
                down(baseUrl, file_dir, pt)
        else:
            down(baseUrl, file_dir)
    except:
        print("路径有问题")


