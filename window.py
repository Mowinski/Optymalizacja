# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Apr  6 15:43:57 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class MainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        self.calculateButton = QtGui.QPushButton(Form)
        self.calculateButton.setGeometry(QtCore.QRect(730, 700, 92, 27))
        self.calculateButton.setObjectName("calculateButton")
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 131, 400))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selection = QtGui.QGroupBox(self.layoutWidget)
        self.selection.setObjectName("selection")
        self.cross_simple_2 = QtGui.QRadioButton(self.selection)
        self.cross_simple_2.setGeometry(QtCore.QRect(0, 30, 108, 22))
        self.cross_simple_2.setMaximumSize(QtCore.QSize(108, 16777215))
        self.cross_simple_2.setObjectName("cross_simple_2")
        self.cross_artmetic_2 = QtGui.QRadioButton(self.selection)
        self.cross_artmetic_2.setGeometry(QtCore.QRect(0, 60, 136, 22))
        self.cross_artmetic_2.setObjectName("cross_artmetic_2")
        self.mutation = QtGui.QGroupBox(self.selection)
        self.mutation.setGeometry(QtCore.QRect(0, 110, 131, 131))
        self.mutation.setObjectName("mutation")
        self.mutation_unity_2 = QtGui.QRadioButton(self.mutation)
        self.mutation_unity_2.setGeometry(QtCore.QRect(0, 20, 136, 22))
        self.mutation_unity_2.setObjectName("mutation_unity_2")
        self.mutacion_gradient_2 = QtGui.QRadioButton(self.mutation)
        self.mutacion_gradient_2.setGeometry(QtCore.QRect(0, 50, 136, 22))
        self.mutacion_gradient_2.setObjectName("mutacion_gradient_2")
        self.mutation_nonunity_2 = QtGui.QRadioButton(self.mutation)
        self.mutation_nonunity_2.setGeometry(QtCore.QRect(0, 80, 136, 22))
        self.mutation_nonunity_2.setObjectName("mutation_nonunity_2")
        self.function = QtGui.QGroupBox(self.selection)
        self.function.setGeometry(QtCore.QRect(0, 240, 120, 171))
        self.function.setObjectName("function")
        self.function_akley_2 = QtGui.QRadioButton(self.function)
        self.function_akley_2.setGeometry(QtCore.QRect(0, 30, 136, 22))
        self.function_akley_2.setObjectName("function_akley_2")
        self.function_rastring_2 = QtGui.QRadioButton(self.function)
        self.function_rastring_2.setGeometry(QtCore.QRect(0, 50, 136, 22))
        self.function_rastring_2.setObjectName("function_rastring_2")
        self.function_golstein_2 = QtGui.QRadioButton(self.function)
        self.function_golstein_2.setGeometry(QtCore.QRect(0, 70, 136, 22))
        self.function_golstein_2.setObjectName("function_golstein_2")
        self.function_gem_2 = QtGui.QRadioButton(self.function)
        self.function_gem_2.setGeometry(QtCore.QRect(0, 90, 136, 22))
        self.function_gem_2.setObjectName("function_gem_2")
        self.function_rosenbrock_2 = QtGui.QRadioButton(self.function)
        self.function_rosenbrock_2.setGeometry(QtCore.QRect(0, 110, 136, 22))
        self.function_rosenbrock_2.setObjectName("function_rosenbrock_2")
        self.verticalLayout_2.addWidget(self.selection)
        self.graphicsView_2 = QtGui.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(190, 50, 820, 620))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.stepButton = QtGui.QPushButton(Form)
        self.stepButton.setGeometry(QtCore.QRect(560, 700, 92, 27))
        self.stepButton.setObjectName("stepButton")
        self.drawButton = QtGui.QPushButton(Form)
        self.drawButton.setGeometry(QtCore.QRect(360, 700, 92, 27))
        self.drawButton.setObjectName("stepButton")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 450, 91, 17))
        self.label.setObjectName("label")
        self.flabel = QtGui.QLabel(Form)
        self.flabel.setGeometry(QtCore.QRect(40, 700, 92, 27))
        self.flabel.setObjectName("flabel")
        self.function_recipce = QtGui.QTextEdit(Form)
        self.function_recipce.setGeometry(QtCore.QRect(90, 700, 192, 27))
        self.function_recipce.setObjectName('function_recipse')
        self.targetLabel = QtGui.QLabel(Form)
        self.targetLabel.setGeometry(QtCore.QRect(40, 470, 122, 17))
        self.targetLabel.setObjectName("targetLabel")
        self.coordsLabel = QtGui.QLabel(Form)
        self.coordsLabel.setGeometry(QtCore.QRect(40, 490, 82, 40))
        self.coordsLabel.setObjectName("coordsLabel")
        self.epochNumber = QtGui.QLCDNumber(Form)
        self.epochNumber.setGeometry(QtCore.QRect(660, 700, 64, 23))
        self.epochNumber.setObjectName("epochNumber")

        self.rangex = QtGui.QLabel(Form)
        self.rangex.setGeometry(QtCore.QRect(40, 630, 92, 27))
        self.rangex.setObjectName("rangex")
        self.from_x = QtGui.QTextEdit(Form)
        self.from_x.setGeometry(QtCore.QRect(90, 630, 30, 27))
        self.from_x.setObjectName('function_recipse')
        self.to_x = QtGui.QTextEdit(Form)
        self.to_x.setGeometry(QtCore.QRect(130, 630, 30, 27))
        self.to_x.setObjectName('function_recipse')
        self.rangey = QtGui.QLabel(Form)
        self.rangey.setGeometry(QtCore.QRect(40, 660, 92, 27))
        self.rangey.setObjectName("rangey")
        self.from_y = QtGui.QTextEdit(Form)
        self.from_y.setGeometry(QtCore.QRect(90, 660, 30, 27))
        self.from_y.setObjectName('function_recipse')
        self.to_y = QtGui.QTextEdit(Form)
        self.to_y.setGeometry(QtCore.QRect(130, 660, 30, 27))
        self.to_y.setObjectName('function_recipse')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("Form", "Licz", None, QtGui.QApplication.UnicodeUTF8))
        self.selection.setTitle(QtGui.QApplication.translate("Form", "Selekcja", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_simple_2.setText(QtGui.QApplication.translate("Form", "Proste", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_artmetic_2.setText(QtGui.QApplication.translate("Form", "Arytmetyczne", None, QtGui.QApplication.UnicodeUTF8))
        self.mutation.setTitle(QtGui.QApplication.translate("Form", "Mutacja", None, QtGui.QApplication.UnicodeUTF8))
        self.mutation_unity_2.setText(QtGui.QApplication.translate("Form", "Równomierna", None, QtGui.QApplication.UnicodeUTF8))
        self.mutacion_gradient_2.setText(QtGui.QApplication.translate("Form", "Gradientowa", None, QtGui.QApplication.UnicodeUTF8))
        self.mutation_nonunity_2.setText(QtGui.QApplication.translate("Form", "Nierównomierna", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setTitle(QtGui.QApplication.translate("Form", "Funkcje", None, QtGui.QApplication.UnicodeUTF8))
        self.function_akley_2.setText(QtGui.QApplication.translate("Form", "Akley", None, QtGui.QApplication.UnicodeUTF8))
        self.function_rastring_2.setText(QtGui.QApplication.translate("Form", "Rastringa", None, QtGui.QApplication.UnicodeUTF8))
        self.function_golstein_2.setText(QtGui.QApplication.translate("Form", "Golsteina-Prica", None, QtGui.QApplication.UnicodeUTF8))
        self.function_gem_2.setText(QtGui.QApplication.translate("Form", "Geem", None, QtGui.QApplication.UnicodeUTF8))
        self.function_rosenbrock_2.setText(QtGui.QApplication.translate("Form", "Rosenbrock\'a", None, QtGui.QApplication.UnicodeUTF8))
        self.stepButton.setText(QtGui.QApplication.translate("Form", "Epoka", None, QtGui.QApplication.UnicodeUTF8))
        self.drawButton.setText(QtGui.QApplication.translate("Form", "Rysuj kroki", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Funkcja celu:", None, QtGui.QApplication.UnicodeUTF8))
        self.flabel.setText(QtGui.QApplication.translate("Form", "Funkcja:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangex.setText(QtGui.QApplication.translate("Form", "Zakres X:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangey.setText(QtGui.QApplication.translate("Form", "Zakres Y:", None, QtGui.QApplication.UnicodeUTF8))