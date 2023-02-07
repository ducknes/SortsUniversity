import math
import random
import sys
from time import time
from newForm import *

QSchanges = 0
QScompares = 0

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

    def quick_sort(self, arrayFrom, start, end):
        if end - start > 1:
            p = self.partition(arrayFrom, start, end)
            self.quick_sort(arrayFrom, start, p)
            self.quick_sort(arrayFrom, p + 1, end)


    def partition(self, arrayFrom, start, end):
        global QSchanges
        global QScompares
        pivot = arrayFrom[start]
        i = start + 1
        j = end - 1

        while True:
            while i <= j and arrayFrom[i] <= pivot:
                i += 1
                QScompares += 1
            while i <= j and arrayFrom[j] >= pivot:
                j -= 1
                QScompares += 1

            if i <= j:
                arrayFrom[i], arrayFrom[j] = arrayFrom[j], arrayFrom[i]
                QSchanges += 1
            else:
                arrayFrom[start], arrayFrom[j] = arrayFrom[j], arrayFrom[start]
                QSchanges += 1
                return j

    def sorts_analyze(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.update()
        mainArray = [random.randint(1, 100000) for x in range(self.ui.spinBox.value())]
        if self.ui.bubble.isChecked():
            self.bubble_sort(mainArray)
        if self.ui.select.isChecked():
            self.selection_sort(mainArray)
        if self.ui.inlude.isChecked():
            self.insertion_sort(mainArray)
        if self.ui.fast.isChecked():
            array_for_sort = mainArray.copy()

            start_time = time()
            self.quick_sort(array_for_sort, 0, len(array_for_sort))
            end_time = time()

            self.ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(str(QScompares)))
            self.ui.tableWidget.setItem(4, 2, QtWidgets.QTableWidgetItem(str(QSchanges)))
            self.ui.tableWidget.setItem(4, 3, QtWidgets.QTableWidgetItem(str(float('{:.3f}'.format(end_time - start_time)))))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LabaFinal()
    myapp.show()
    sys.exit(app.exec())
