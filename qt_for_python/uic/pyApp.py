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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import rec_rc
import resours_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"#LeftBar {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#RightBar {\n"
"	background-color: rgb(40, 44,52);\n"
"}\n"
"\n"
"#RightTopBar{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#RightUndBar{\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#LeftTopImag{\n"
"border-image:url(:/Image/images/images/100678278.png);\n"
"}\n"
"\n"
"#toggleLeftBox{\n"
"background-image: url(:/Icon/images/icons/icon_settings.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#toggleLeftBox:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleLeftBox:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
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
        self.LeftBar.setMinimumSize(QSize(60, 0))
        self.LeftBar.setMaximumSize(QSize(60, 16777215))
        self.LeftBar.setFrameShape(QFrame.StyledPanel)
        self.LeftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.LeftBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftTopImag = QFrame(self.LeftBar)
        self.LeftTopImag.setObjectName(u"LeftTopImag")
        self.LeftTopImag.setMinimumSize(QSize(60, 45))
        self.LeftTopImag.setMaximumSize(QSize(60, 50))
        self.LeftTopImag.setFrameShape(QFrame.StyledPanel)
        self.LeftTopImag.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.LeftTopImag)

        self.LeftMidMenuUp = QFrame(self.LeftBar)
        self.LeftMidMenuUp.setObjectName(u"LeftMidMenuUp")
        self.LeftMidMenuUp.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenuUp.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.LeftMidMenuUp)

        self.LeftMidMenuDwn = QFrame(self.LeftBar)
        self.LeftMidMenuDwn.setObjectName(u"LeftMidMenuDwn")
        self.LeftMidMenuDwn.setFrameShape(QFrame.StyledPanel)
        self.LeftMidMenuDwn.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.LeftMidMenuDwn)

        self.LeftUndCmd = QFrame(self.LeftBar)
        self.LeftUndCmd.setObjectName(u"LeftUndCmd")
        self.LeftUndCmd.setMaximumSize(QSize(16777215, 45))
        self.LeftUndCmd.setFrameShape(QFrame.StyledPanel)
        self.LeftUndCmd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftUndCmd)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.LeftUndCmd)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setStyleSheet(u"")
        self.toggleLeftBox.setAutoDefault(False)
        self.toggleLeftBox.setFlat(False)

        self.verticalLayout_3.addWidget(self.toggleLeftBox)


        self.verticalLayout.addWidget(self.LeftUndCmd)


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
        self.RightTopBar.setMinimumSize(QSize(0, 50))
        self.RightTopBar.setMaximumSize(QSize(16777215, 50))
        self.RightTopBar.setFrameShape(QFrame.StyledPanel)
        self.RightTopBar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.RightTopBar)

        self.RightMidCont = QFrame(self.RightBar)
        self.RightMidCont.setObjectName(u"RightMidCont")
        self.RightMidCont.setFrameShape(QFrame.StyledPanel)
        self.RightMidCont.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.RightMidCont)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.RightMidCont)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.RightMidCont)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.RightMidCont)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.RightMidCont)

        self.RightUndBar = QFrame(self.RightBar)
        self.RightUndBar.setObjectName(u"RightUndBar")
        self.RightUndBar.setMaximumSize(QSize(16777215, 15))
        self.RightUndBar.setFrameShape(QFrame.StyledPanel)
        self.RightUndBar.setFrameShadow(QFrame.Raised)

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
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

