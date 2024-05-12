# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewPerson.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPersonWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 100, 350, 300))
        self.frame.setMinimumSize(QtCore.QSize(350, 300))
        self.frame.setStyleSheet("#frame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 6, 91, 20))
        self.label.setStyleSheet("font: 12pt \"幼圆\";")
        self.label.setObjectName("label")
        self.pushButtonClose = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonClose.setGeometry(QtCore.QRect(308, 0, 41, 33))
        self.pushButtonClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClose.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgba(255, 0, 0,180);\n"
"    icon-color:white\n"
"}\n"
" \n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgba(255, 0, 0,130);\n"
"    padding-left:3px;\n"
"    padding-top:3px\n"
"}\n"
"#pushButtonClose{\n"
"border-top-right-radius:16px;\n"
"}")
        self.pushButtonClose.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/phres/icon/colse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon)
        self.pushButtonClose.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 9, 16, 16))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/phres/icon/添加增加加入.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("QLabel{\n"
"\n"
"font: 10pt \"幼圆\";\n"
"\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 55);\n"
"    border:none;\n"
"     font: 12pt \"幼圆\";\n"
"    color: rgb(108, 108, 108);\n"
"    border-bottom:1px solid rgb(211, 211, 211);\n"
"}\n"
"QPushButton{\n"
"    border-radius:8px;\n"
"    font: 10pt \"幼圆\";\n"
"    background-color: rgba(0, 170, 255,80);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(15 , 150 , 255);\n"
"}\n"
" \n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid rgb(1 , 84 , 153);\n"
"    background-color: rgba(0, 170, 255,125);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"#frame_4{\n"
"    border-top:1px solid rgb(229, 229, 229)\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEditName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditName.setGeometry(QtCore.QRect(100, 14, 200, 30))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditGender = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditGender.setGeometry(QtCore.QRect(100, 54, 200, 30))
        self.lineEditGender.setObjectName("lineEditGender")
        self.lineEditNumber = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditNumber.setGeometry(QtCore.QRect(100, 94, 200, 30))
        self.lineEditNumber.setObjectName("lineEditNumber")
        self.lineEditEmail = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditEmail.setGeometry(QtCore.QRect(100, 134, 200, 30))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditText = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditText.setGeometry(QtCore.QRect(100, 174, 200, 30))
        self.lineEditText.setObjectName("lineEditText")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 54, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 54, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 54, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 54, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 54, 20))
        self.label_7.setObjectName("label_7")
        self.pushButtonAdd = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonAdd.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 210, 241, 20))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label_9 = QtWidgets.QLabel(self.page1)
        self.label_9.setGeometry(QtCore.QRect(80, 0, 121, 16))
        self.label_9.setStyleSheet("color :rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label_8 = QtWidgets.QLabel(self.page2)
        self.label_8.setGeometry(QtCore.QRect(80, 0, 121, 16))
        self.label_8.setStyleSheet("color :rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page2)
        self.pushButtonAddphoto = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonAddphoto.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.pushButtonAddphoto.setObjectName("pushButtonAddphoto")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "添加联系人"))
        self.lineEditName.setPlaceholderText(_translate("MainWindow", "请输入姓名"))
        self.lineEditGender.setPlaceholderText(_translate("MainWindow", "请输入性别"))
        self.lineEditNumber.setPlaceholderText(_translate("MainWindow", "请输入电话号"))
        self.lineEditEmail.setPlaceholderText(_translate("MainWindow", "请输入邮箱"))
        self.lineEditText.setPlaceholderText(_translate("MainWindow", "请输入备注"))
        self.label_3.setText(_translate("MainWindow", "姓名："))
        self.label_4.setText(_translate("MainWindow", "性别："))
        self.label_5.setText(_translate("MainWindow", "电话："))
        self.label_6.setText(_translate("MainWindow", "邮箱："))
        self.label_7.setText(_translate("MainWindow", "备注："))
        self.pushButtonAdd.setText(_translate("MainWindow", "添加"))
        self.label_9.setText(_translate("MainWindow", "姓名不能为空"))
        self.label_8.setText(_translate("MainWindow", "该联系人已存在"))
        self.pushButtonAddphoto.setText(_translate("MainWindow", "导入名片"))
import res_rc