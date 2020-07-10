from urllib import request,parse

def urllib_request():
    base_url='http://www.tuling123.com/openapi/api'
    payLoad={
        'key':'your',
        'key2':'你好'
    }
    ur=request.Request(url=base_url)
    ur_response=request.urlopen(ur)
    print(ur)
    '''
    print('\n ur_response: \n\t', ur_response)
    print('\n ur_response_code: \n\t', ur_response.getcode)
    print('\n ur_response_headers: \n\t',ur_response.headers)


    data = parse.urlencode(payLoad).encode('utf-8')
    url_payload = request.Request(url=base_url, data=data)
    url_payload_response = request.urlopen(url_payload)
    print('\n url_payload_response: \n\t', url_payload_response)
    print('\n url_payload_response_getcode: \n\t ', url_payload_response.getcode)
    print('\n url_payload_response_headers: \n\t ', url_payload_response.headers)
    print('\n url_payload_response_msg: \n\t ', url_payload_response.msg)
    print('\n url_payload_response_read: \n\t ', url_payload_response.read)

    '''
urllib_request()


