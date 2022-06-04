import openpyxl
import pathlib
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.styles import Font

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
