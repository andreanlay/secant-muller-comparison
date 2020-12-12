import sys
import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne

from PyQt5 import QtCore, QtGui, QtWidgets

exp = x1 = x2 = x3 = None
max_error = max_iter = None

secant_roots = secant_errors = 0
muller_roots = muller_errors = 0

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1008, 688)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        
        self.input_groupbox = QtWidgets.QGroupBox(Form)
        self.input_groupbox.setGeometry(QtCore.QRect(30, 20, 471, 121))
        self.input_groupbox.setObjectName("input_groupbox")
        
        self.exp_input = QtWidgets.QLineEdit(self.input_groupbox)
        self.exp_input.setGeometry(QtCore.QRect(50, 30, 261, 20))
        self.exp_input.setObjectName("exp_input")
        
        self.fx_label = QtWidgets.QLabel(self.input_groupbox)
        self.fx_label.setGeometry(QtCore.QRect(20, 30, 21, 21))
        self.fx_label.setObjectName("fx_label")
        
        self.x1_label = QtWidgets.QLabel(self.input_groupbox)
        self.x1_label.setGeometry(QtCore.QRect(20, 60, 16, 21))
        self.x1_label.setObjectName("x1_label")
        self.x1_input = QtWidgets.QLineEdit(self.input_groupbox)
        self.x1_input.setGeometry(QtCore.QRect(50, 60, 51, 20))
        self.x1_input.setObjectName("x1_input")
        
        self.x2_input = QtWidgets.QLineEdit(self.input_groupbox)
        self.x2_input.setGeometry(QtCore.QRect(50, 90, 51, 20))
        self.x2_input.setObjectName("x2_input")
        self.x2_label = QtWidgets.QLabel(self.input_groupbox)
        self.x2_label.setGeometry(QtCore.QRect(20, 90, 16, 21))
        self.x2_label.setObjectName("x2_label")
        
        self.x3_label = QtWidgets.QLabel(self.input_groupbox)
        self.x3_label.setGeometry(QtCore.QRect(150, 60, 16, 21))
        self.x3_label.setObjectName("x3_label")
        self.x3_input = QtWidgets.QLineEdit(self.input_groupbox)
        self.x3_input.setGeometry(QtCore.QRect(180, 60, 51, 20))
        self.x3_input.setObjectName("x3_input")
        
        self.hyperparameter_groupbox = QtWidgets.QGroupBox(Form)
        self.hyperparameter_groupbox.setGeometry(QtCore.QRect(510, 20, 471, 121))
        self.hyperparameter_groupbox.setObjectName("hyperparameter_groupbox")
        
        self.error_input = QtWidgets.QLineEdit(self.hyperparameter_groupbox)
        self.error_input.setGeometry(QtCore.QRect(130, 30, 191, 20))
        self.error_input.setObjectName("error_input")

        self.max_error_label = QtWidgets.QLabel(self.hyperparameter_groupbox)
        self.max_error_label.setGeometry(QtCore.QRect(10, 30, 95, 21))
        self.max_error_label.setObjectName("max_error_label")
        
        self.max_inter_input = QtWidgets.QLineEdit(self.hyperparameter_groupbox)
        self.max_inter_input.setGeometry(QtCore.QRect(130, 70, 191, 20))
        self.max_inter_input.setText("")
        self.max_inter_input.setObjectName("max_inter_input")
        
        self.max_iteration_label = QtWidgets.QLabel(self.hyperparameter_groupbox)
        self.max_iteration_label.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.max_iteration_label.setObjectName("max_iteration_label")
        
        self.secant_table = QtWidgets.QTableWidget(Form)
        self.secant_table.setEnabled(True)
        self.secant_table.setGeometry(QtCore.QRect(10, 220, 971, 192))
        
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        
        self.secant_table.setFont(font)
        self.secant_table.setShowGrid(True)
        self.secant_table.setRowCount(0)
        self.secant_table.setColumnCount(4)
        self.secant_table.setObjectName("secant_table")
        item = QtWidgets.QTableWidgetItem()
        self.secant_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.secant_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.secant_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.secant_table.setHorizontalHeaderItem(3, item)
        self.secant_table.horizontalHeader().setVisible(True)
        self.secant_table.horizontalHeader().setDefaultSectionSize(242)
        self.secant_table.verticalHeader().setStretchLastSection(False)
        self.secant_title_label = QtWidgets.QLabel(Form)
        self.secant_title_label.setGeometry(QtCore.QRect(20, 190, 111, 16))
        self.secant_title_label.setObjectName("secant_title_label")
        
        self.muller_table = QtWidgets.QTableWidget(Form)
        self.muller_table.setGeometry(QtCore.QRect(10, 460, 971, 191))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.muller_table.setFont(font)
        self.muller_table.setRowCount(0)
        self.muller_table.setColumnCount(5)
        self.muller_table.setObjectName("muller_table")
        item = QtWidgets.QTableWidgetItem()
        self.muller_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.muller_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.muller_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.muller_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.muller_table.setHorizontalHeaderItem(4, item)
        self.muller_table.horizontalHeader().setDefaultSectionSize(194)
        self.muller_title_label = QtWidgets.QLabel(Form)
        self.muller_title_label.setGeometry(QtCore.QRect(20, 430, 111, 16))
        self.muller_title_label.setObjectName("muller_title_label")
        
        self.plot_btn = QtWidgets.QPushButton(Form)
        self.plot_btn.setGeometry(QtCore.QRect(140, 150, 91, 23))
        self.plot_btn.setObjectName("plot_btn")
        self.plot_btn.clicked.connect(plot_graph)

        self.calculate_btn = QtWidgets.QPushButton(Form)
        self.calculate_btn.setGeometry(QtCore.QRect(30, 150, 91, 23))
        self.calculate_btn.setObjectName("calculate_btn")
        self.calculate_btn.clicked.connect(calculate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Secant & Muller Method Comparison"))
        self.input_groupbox.setTitle(_translate("Form", "Input"))
        self.fx_label.setText(_translate("Form", "f(x)"))
        self.x1_label.setText(_translate("Form", "x1"))
        self.x2_label.setText(_translate("Form", "x2"))
        self.x3_label.setText(_translate("Form", "x3"))
        self.hyperparameter_groupbox.setTitle(_translate("Form", "Option"))
        self.error_input.setPlaceholderText(_translate("Form", "Default: 3%"))
        self.max_error_label.setText(_translate("Form", "Max Error (%)"))
        self.max_inter_input.setPlaceholderText(_translate("Form", "Default: 100"))
        self.max_iteration_label.setText(_translate("Form", "Max Iteration"))
        item = self.secant_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "x(i-1)"))
        item = self.secant_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x(i)"))
        item = self.secant_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "f(x)"))
        item = self.secant_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Error (%)"))
        item = self.muller_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "x1"))
        item = self.muller_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x2"))
        item = self.muller_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "x3"))
        item = self.muller_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Root"))
        item = self.muller_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Error (%)"))
        self.secant_title_label.setText(_translate("Form", "Secant Method"))
        self.muller_title_label.setText(_translate("Form", "Muller Method"))
        self.plot_btn.setText(_translate("Form", "Show Plot"))
        self.calculate_btn.setText(_translate("Form", "Calculate"))

def calculate():
    global exp, x1, x2, x3, max_error, max_iter
    global secant_roots, secant_errors
    global muller_roots, muller_errors
    try:
        exp = ui.exp_input.text()
        x1 = float(ui.x1_input.text())
        x2 = float(ui.x2_input.text())
        x3 = float(ui.x3_input.text())
        
        max_error = float(ui.error_input.text()) if ui.error_input.text() else 3.0
        max_iter = int(ui.max_inter_input.text()) if ui.max_inter_input.text() else 100
    except:
        display_error('Please fill all input fields')
        return
        
    try:
        f(x1)
    except:
        display_error('Wrong input format!')
        return

    try:
        secant_roots, secant_errors, x_prev, x_next = secant(x1, x2)
        set_secant_data(secant_roots, secant_errors, x_prev, x_next)
    except:
        display_error('Secant failed to converge')

    try:
        muller_roots, muller_errors, x1s, x2s, x3s = muller(x1, x2, x3)
        set_muller_data(muller_roots, muller_errors, x1s, x2s, x3s)
    except:
        display_error('Muller failed to converge')

def set_secant_data(roots, errors, x_prev, x_next):
    ui.secant_table.setRowCount(0)
    n = len(roots)
    for i in range(n):
        ui.secant_table.insertRow(i)
        ui.secant_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(x_prev[i])))
        ui.secant_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(x_next[i])))
        ui.secant_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(roots[i])))
        ui.secant_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(errors[i])))

def set_muller_data(roots, errors, x1, x2, x3):
    ui.muller_table.setRowCount(0)
    n = len(roots)
    for i in range(n):
        ui.muller_table.insertRow(i)
        ui.muller_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(x1[i])))
        ui.muller_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(x2[i])))
        ui.muller_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(x3[i])))
        ui.muller_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(roots[i])))
        ui.muller_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(errors[i])))

def plot_graph():
    plt.subplot(211)
    plt.plot(secant_roots, 'bo--', label='Secant')
    plt.plot(muller_roots, 'go--', label='Muller')
    plt.title(exp)
    plt.legend()
    plt.ylabel('Akar')

    plt.subplot(212)
    plt.plot(secant_errors, 'bo--', label='Secant')
    plt.plot(muller_errors, 'go--', label='Muller')
    plt.ylabel('Error (%)')
    plt.xlabel('Iterasi')
    plt.legend()
    plt.show()

def f(x):
    return ne.evaluate(exp)

def secant(x_prev, x):
    x_list = []
    err_list = [100]
    x_prev_list = [x_prev]
    x_next_list = [x]

    i = 1
    while True:
        x_next = x - f(x) * ((x - x_prev) / (f(x) - f(x_prev)))
        x_list.append(x_next)

        if f(x_next) == 0:
            break
        if i > 1:
            error = abs((x_next - x) / x_next) * 100
            err_list.append(error)
            if err_list[-1] < max_error:
                break

        if i == max_iter:
            display_error('Secant fail converge until {} iteration(s)!'.format(max_iter))
            break
        x_prev = x;
        x = x_next
        x_prev_list.append(x_prev)
        x_next_list.append(x)
        i += 1

    return x_list, err_list, x_prev_list, x_next_list
    
def muller(x0, x1, x2):
    i = 1
    x0_list = [x0]
    x1_list = [x1]
    x2_list = [x2]
    roots = []
    errors = []
    x_new = [x0, x1, x2]

    while True:
        x0 = x_new[0]
        x1 = x_new[1]
        x2 = x_new[2]
        
        h1 = x1 - x0
        h2 = x2 - x1 

        delta0 = (f(x1) - f(x0)) / h1
        delta1 = (f(x2) - f(x1)) / h2
        
        a = (delta1 - delta0) / (h2 + h1)
        b = delta1 + a*h2
        c = f(x2)
            
        D = np.lib.scimath.sqrt(b**2 - 4*a*c)

        h = -2 * c / np.maximum(b + D, b - D)
        x_next = x2 + h
        
        errors.append(abs((x_next - x2) / x_next) * 100)
        roots.append(x_next)

        if f(x_next) == 0:
            break

        if f(x1) == f(x2) == f(x_next):
            display_error('Muller fail to converge! (All points ended in the same function value, apply Secant Method.)')
            break
           
        if x1 == x2 == x_next:
            display_error('Muller fail to converge! (All points ended on the same line)')
            break

        x_new = [x1, x2, x_next]

        if errors[-1] < max_error:
            break
        if i == max_iter:
            display_error('Muller fail to converge until {} iteration(s)'.format(max_iter))
            break

        x0_list.append(x1)
        x1_list.append(x2)
        x2_list.append(x_next)
        i += 1
    
    return roots, errors, x0_list, x1_list, x2_list

def display_error(message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle('Error')
    msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
