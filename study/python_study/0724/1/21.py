__author__ = 'mingyu.zhang'
import re

def is_valid_email(adr):
    if re.match(r'^\w([\w\.]*)@(\w*)\.com',adr):
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):

    return None