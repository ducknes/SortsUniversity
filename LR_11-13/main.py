import math
import random
import sys
from time import time
from Form import *


class LabaFinal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.quit)
        self.ui.sort.clicked.connect(self.sorts_analyze)

    def quit(self):
        self.ui.pushButton.clicked.connect(QtWidgets.QApplication.instance().quit)

    def testfunction(self):
        if self.ui.bubble.isChecked():
            self.ui.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem("hello"))
            print(self.ui.spinBox.value())

    def bubble_sort(self, arrayFrom):
        array_for_sort = arrayFrom.copy()
        compare_count = 0
        change_count = 0

        start_time = time()
        for i in range(self.ui.spinBox.value()):
            already_sort = True
            for j in range(self.ui.spinBox.value() - i - 1):
                if array_for_sort[j] > array_for_sort[j + 1]:
                    compare_count += 1
                    change_count += 1
                    array_for_sort[j], array_for_sort[j + 1] = array_for_sort[j + 1], array_for_sort[j]
                    already_sort = False
                else:
                    compare_count += 1

            if already_sort:
                break
        end_time = time()

        self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(compare_count)))
        self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(change_count)))
        self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(float('{:.3f}'.format(end_time - start_time)))))

    def selection_sort(self, arrayFrom):
        array_for_sort = arrayFrom.copy()
        compare_count = 0
        change_count = 0

        start_time = time()
        for i in range(self.ui.spinBox.value() - 1):
            min_index = i

            for j in range(i + 1, self.ui.spinBox.value()):
                if array_for_sort[j] < array_for_sort[min_index]:
                    min_index = j
                    compare_count += 1
                else:
                    compare_count += 1
            
            array_for_sort[i], array_for_sort[min_index] = array_for_sort[min_index], array_for_sort[i]
            change_count += 1
        end_time = time()

        self.ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(compare_count)))
        self.ui.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(change_count)))
        self.ui.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem(str(float('{:.3f}'.format(end_time - start_time)))))

    def insertion_sort(self, arrayFrom):
        array_for_sort = arrayFrom.copy()
        compare_count = 0
        change_count = 0

        start_time = time()
        for i in range(1, self.ui.spinBox.value()):

            key = array_for_sort[i]
            j = i - 1
            while j >= 0 and key < array_for_sort[j]:
                compare_count += 1
                array_for_sort[j + 1] = array_for_sort[j]
                j -= 1
                change_count += 1
            array_for_sort[j + 1] = key
            change_count += 1
        end_time = time()

        self.ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(str(compare_count)))
        self.ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(str(change_count)))
        self.ui.tableWidget.setItem(2, 3, QtWidgets.QTableWidgetItem(str(float('{:.3f}'.format(end_time - start_time)))))

    def sorts_analyze(self):
        mainArray = [random.randint(1, 100000) for x in range(self.ui.spinBox.value())]
        if self.ui.bubble.isChecked():
            self.bubble_sort(mainArray)
        if self.ui.select.isChecked():
            self.selection_sort(mainArray)
        if self.ui.inlude.isChecked():
            self.insertion_sort(mainArray)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LabaFinal()
    myapp.show()
    sys.exit(app.exec())
