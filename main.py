from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = pyApp.Ui_MainWindow()
    ui.setupUi(MainWindow)

    def docmd():
        FileName = QFileDialog.getOpenFileName(
            MainWindow, "选择文件")  # 选择目录，返回选中的路径
        ui.lineEdit.setText(FileName[0])
        return FileName


    ui.openFilesButton.clicked.connect(docmd)

    MainWindow.show()
    sys.exit(app.exec())
