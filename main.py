from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyApp
import sys
import openpyxl
from pathlib import Path
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.styles import Font
from typing import *
import threading

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = pyApp.Ui_MainWindow()
        ui.setupUi(MainWindow)

        # 获取Excel路径
        def getExcelFilePath() -> str:
            excelFile = QFileDialog.getOpenFileName(
                MainWindow, "选择文件", './', '*.xlsx')  # 选择目录，返回选中的路径
            excelFilePath = excelFile[0]
            return excelFilePath

        # 获取Excel的sheet清单
        def getExcelSheetName(path: str) -> list:
            wb = openpyxl.load_workbook(Path(path))
            wbSheetsList = [i.title for i in wb]
            wb.close()
            return wbSheetsList

        # 定义tableWidget控件的排版方法，此控件9*3
        def gridTableWidget(list: list) -> None:

            def ListIter(list):
                for i in list:
                    yield i

            listIter = ListIter(list)

            itemColumn = 0
            while itemColumn < 3:
                itemRow = 0
                while itemRow < 9:
                    try:
                        ui.tableWidget.setItem(
                            itemRow, itemColumn, QTableWidgetItem(next(listIter)))
                        itemRow += 1
                    except StopIteration:
                        return None
                itemColumn += 1

        # 定义openFile按钮的动作

        def cmdOpenExcelFile() -> None:
            excelFilePath = getExcelFilePath()
            wbSheetsList = getExcelSheetName(excelFilePath)

            ui.lineEdit.setText(excelFilePath)  # 将路径写入lineEdit

            # 将sheet名字写入tableWidget
            gridTableWidget(wbSheetsList)

        # 定义commitFileCMD按钮的动作
        def cmdCommitFile() -> None:
            font = Font(underline='single', color='FF0000FF')

            excelFilePath = ui.lineEdit.text()
            wb = openpyxl.load_workbook(Path(excelFilePath))

            if '目录' not in [i.title for i in wb]:
                wb.create_sheet('目录', 0)
            else:
                wb['目录'].delete_cols(1, 2)
            wsList = wb['目录']

            rownum, colnum = 1, 1
            wsWorkSheetList = [i.title for i in wb if i.title != '目录']
            wsList.cell(row=rownum, column=colnum, value='目 录')
            for i in wsWorkSheetList:
                rownum += 1
                wsList.cell(row=rownum, column=colnum, value=i).font = font
                wsList.cell(row=rownum, column=colnum).hyperlink = Hyperlink(
                    ref='', location='\'%s\'!A1' % i, tooltip=None, display='%s' % i, id=None)

                wb[i]['A3'].font = font
                wb[i]['A3'].hyperlink = Hyperlink(
                    ref='', location='\'目录\'!A1', tooltip=None, display='目录', id=None)
            wb.save(excelFilePath)
            wb.close()

        MainWindow.show()

        ui.openFilesButton.clicked.connect(cmdOpenExcelFile)
        ui.commitButton.clicked.connect(cmdCommitFile)

        sys.exit(app.exec())

    finally:
        pass
