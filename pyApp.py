# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyApp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import rec_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 602)
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.StyleSheet.setFont(font)
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
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.StyleSheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label = QLabel(self.LeftMidMenuTop)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"	color: rgb(100, 100, 100);\n"
"	font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout_5.addWidget(self.label)


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
        self.toggleButton = QPushButton(self.LeftMidMenuHill)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setStyleSheet(u"background-image: url(:/Icon/images/icons/icon_menu.png);")

        self.verticalLayout_5.addWidget(self.toggleButton)


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
        self.btn_home = QPushButton(self.LeftMidMenu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-home.png);")

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.LeftMidMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-gamepad.png);")

        self.verticalLayout_6.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.LeftMidMenu)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-file.png);")

        self.verticalLayout_6.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.LeftMidMenu)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-save.png);")

        self.verticalLayout_6.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.LeftMidMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setStyleSheet(u"background-image: url(:/Icon/images/icons/cil-x.png);")

        self.verticalLayout_6.addWidget(self.btn_exit)


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
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.toggleLeftBox.setFont(font1)
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
        self.RightTopBar = QFrame(self.RightBar)
        self.RightTopBar.setObjectName(u"RightTopBar")
        self.RightTopBar.setMinimumSize(QSize(0, 25))
        self.RightTopBar.setMaximumSize(QSize(16777215, 25))
        self.RightTopBar.setFrameShape(QFrame.StyledPanel)
        self.RightTopBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.RightTopBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftButtons = QFrame(self.RightTopBar)
        self.LeftButtons.setObjectName(u"LeftButtons")
        self.LeftButtons.setMinimumSize(QSize(300, 25))
        self.LeftButtons.setMaximumSize(QSize(16777215, 25))
        self.LeftButtons.setFrameShape(QFrame.StyledPanel)
        self.LeftButtons.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.LeftButtons)

        self.rightButtons = QFrame(self.RightTopBar)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(100, 25))
        self.rightButtons.setMaximumSize(QSize(100, 16777215))
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(15, 15))
        self.minimizeAppBtn.setMaximumSize(QSize(15, 15))
        icon = QIcon()
        icon.addFile(u":/Icon/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(15, 15))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(15, 15))
        icon1 = QIcon()
        icon1.addFile(u":/Icon/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(15, 15))
        self.closeAppBtn.setMaximumSize(QSize(15, 15))
        icon2 = QIcon()
        icon2.addFile(u":/Icon/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.RightTopBar)

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
        self.DirBuid = QWidget()
        self.DirBuid.setObjectName(u"DirBuid")
        self.verticalLayout_7 = QVBoxLayout(self.DirBuid)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.DirBuidTopTop = QFrame(self.DirBuid)
        self.DirBuidTopTop.setObjectName(u"DirBuidTopTop")
        self.DirBuidTopTop.setMaximumSize(QSize(16777215, 50))
        self.DirBuidTopTop.setFrameShape(QFrame.StyledPanel)
        self.DirBuidTopTop.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.DirBuidTopTop)

        self.DirBuidTop = QFrame(self.DirBuid)
        self.DirBuidTop.setObjectName(u"DirBuidTop")
        self.DirBuidTop.setMaximumSize(QSize(16777215, 110))
        self.DirBuidTop.setStyleSheet(u"QPushButton {\n"
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
        self.DirBuidTop.setFrameShape(QFrame.StyledPanel)
        self.DirBuidTop.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.DirBuidTop)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.lineEdit = QLineEdit(self.DirBuidTop)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"#DirBuid .QLineEdit {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    color: rgb(100, 100, 100);\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/Icon/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFilesButton.setIcon(icon3)

        self.gridLayout.addWidget(self.openFilesButton, 1, 2, 1, 1)

        self.labelBoxBlenderInstalation = QLabel(self.DirBuidTop)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")

        self.gridLayout.addWidget(self.labelBoxBlenderInstalation, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.DirBuidTop)

        self.DirBuidDwn = QFrame(self.DirBuid)
        self.DirBuidDwn.setObjectName(u"DirBuidDwn")
        self.DirBuidDwn.setFrameShape(QFrame.StyledPanel)
        self.DirBuidDwn.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.DirBuidDwn)

        self.stackedWidget.addWidget(self.DirBuid)
        self.whatever = QWidget()
        self.whatever.setObjectName(u"whatever")
        self.stackedWidget.addWidget(self.whatever)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.RightMidCont)

        self.RightUndBar = QFrame(self.RightBar)
        self.RightUndBar.setObjectName(u"RightUndBar")
        self.RightUndBar.setMinimumSize(QSize(0, 15))
        self.RightUndBar.setMaximumSize(QSize(16777215, 15))
        self.RightUndBar.setFrameShape(QFrame.StyledPanel)
        self.RightUndBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.RightUndBar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.RightUndBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"	color: rgb(100, 100, 100);\n"
"	font: 8pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.RightUndBar)


        self.horizontalLayout_2.addWidget(self.RightBar)


        self.horizontalLayout.addWidget(self.App)

        MainWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(MainWindow)

        self.toggleLeftBox.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uff1a\u5927\u5c3e\u5df4\u9c7c", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u76ee\u5f55", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd2", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd3", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd4", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd5", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u901a\u8fc7\u6253\u5f00\u6309\u94ae\u9009\u62e9\u6587\u4ef6", None))
        self.labelVersion_4.setText("")
        self.openFilesButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Product by zhhony@126.com", None))
    # retranslateUi

