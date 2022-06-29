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

        font = Font(underline='single', color='FF0000FF')

        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = pyApp.Ui_MainWindow()
        ui.setupUi(MainWindow)

        def getFileName() -> str:
            FileName = QFileDialog.getOpenFileName(
                MainWindow, "选择文件", './', '*.xlsx')  # 选择目录，返回选中的路径
            ui.lineEdit.setText(FileName[0])
            return FileName[0]

        def getSheetName(path: str) -> None:
            global wb
            wb = openpyxl.load_workbook(Path(path))
            wbSheets = [i.title for i in wb]
            row = 0
            for i in wbSheets:
                ui.tableWidget.setItem(row, 0, QTableWidgetItem(i))
                row += 1
            return None

        def openFileCMD() -> None:
            path = getFileName()
            getSheetName(path)
            return None

        def commitFileCMD():
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
            wb.save()
            wb.close()

        ui.openFilesButton.clicked.connect(openFileCMD)

        MainWindow.show()
        sys.exit(app.exec())

    finally:
        pass
