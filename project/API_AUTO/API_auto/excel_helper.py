import requests, json, openpyxl

'''
    接口自动化测试框架
    author：zhangmingyu
    date:2020/11/4
        
'''


class excel_helper(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = None

    def open_excel(self):
        try:
            workbook = openpyxl.load_workbook(self.file_path)
        except FileNotFoundError:
            print('文件不存在，将自动创建')
            workbook = openpyxl.Workbook('cases.xlsx')
            workbook.active()
            # workbook = openpyxl.load_workbook(workbook)
        self.workbook = workbook
        return self.workbook

    def open_sheet(self, sheetname):
        workbook = self.open_excel()
        try:
            sheet = workbook[sheetname]
        except:
            sheet = workbook.create_sheet(sheetname)
        return sheet

    def read_excel(self, sheetname):
        sheet = self.open_sheet(sheetname)
        cases = []
        title = []
        rows_data = list(sheet.rows)
        if len(rows_data) <= 1:
            raise Exception()
        for cell in rows_data[0]:
            title.append(cell.value)
        for row in rows_data[1:]:
            case = {}
            for index, cell in enumerate(row):
                case[title[index]] = cell.value
            if case['header'] is None:
                case['header'] = '{}'
            cases.append(case)
        return cases

    def write_excel(self, sheetname, row, colmun, value):
        sheet = self.open_sheet(sheetname)
        self.save()
        cell = sheet.cell(row, colmun)
        cell.value = value
        self.save()
        self.close()

    def save(self):
        self.workbook.save(self.file_path)

    def close(self):
        self.workbook.close()



