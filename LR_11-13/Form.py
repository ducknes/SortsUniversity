# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 2, 481, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.bubble = QtWidgets.QCheckBox(self.centralwidget)
        self.bubble.setGeometry(QtCore.QRect(115, 28, 20, 20))
        self.bubble.setText("")
        self.bubble.setObjectName("bubble")
        self.select = QtWidgets.QCheckBox(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(115, 59, 21, 20))
        self.select.setText("")
        self.select.setObjectName("select")
        self.inlude = QtWidgets.QCheckBox(self.centralwidget)
        self.inlude.setGeometry(QtCore.QRect(115, 89, 21, 20))
        self.inlude.setText("")
        self.inlude.setObjectName("inlude")
        self.shell = QtWidgets.QCheckBox(self.centralwidget)
        self.shell.setGeometry(QtCore.QRect(115, 119, 21, 20))
        self.shell.setText("")
        self.shell.setObjectName("shell")
        self.fast = QtWidgets.QCheckBox(self.centralwidget)
        self.fast.setGeometry(QtCore.QRect(115, 149, 21, 20))
        self.fast.setText("")
        self.fast.setObjectName("fast")
        self.line = QtWidgets.QCheckBox(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(116, 178, 21, 20))
        self.line.setText("")
        self.line.setObjectName("line")
        self.buildin = QtWidgets.QCheckBox(self.centralwidget)
        self.buildin.setGeometry(QtCore.QRect(116, 209, 21, 20))
        self.buildin.setText("")
        self.buildin.setObjectName("buildin")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(243, 242, 111, 24))
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setProperty("value", 10000)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 246, 111, 16))
        self.label.setObjectName("label")
        self.sort = QtWidgets.QPushButton(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(6, 240, 113, 32))
        self.sort.setObjectName("sort")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 240, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Антонов 21ВП2 Лабораторная работа №11-13"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Обмен"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Выбор"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Включение"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Шелла"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Быстрая"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Линейная"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Встроенная"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Сравнения"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Перестановки"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Время"))
        self.label.setText(_translate("MainWindow", "Размер массива"))
        self.sort.setText(_translate("MainWindow", "Сортировать"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
