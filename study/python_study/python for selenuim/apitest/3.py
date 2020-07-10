__author__ = 'mingyu.zhang'
import requests
import random
import hashlib
import urllib
import json

class BaiduTranslate(object):
    def __init__(self,word):
        self.q=word
        self.fromLang='en'
        self.toLang='zh'
        self.baidu_translate='https://api.fanyi.baidu.com'
        self.translate_api_url='/api/trans/vip/translate'

        self.appid='xxxxx'
        self.secretKey='xxxxx'

        self.salt=random.randint(32768,65536)
        self.sign=self.appid+self.q+str(self.salt)+self.secretKey
        m1=hashlib.md5()
        m1.update(self.sign.encode('utf-8'))
        self.sign = m1.hexdigest()
        self.my_url = self.translate_api_url + '?appid=' + self.appid + '&q=' + urllib.request.quote(self.q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(self.salt) + '&sign=' + self.sign

    def en_translate_zh(self):
        re = requests.request('post', self.baidu_translate + self.my_url)
        print('\n\t re.text', re.text)
        re_json = json.loads(re.text)
        print('\n\t re_json', re_json)

if __name__ == '__main__':
    bt = BaiduTranslate('test')
    bt.en_translate_zh()