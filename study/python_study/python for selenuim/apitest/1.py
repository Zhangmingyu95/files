__author__ = 'mingyu.zhang'
import requests

'''httpGet = requests.get('http://httpbin.org/get',data={'key':'value'})
#print(httpGet.text)

def transfer_dict_parameter():
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }

    transfer_dict_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print("transfer_dict_parameter_url: ", transfer_dict_parameter_result.url)
    #print("transfer_dict_parameter_text: ", transfer_dict_parameter_result.text)


transfer_dict_parameter()


def transfer_multipart_encoded_file():
    interface_url = 'https://httpbin.org/post'
    files = {
        # 显示设置文件名、文件类型和请求头
        'file': ('re', open('re', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})
    }

    transfer_multipart_encoded_file_result = requests.post(url=interface_url, files=files)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.url)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.cookies)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.headers)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.text)
    #print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.content)

    transfer_multipart_encoded_file_result_content=transfer_multipart_encoded_file_result.raw
    transfer_multipart_encoded_file_result_content_read=transfer_multipart_encoded_file_result_content.read(10)
    print(transfer_multipart_encoded_file_result_content,transfer_multipart_encoded_file_result_content_read)



transfer_multipart_encoded_file()

'''

url='https://httpbin.org/get'

def operaror_cookies():
    r=requests.get(url,5)
    print('r.cookies:',r.cookies)

    jar=requests.cookies.RequsetsCookieJar()
    jar.set('tasty_cookie','yum',domin='httpbin.org',path='/cookies')
    jar.set('gross_cookie','blech',domin='httpbin.org',path='/elsewhere')
    r2=requests.get(url=url,cookies=jar)
    print('r2.text',r2.text)

operaror_cookies()