# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/4th.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 772)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.icons_only = QtWidgets.QWidget(self.centralwidget)
        self.icons_only.setMaximumSize(QtCore.QSize(95, 16777215))
        self.icons_only.setStyleSheet("QWidget{\n"
"background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white\n"
"\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"        background-color: rgb(99, 99, 99);\n"
"\n"
"    font-weight:bold;\n"
"}")
        self.icons_only.setObjectName("icons_only")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icons_only)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.icons_only)
        self.label.setMinimumSize(QtCore.QSize(80, 80))
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/eye-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.dashboard_btn1 = QtWidgets.QPushButton(self.icons_only)
        self.dashboard_btn1.setMinimumSize(QtCore.QSize(60, 60))
        self.dashboard_btn1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_btn1.setIcon(icon)
        self.dashboard_btn1.setIconSize(QtCore.QSize(40, 40))
        self.dashboard_btn1.setCheckable(True)
        self.dashboard_btn1.setChecked(True)
        self.dashboard_btn1.setAutoExclusive(True)
        self.dashboard_btn1.setObjectName("dashboard_btn1")
        self.verticalLayout_2.addWidget(self.dashboard_btn1)
        self.search_btn1 = QtWidgets.QPushButton(self.icons_only)
        self.search_btn1.setMinimumSize(QtCore.QSize(60, 60))
        self.search_btn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn1.setIcon(icon1)
        self.search_btn1.setIconSize(QtCore.QSize(40, 40))
        self.search_btn1.setCheckable(True)
        self.search_btn1.setAutoExclusive(True)
        self.search_btn1.setObjectName("search_btn1")
        self.verticalLayout_2.addWidget(self.search_btn1)
        self.notification_1 = QtWidgets.QPushButton(self.icons_only)
        self.notification_1.setMinimumSize(QtCore.QSize(60, 60))
        self.notification_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/notifications.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification_1.setIcon(icon2)
        self.notification_1.setIconSize(QtCore.QSize(40, 40))
        self.notification_1.setCheckable(True)
        self.notification_1.setAutoExclusive(True)
        self.notification_1.setObjectName("notification_1")
        self.verticalLayout_2.addWidget(self.notification_1)
        self.settings_1 = QtWidgets.QPushButton(self.icons_only)
        self.settings_1.setMinimumSize(QtCore.QSize(60, 60))
        self.settings_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_1.setIcon(icon3)
        self.settings_1.setIconSize(QtCore.QSize(30, 30))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)
        self.settings_1.setObjectName("settings_1")
        self.verticalLayout_2.addWidget(self.settings_1)
        self.signout_1 = QtWidgets.QPushButton(self.icons_only)
        self.signout_1.setMinimumSize(QtCore.QSize(60, 60))
        self.signout_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/log_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signout_1.setIcon(icon4)
        self.signout_1.setIconSize(QtCore.QSize(40, 40))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)
        self.signout_1.setObjectName("signout_1")
        self.verticalLayout_2.addWidget(self.signout_1)
        self.gridLayout.addWidget(self.icons_only, 0, 1, 1, 1)
        self.main_meun = QtWidgets.QWidget(self.centralwidget)
        self.main_meun.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.main_meun.setObjectName("main_meun")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_meun)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header = QtWidgets.QWidget(self.main_meun)
        self.header.setEnabled(True)
        self.header.setMinimumSize(QtCore.QSize(0, 100))
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setStyleSheet("QWidget{\n"
"background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white\n"
"\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background_color: #F5FAFE;\n"
"    color: 1F95EF;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color:white;\n"
"}")
        self.header.setObjectName("header")
        self.pushButton_7 = QtWidgets.QPushButton(self.header)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.header)
        self.lineEdit.setGeometry(QtCore.QRect(380, 20, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.header)
        self.widget = QtWidgets.QWidget(self.main_meun)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.gridLayout.addWidget(self.main_meun, 0, 4, 1, 1)
        self.icons_names = QtWidgets.QWidget(self.centralwidget)
        self.icons_names.setMaximumSize(QtCore.QSize(200, 16777215))
        self.icons_names.setStyleSheet("QWidget{\n"
"    border-color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white\n"
"\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"        background-color: rgb(99, 99, 99);\n"
"\n"
"    font-weight:bold;\n"
"}")
        self.icons_names.setHidden(True)
        self.icons_names.setObjectName("icons_names")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.icons_names)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.icons_names)
        self.label_2.setMinimumSize(QtCore.QSize(80, 80))
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/eye-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dashboard_btn2 = QtWidgets.QPushButton(self.icons_names)
        self.dashboard_btn2.setMinimumSize(QtCore.QSize(60, 60))
        self.dashboard_btn2.setIcon(icon)
        self.dashboard_btn2.setIconSize(QtCore.QSize(40, 40))
        self.dashboard_btn2.setCheckable(True)
        self.dashboard_btn2.setChecked(True)
        self.dashboard_btn2.setAutoExclusive(True)
        self.dashboard_btn2.setObjectName("dashboard_btn2")
        self.verticalLayout.addWidget(self.dashboard_btn2)
        self.search_btn2 = QtWidgets.QPushButton(self.icons_names)
        self.search_btn2.setMinimumSize(QtCore.QSize(60, 60))
        self.search_btn2.setIcon(icon1)
        self.search_btn2.setIconSize(QtCore.QSize(40, 40))
        self.search_btn2.setCheckable(True)
        self.search_btn2.setAutoExclusive(True)
        self.search_btn2.setObjectName("search_btn2")
        self.verticalLayout.addWidget(self.search_btn2)
        self.notification_2 = QtWidgets.QPushButton(self.icons_names)
        self.notification_2.setMinimumSize(QtCore.QSize(60, 60))
        self.notification_2.setIcon(icon2)
        self.notification_2.setIconSize(QtCore.QSize(40, 40))
        self.notification_2.setCheckable(True)
        self.notification_2.setAutoExclusive(True)
        self.notification_2.setObjectName("notification_2")
        self.verticalLayout.addWidget(self.notification_2)
        self.settings_2 = QtWidgets.QPushButton(self.icons_names)
        self.settings_2.setMinimumSize(QtCore.QSize(60, 60))
        self.settings_2.setIcon(icon3)
        self.settings_2.setIconSize(QtCore.QSize(30, 30))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)
        self.settings_2.setObjectName("settings_2")
        self.verticalLayout.addWidget(self.settings_2)
        self.pushButton_11 = QtWidgets.QPushButton(self.icons_names)
        self.pushButton_11.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.gridLayout.addWidget(self.icons_names, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dashboard_btn1.toggled['bool'].connect(self.dashboard_btn2.setChecked) # type: ignore
        self.search_btn1.toggled['bool'].connect(self.search_btn2.setChecked) # type: ignore
        self.notification_1.toggled['bool'].connect(self.notification_2.setChecked) # type: ignore
        self.settings_1.toggled['bool'].connect(self.settings_2.setChecked) # type: ignore
        self.dashboard_btn2.toggled['bool'].connect(self.dashboard_btn1.setChecked) # type: ignore
        self.search_btn2.toggled['bool'].connect(self.search_btn1.setChecked) # type: ignore
        self.notification_2.toggled['bool'].connect(self.notification_1.setChecked) # type: ignore
        self.settings_2.toggled['bool'].connect(self.settings_1.setChecked) # type: ignore
        self.pushButton_7.toggled['bool'].connect(self.icons_only.setHidden) # type: ignore
        self.pushButton_7.toggled['bool'].connect(self.icons_names.setVisible) # type: ignore
        self.signout_1.toggled['bool'].connect(self.pushButton_11.setChecked) # type: ignore
        self.pushButton_11.toggled['bool'].connect(self.signout_1.setChecked) # type: ignore
        self.signout_1.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.pushButton_11.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "MENU"))
        self.lineEdit.setText(_translate("MainWindow", "EYE OF THE SAURON"))
        self.dashboard_btn2.setText(_translate("MainWindow", "DASHBOARD"))
        self.search_btn2.setText(_translate("MainWindow", "SEARCH"))
        self.notification_2.setText(_translate("MainWindow", "NOTIFICATION"))
        self.settings_2.setText(_translate("MainWindow", "SETTINGS"))
        self.pushButton_11.setText(_translate("MainWindow", "SIGN OUT"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
