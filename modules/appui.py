# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import modules.rec_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 602)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(9)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.StyleSheet.setFont(font1)
        self.StyleSheet.setStyleSheet(u"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"#LeftBar {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#RightBar {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"#RightTopBar {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#RightUndBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"\n"
"#LeftTopImag {\n"
"    border-image: url(:/Image/images/images/100678278.png);\n"
"}\n"
"\n"
"#LeftBar .QPushButton {\n"
"    background-image: url(:/Icon/images/icons/icon_settings.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"\n"
"#LeftBar .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"#LeftBar .QPushButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255"
                        ", 255, 255);\n"
"}\n"
"\n"
"\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#rightButtons .QPushButton:hover {\n"
"    background-color: rgb(44, 49, 57);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#RightMidCont .QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"#RightMidCont .QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"#RightMidCont .QPushButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    ma"
                        "rgin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: n"
                        "one;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: n"
                        "one;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.App = QFrame(self.StyleSheet)
        self.App.setObjectName(u"App")
        self.App.setFrameShape(QFrame.StyledPanel)
        self.App.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.App)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftBar = QFrame(self.App)
        self.LeftBar.setObjectName(u"LeftBar")
        self.LeftBar.setMinimumSize(QSize(170, 0))
        self.LeftBar.setMaximumSize(QSize(60, 16777215))
        self.LeftBar.setFrameShape(QFrame.StyledPanel)
        self.LeftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.LeftBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMidMenuTop = QFrame(self.LeftBar)
        self.LeftMidMenuTop.setObjectName(u"LeftMidMenuTop")
        self.LeftMidMenuTop.setMinimumSize(QSize(0, 25))
        self.LeftMidMenuTop.setMaximumSize(QSize(16777215, 25))
        self.LeftMidMenuTop.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenuTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.LeftMidMenuTop)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.LeftMidMenuTop)

        self.LeftMidMenuHill = QFrame(self.LeftBar)
        self.LeftMidMenuHill.setObjectName(u"LeftMidMenuHill")
        self.LeftMidMenuHill.setMaximumSize(QSize(16777215, 45))
        self.LeftMidMenuHill.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenuHill.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.LeftMidMenuHill)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.LeftMidMenuHill)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_home.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-home.png);")

        self.verticalLayout_5.addWidget(self.btn_home)


        self.verticalLayout.addWidget(self.LeftMidMenuHill)

        self.LeftMidMenu = QFrame(self.LeftBar)
        self.LeftMidMenu.setObjectName(u"LeftMidMenu")
        self.LeftMidMenu.setMaximumSize(QSize(16777215, 230))
        self.LeftMidMenu.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.LeftMidMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_dir = QPushButton(self.LeftMidMenu)
        self.btn_dir.setObjectName(u"btn_dir")
        self.btn_dir.setMinimumSize(QSize(0, 45))
        self.btn_dir.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-menu.png);")

        self.verticalLayout_6.addWidget(self.btn_dir)

        self.btn_2 = QPushButton(self.LeftMidMenu)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(0, 45))
        self.btn_2.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-gamepad.png);")

        self.verticalLayout_6.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.LeftMidMenu)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(0, 45))
        self.btn_3.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-file.png);")

        self.verticalLayout_6.addWidget(self.btn_3)

        self.btn_4 = QPushButton(self.LeftMidMenu)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(0, 45))
        self.btn_4.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-save.png);")

        self.verticalLayout_6.addWidget(self.btn_4)

        self.btn_5 = QPushButton(self.LeftMidMenu)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(0, 45))
        self.btn_5.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-x.png);")

        self.verticalLayout_6.addWidget(self.btn_5)


        self.verticalLayout.addWidget(self.LeftMidMenu)

        self.frame_3 = QFrame(self.LeftBar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.LeftMidMenuDwn = QFrame(self.LeftBar)
        self.LeftMidMenuDwn.setObjectName(u"LeftMidMenuDwn")
        self.LeftMidMenuDwn.setMaximumSize(QSize(16777215, 45))
        self.LeftMidMenuDwn.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenuDwn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftMidMenuDwn)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.LeftMidMenuDwn)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.toggleLeftBox.setFont(font2)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setStyleSheet(u"")
        self.toggleLeftBox.setAutoDefault(False)
        self.toggleLeftBox.setFlat(False)

        self.verticalLayout_3.addWidget(self.toggleLeftBox)


        self.verticalLayout.addWidget(self.LeftMidMenuDwn)


        self.horizontalLayout_2.addWidget(self.LeftBar)

        self.RightBar = QFrame(self.App)
        self.RightBar.setObjectName(u"RightBar")
        self.RightBar.setFrameShape(QFrame.StyledPanel)
        self.RightBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.RightBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RightMidCont = QFrame(self.RightBar)
        self.RightMidCont.setObjectName(u"RightMidCont")
        self.RightMidCont.setStyleSheet(u"border-top: 0px solid rgb(40, 44, 52);\n"
"background-color: rgb(40, 44, 52);")
        self.RightMidCont.setFrameShape(QFrame.StyledPanel)
        self.RightMidCont.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.RightMidCont)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.RightMidCont)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.Home)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.HomeIcon = QFrame(self.Home)
        self.HomeIcon.setObjectName(u"HomeIcon")
        self.HomeIcon.setMaximumSize(QSize(16777215, 16777215))
        self.HomeIcon.setStyleSheet(u"background-image: url(:/Image/images/images/100678278.png);\n"
"background-position: center bottom;\n"
"background-repeat: no-repeat;")
        self.HomeIcon.setFrameShape(QFrame.StyledPanel)
        self.HomeIcon.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.HomeIcon)

        self.HomeMid = QFrame(self.Home)
        self.HomeMid.setObjectName(u"HomeMid")
        self.HomeMid.setMaximumSize(QSize(16777215, 45))
        self.HomeMid.setStyleSheet(u"QLabel {\n"
"color: rgb(170, 170,170);\n"
"font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.HomeMid.setFrameShape(QFrame.StyledPanel)
        self.HomeMid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.HomeMid)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.HomeMid)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(170, 170,170);\n"
"font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label)

        self.label_3 = QLabel(self.HomeMid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)


        self.verticalLayout_10.addWidget(self.HomeMid)

        self.HomeText = QFrame(self.Home)
        self.HomeText.setObjectName(u"HomeText")
        self.HomeText.setMaximumSize(QSize(16777215, 16777215))
        self.HomeText.setFrameShape(QFrame.StyledPanel)
        self.HomeText.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.HomeText)

        self.stackedWidget.addWidget(self.Home)
        self.DirBuid = QWidget()
        self.DirBuid.setObjectName(u"DirBuid")
        self.verticalLayout_7 = QVBoxLayout(self.DirBuid)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.DirBuidTopTop = QFrame(self.DirBuid)
        self.DirBuidTopTop.setObjectName(u"DirBuidTopTop")
        self.DirBuidTopTop.setMinimumSize(QSize(0, 50))
        self.DirBuidTopTop.setMaximumSize(QSize(16777215, 50))
        self.DirBuidTopTop.setFrameShape(QFrame.StyledPanel)
        self.DirBuidTopTop.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.DirBuidTopTop)

        self.DirBuidTop = QFrame(self.DirBuid)
        self.DirBuidTop.setObjectName(u"DirBuidTop")
        self.DirBuidTop.setMaximumSize(QSize(16777215, 110))
        self.DirBuidTop.setStyleSheet(u"")
        self.DirBuidTop.setFrameShape(QFrame.StyledPanel)
        self.DirBuidTop.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.DirBuidTop)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.lineEdit = QLineEdit(self.DirBuidTop)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.lineEdit.setFont(font3)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"#DirBuid .QLineEdit {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    color: rgb(170, 170, 170);\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"#DirBuid .QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"#DirBuid .QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.labelVersion_4 = QLabel(self.DirBuidTop)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"\n"
"font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.labelVersion_4, 2, 0, 1, 3)

        self.openFilesButton = QPushButton(self.DirBuidTop)
        self.openFilesButton.setObjectName(u"openFilesButton")
        self.openFilesButton.setMinimumSize(QSize(100, 30))
        self.openFilesButton.setMaximumSize(QSize(150, 30))
        self.openFilesButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icon/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFilesButton.setIcon(icon)

        self.gridLayout.addWidget(self.openFilesButton, 1, 2, 1, 1)

        self.labelBoxBlenderInstalation = QLabel(self.DirBuidTop)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")

        self.gridLayout.addWidget(self.labelBoxBlenderInstalation, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.DirBuidTop)

        self.DirBuidDwn = QFrame(self.DirBuid)
        self.DirBuidDwn.setObjectName(u"DirBuidDwn")
        self.DirBuidDwn.setFrameShape(QFrame.StyledPanel)
        self.DirBuidDwn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.DirBuidDwn)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.DirBuidDwn)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 330))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(33, 37, 43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.frame_5 = QFrame(self.DirBuidDwn)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_5)

        self.DirBuidCMD = QFrame(self.DirBuidDwn)
        self.DirBuidCMD.setObjectName(u"DirBuidCMD")
        self.DirBuidCMD.setMinimumSize(QSize(0, 50))
        self.DirBuidCMD.setMaximumSize(QSize(16777215, 100))
        self.DirBuidCMD.setFrameShape(QFrame.StyledPanel)
        self.DirBuidCMD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.DirBuidCMD)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.DirBuidCMD)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.DirBuidCMD)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(120, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.commitButton = QPushButton(self.frame_4)
        self.commitButton.setObjectName(u"commitButton")
        self.commitButton.setMinimumSize(QSize(100, 30))
        self.commitButton.setMaximumSize(QSize(150, 30))
        self.commitButton.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/Icon/images/icons/cil-input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commitButton.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.commitButton)


        self.horizontalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.DirBuidCMD)


        self.verticalLayout_7.addWidget(self.DirBuidDwn)

        self.stackedWidget.addWidget(self.DirBuid)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_14 = QVBoxLayout(self.page_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_15 = QVBoxLayout(self.page_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.RightMidCont)

        self.RightUndBar = QFrame(self.RightBar)
        self.RightUndBar.setObjectName(u"RightUndBar")
        self.RightUndBar.setMinimumSize(QSize(0, 15))
        self.RightUndBar.setMaximumSize(QSize(16777215, 15))
        self.RightUndBar.setStyleSheet(u"QLabel{\n"
"	color: rgb(100, 100, 100);\n"
"	font: 8pt \"Segoe UI\";\n"
"}")
        self.RightUndBar.setFrameShape(QFrame.StyledPanel)
        self.RightUndBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.RightUndBar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.productlab = QLabel(self.RightUndBar)
        self.productlab.setObjectName(u"productlab")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setKerning(False)
        self.productlab.setFont(font5)
        self.productlab.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.productlab)

        self.versionlab = QLabel(self.RightUndBar)
        self.versionlab.setObjectName(u"versionlab")
        self.versionlab.setFont(font5)
        self.versionlab.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.versionlab)


        self.verticalLayout_2.addWidget(self.RightUndBar)


        self.horizontalLayout_2.addWidget(self.RightBar)


        self.verticalLayout_13.addWidget(self.App)

        MainWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(MainWindow)

        self.toggleLeftBox.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Excel\u4f34\u4fa3", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_dir.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u76ee\u5f55", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd3", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd5", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u54b3\u54b3\uff0c\u611f\u89c9\u8fd9\u91cc\u5e94\u8be5\u9700\u8981\u4e00\u6bb5\u8bdd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4ebaGit\u4e3b\u9875\uff1ahttps://github.com/zhhony", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u901a\u8fc7\u6253\u5f00\u6309\u94ae\u9009\u62e9\u6587\u4ef6", None))
        self.labelVersion_4.setText("")
        self.openFilesButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"sheet", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.commitButton.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u76ee\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u767d\u9875\u9762", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u767d\u9875\u9762", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u767d\u9875\u9762", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u767d\u9875\u9762", None))
        self.productlab.setText(QCoreApplication.translate("MainWindow", u" Product by zhhony@126.com", None))
        self.versionlab.setText("")
    # retranslateUi

