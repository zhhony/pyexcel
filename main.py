from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from typing import *
import modules.dirpage as dirpage
import modules.homepage as homepage
import modules.appui as appui
import sys

# 主程序
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = appui.Ui_MainWindow()

        dirPg = dirpage.DirPage(MainWindow, ui)  # 定义dirPage窗口类，方便调用目录窗口的方法
        homePg = homepage.HomePage(MainWindow, ui)  # 定义dirHome窗口类，方便调用Home窗口的方法

        ui.setupUi(MainWindow)
        ui.stackedWidget.setCurrentIndex(0)  # 将'Home'页设置成stackedwidget的预展示页面
        MainWindow.show()

        # 主界面按钮监控
        ui.btn_home.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(0))  # 监控'Home'页的click动作
        ui.btn_dir.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(1))  # 监控'建立目录'页的click动作
        ui.btn_2.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(2))  # 监控'功能2'页的click动作
        ui.btn_3.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(3))  # 监控'功能3'页的click动作
        ui.btn_4.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(4))  # 监控'功能4'页的click动作
        ui.btn_5.clicked.connect(
            lambda: ui.stackedWidget.setCurrentIndex(5))  # 监控'功能5'页的click动作

        # page 0 'Home'界面按钮监控
        ui.versionlab.setText(homePg._APP_VERSION)  # 获取版本号

        # page 1 '建立目录'界面按钮监控
        ui.openFilesButton.clicked.connect(
            dirPg.cmdOpenExcelFile)  # 监控openFilesButton的click动作
        ui.commitButton.clicked.connect(
            dirPg.cmdCommitFile)  # 监控commitButton的click动作

        # page 2 界面按钮监控
        # page 3 界面按钮监控
        # page 4 界面按钮监控
        # page 5 界面按钮监控
    finally:
        sys.exit(app.exec())
