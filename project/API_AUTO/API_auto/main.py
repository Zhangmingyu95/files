# This is a sample Python script.
import requests, openpyxl
import excel_helper, runCase

if __name__ == '__main__':
    excel_path = input('请输入用例文件名或路径：')
    login_sheetName = input('请输入登录用例所在表单名')
    cases_sheetName = input('请输入测试用例所在表单名')

    cases = excel_helper.excel_helper(excel_path).read_excel(cases_sheetName)

    try:
        login_case = excel_helper.excel_helper(excel_path).read_excel(login_sheetName)
    except Exception:
        print("未填写登录接口")
    else:
        cases.append(login_case)

    runCase.runCase(cases).runCases()

    result_excel = 'result.xlsx'
    sheet_name = 'result'
    excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=1, colmun=1, value='caseID')
    excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=1, colmun=2, value='title')
    excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=1, colmun=3, value='result')
    index = 2
    for case in cases:
        excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=index, colmun=1, value=case['caseID'])
        excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=index, colmun=2, value=case['title'])
        excel_helper.excel_helper(result_excel).write_excel(sheet_name, row=index, colmun=3, value=case['result'])
        index = index + 1
    print('运行完成')