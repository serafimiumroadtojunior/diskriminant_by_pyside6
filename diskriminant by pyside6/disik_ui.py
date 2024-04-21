# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rework_app.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(399, 582)
        icon = QIcon()
        icon.addFile(u"../icons/dicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Comic Sans MS\";\n"
"    font-size: 13px;\n"
"    color: white;\n"
"    background-color: rgb(62, 75, 75);\n"
"	 width:bold;\n"
"    padding-left:3px;\n"
"}\n"
"\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"	font-family: \"Comic Sans MS\";\n"
"    color:white;\n"
"    font-size: 16px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"	width:bold;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"    font-family: \"Comic Sans MS\";\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    opacity: 0.2;\n"
"    transition: all 0.5s;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"} ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.USER_CHOICE_FRAME = QFrame(self.centralwidget)
        self.USER_CHOICE_FRAME.setObjectName(u"USER_CHOICE_FRAME")
        self.USER_CHOICE_FRAME.setGeometry(QRect(19, 19, 151, 211))
        self.USER_CHOICE_FRAME.setFrameShape(QFrame.StyledPanel)
        self.USER_CHOICE_FRAME.setFrameShadow(QFrame.Raised)
        self.A_LABEL = QLabel(self.USER_CHOICE_FRAME)
        self.A_LABEL.setObjectName(u"A_LABEL")
        self.A_LABEL.setGeometry(QRect(20, 30, 31, 21))
        self.B_LABEL = QLabel(self.USER_CHOICE_FRAME)
        self.B_LABEL.setObjectName(u"B_LABEL")
        self.B_LABEL.setGeometry(QRect(20, 90, 31, 21))
        self.C_LABEL = QLabel(self.USER_CHOICE_FRAME)
        self.C_LABEL.setObjectName(u"C_LABEL")
        self.C_LABEL.setGeometry(QRect(20, 150, 31, 21))
        self.USER_TEXT_A = QLineEdit(self.USER_CHOICE_FRAME)
        self.USER_TEXT_A.setObjectName(u"USER_TEXT_A")
        self.USER_TEXT_A.setGeometry(QRect(60, 30, 61, 21))
        self.USER_TEXT_B = QLineEdit(self.USER_CHOICE_FRAME)
        self.USER_TEXT_B.setObjectName(u"USER_TEXT_B")
        self.USER_TEXT_B.setGeometry(QRect(60, 90, 61, 21))
        self.USER_TEXT_C = QLineEdit(self.USER_CHOICE_FRAME)
        self.USER_TEXT_C.setObjectName(u"USER_TEXT_C")
        self.USER_TEXT_C.setGeometry(QRect(60, 150, 61, 20))
        self.FORMULS_FRAME = QFrame(self.centralwidget)
        self.FORMULS_FRAME.setObjectName(u"FORMULS_FRAME")
        self.FORMULS_FRAME.setGeometry(QRect(190, 20, 191, 211))
        self.FORMULS_FRAME.setFrameShape(QFrame.StyledPanel)
        self.FORMULS_FRAME.setFrameShadow(QFrame.Raised)
        self.HELLO_LABEL = QLabel(self.FORMULS_FRAME)
        self.HELLO_LABEL.setObjectName(u"HELLO_LABEL")
        self.HELLO_LABEL.setGeometry(QRect(46, 13, 91, 21))
        self.FORMUL_1 = QLabel(self.FORMULS_FRAME)
        self.FORMUL_1.setObjectName(u"FORMUL_1")
        self.FORMUL_1.setGeometry(QRect(10, 50, 161, 21))
        self.FORMUL_2 = QLabel(self.FORMULS_FRAME)
        self.FORMUL_2.setObjectName(u"FORMUL_2")
        self.FORMUL_2.setGeometry(QRect(10, 90, 161, 21))
        self.FORMUL_3 = QLabel(self.FORMULS_FRAME)
        self.FORMUL_3.setObjectName(u"FORMUL_3")
        self.FORMUL_3.setGeometry(QRect(10, 130, 161, 21))
        self.FORMUL_4 = QLabel(self.FORMULS_FRAME)
        self.FORMUL_4.setObjectName(u"FORMUL_4")
        self.FORMUL_4.setGeometry(QRect(10, 170, 161, 21))
        self.RESULT_FRAME = QFrame(self.centralwidget)
        self.RESULT_FRAME.setObjectName(u"RESULT_FRAME")
        self.RESULT_FRAME.setGeometry(QRect(20, 250, 361, 321))
        self.RESULT_FRAME.setFrameShape(QFrame.StyledPanel)
        self.RESULT_FRAME.setFrameShadow(QFrame.Raised)
        self.RESULT_BUTTON = QPushButton(self.RESULT_FRAME)
        self.RESULT_BUTTON.setObjectName(u"RESULT_BUTTON")
        self.RESULT_BUTTON.setGeometry(QRect(204, 272, 141, 31))
        self.RESULT_LABEL_1 = QLabel(self.RESULT_FRAME)
        self.RESULT_LABEL_1.setObjectName(u"RESULT_LABEL1")
        self.RESULT_LABEL_1.setGeometry(QRect(20, 20, 311, 31))
        self.RESULT_LABEL_2 = QLabel(self.RESULT_FRAME)
        self.RESULT_LABEL_2.setObjectName(u"RESULT_LABEL_2")
        self.RESULT_LABEL_2.setGeometry(QRect(20, 80, 311, 31))
        self.RESULT_LABEL_3 = QLabel(self.RESULT_FRAME)
        self.RESULT_LABEL_3.setObjectName(u"RESULT_LABEL_3")
        self.RESULT_LABEL_3.setGeometry(QRect(20, 140, 311, 31))
        self.RESULT_LABEL_4 = QLabel(self.RESULT_FRAME)
        self.RESULT_LABEL_4.setObjectName(u"RESULT_LABEL_4")
        self.RESULT_LABEL_4.setGeometry(QRect(20, 200, 311, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Diskriminant For School", None))
        self.A_LABEL.setText(QCoreApplication.translate("MainWindow", u" a  = ", None))
        self.B_LABEL.setText(QCoreApplication.translate("MainWindow", u"b  =", None))
        self.C_LABEL.setText(QCoreApplication.translate("MainWindow", u"c  =", None))
        self.HELLO_LABEL.setText(QCoreApplication.translate("MainWindow", u"Formul's", None))
        self.FORMUL_1.setText(QCoreApplication.translate("MainWindow", u"ax^2 + bx + c = 0", None))
        self.FORMUL_2.setText(QCoreApplication.translate("MainWindow", u"D = b^2 - 4ac", None))
        self.FORMUL_3.setText(QCoreApplication.translate("MainWindow", u"x1 = (-b - \u221aD) / 2a", None))
        self.FORMUL_4.setText(QCoreApplication.translate("MainWindow", u"x2 = (-b + \u221aD) / 2a", None))
        self.RESULT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.RESULT_LABEL_1.setText("")
        self.RESULT_LABEL_2.setText("")
        self.RESULT_LABEL_3.setText("")
        self.RESULT_LABEL_4.setText("")
    # retranslateUi