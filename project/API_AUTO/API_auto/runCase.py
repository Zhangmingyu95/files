import requests


class runCase(object):
    def __init__(self, cases):
        self.cases = cases

    def runLogin(self, login_info):
        response = requests.request(method=self.cases[-1]['method'].upper(), url=self.cases[-1]['url'],
                                    params=login_info,
                                    headers=eval(self.cases[-1]['header']))
        return response.cookies

    def runCases(self):
        for case in self.cases:
            if case['login_info']:
                case['cookie'] = self.runLogin(case['login_info'])
                response = requests.request(method=case['method'].upper(), url=case['url'], params=eval(case['param']),
                                            headers=eval(case['header']), cookies=case['cookie']).json()
            else:
                response = requests.request(method=case['method'].upper(), url=case['url'], params=eval(case['param']),
                                            headers=eval(case['header'])).json()
            expected = eval(case['expected'])
            result = 'pass'
            for i in expected:
                if response[i] == expected[i]:
                    result = 'pass'
                else:
                    result = 'failed'
            case['result'] = result
