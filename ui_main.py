# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gerador.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 637)
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.title_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame {\n"
"background-color: rgb(38,38,38);\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #fff;\n"
"}\n"
"\n"
"QLabel{\n"
"border: 1.4px solid white;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_left = QPushButton(self.frame)
        self.btn_left.setObjectName(u"btn_left")
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_left.setFont(font1)
        self.btn_left.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_left, 0, Qt.AlignLeft)

        self.btn_right = QPushButton(self.frame)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setFont(font1)
        self.btn_right.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame)

        self.lbl_img = QLabel(self.main_frame)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setMinimumSize(QSize(384, 384))
        self.lbl_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_img)


        self.verticalLayout.addWidget(self.main_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMinimumSize(QSize(0, 0))
        self.main_container.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(42,42,42);\n"
"color: rgb(245,245,245);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255,255,255);\n"
"border: solid 0px;\n"
"font: 75 16px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0,170,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_description = QLineEdit(self.main_container)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.txt_description.setFont(font2)
        self.txt_description.setAutoFillBackground(False)
        self.txt_description.setStyleSheet(u"")
        self.txt_description.setAlignment(Qt.AlignCenter)
        self.txt_description.setDragEnabled(False)
        self.txt_description.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.txt_description)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_name_file = QLineEdit(self.main_container)
        self.txt_name_file.setObjectName(u"txt_name_file")
        self.txt_name_file.setFont(font)
        self.txt_name_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_name_file)

        self.btn_generate = QPushButton(self.main_container)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.btn_generate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">GERADOR DE IMAGENS IA</span></p></body></html>", None))
        self.btn_left.setText(QCoreApplication.translate("MainWindow", u"<---", None))
        self.btn_right.setText(QCoreApplication.translate("MainWindow", u"--->", None))
        self.lbl_img.setText("")
        self.txt_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o texto em ingl\u00eas para gerar a imagem.", None))
        self.txt_name_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"GERAR", None))
    # retranslateUi

