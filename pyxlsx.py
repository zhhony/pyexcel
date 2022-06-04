import openpyxl
import pathlib
import argparse
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.styles import Font
from win32com import client
from typing import *

path = pathlib.Path("C:\\Users\\zhhon\\Desktop\\2022年项目费用记录表【高倩】.xlsx")
wb = openpyxl.load_workbook(path)
wsWorkSheetList = wb.sheetnames[2:]
wsList = wb['目录']

font = Font(underline='single', color='FF0000FF')

rownum = 1
colnum = 1
wsList.cell(row=rownum, column=colnum, value='目 录')
for i in wsWorkSheetList:
    rownum += 1
    wsList.cell(row=rownum, column=colnum, value=i).font = font
    wsList.cell(row=rownum, column=colnum).hyperlink = Hyperlink(
        ref='', location='\'%s\'!A1' % i, tooltip=None, display='%s' % i, id=None)

    wb[i]['A3'].font = font
    wb[i]['A3'].hyperlink = Hyperlink(
        ref='', location='\'目录\'!A1', tooltip=None, display='目录', id=None)


wb.save(path)
wb.close()


# xls转xlsx
def TypeTransform(filePath: pathlib.Path) -> pathlib.Path:
    excel = client.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(filePath)
    wb.SaveAs(str(filePath) + "x", FileFormat=51)
    wb.Close()
    excel.Application.Quit()
    return pathlib.Path(str(filePath) + "x")


if __name__ == '__main__':
    class ExcelTypeError(TypeError):
        pass

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='excel文件路径')
    try:
        arge = parser.parse_args()
        filePath = pathlib.Path(arge.path)
        if filePath.match('*.xlsx'):
            pass
        elif filePath.match('*.xls'):
            TypeTransform(filePath)
            pass
        else:
            raise ExcelTypeError
    except ExcelTypeError:
        print('不是合规的excel文件，只支持xlsx、xls文件')
    finally:
        pass
