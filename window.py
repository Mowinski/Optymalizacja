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
        Form.resize(800, 600)

        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 131, 540))
        self.layoutWidget.setObjectName("layoutWidget")
        # OPTIONS
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.selection = QtGui.QGroupBox(self.layoutWidget)
        self.selection.setObjectName("selection")
        self.cross_simple_2 = QtGui.QRadioButton(self.selection)
        self.cross_simple_2.setGeometry(QtCore.QRect(0, 30, 108, 22))
        self.cross_simple_2.setObjectName("cross_simple_2")
        self.cross_simple_2.toggle()
        self.cross_artmetic_2 = QtGui.QRadioButton(self.selection)
        self.cross_artmetic_2.setGeometry(QtCore.QRect(0, 60, 136, 22))
        self.cross_artmetic_2.setObjectName("cross_artmetic_2")

        self.mutation = QtGui.QGroupBox(self.selection)
        self.mutation.setGeometry(QtCore.QRect(0, 110, 131, 131))
        self.mutation.setObjectName("mutation")
        self.mutation_unity_2 = QtGui.QRadioButton(self.mutation)
        self.mutation_unity_2.setGeometry(QtCore.QRect(0, 20, 136, 22))
        self.mutation_unity_2.setObjectName("mutation_unity_2")
        self.mutation_unity_2.toggle()
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
        self.function_akley_2.toggle()
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
        self.function_other = QtGui.QRadioButton(self.function)
        self.function_other.setGeometry(QtCore.QRect(0, 130, 136, 22))
        self.function_other.setObjectName("function_other")

        self.strategy = QtGui.QGroupBox(self.selection)
        self.strategy.setGeometry(QtCore.QRect(0, 400, 120, 171))
        self.strategy.setObjectName("strategy")
        self.strategy_genetic = QtGui.QRadioButton(self.strategy)
        self.strategy_genetic.setGeometry(QtCore.QRect(0, 20, 108, 22))
        self.strategy_genetic.setObjectName("strategy_genetic")
        self.strategy_mipluslambda = QtGui.QRadioButton(self.strategy)
        self.strategy_mipluslambda.setGeometry(QtCore.QRect(0, 45, 108, 22))
        self.strategy_mipluslambda.setObjectName("strategy_mi_plus_lambda")
        self.strategy_mipluslambda.toggle()
        self.strategy_milambda = QtGui.QRadioButton(self.strategy)
        self.strategy_milambda.setGeometry(QtCore.QRect(0, 70, 108, 22))
        self.strategy_milambda.setObjectName("strategy_milambda")
        self.strategy_two = QtGui.QRadioButton(self.strategy)
        self.strategy_two.setGeometry(QtCore.QRect(0, 100, 108, 22))
        self.strategy_two.setObjectName("strategy_two")
        self.verticalLayout_2.addWidget(self.selection)
        # END OPTIONS

        self.graphicsView_2 = QtGui.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(140, 90, 500, 400))
        self.graphicsView_2.setObjectName("graphicsView_2")
        # Rysuj
        self.calculateButton = QtGui.QPushButton(Form)
        self.calculateButton.setGeometry(QtCore.QRect(660, 50, 50, 27))
        self.calculateButton.setObjectName("calculateButton")
        # Epoka
        self.stepButton = QtGui.QPushButton(Form)
        self.stepButton.setGeometry(QtCore.QRect(660, 80, 50, 27))
        self.stepButton.setObjectName("stepButton")
        # Rysuj kroki
        self.drawButton = QtGui.QPushButton(Form)
        self.drawButton.setGeometry(QtCore.QRect(720, 50, 60, 27))
        self.drawButton.setObjectName("drewButton")
        # LICZNIK
        self.epochNumber = QtGui.QLCDNumber(Form)
        self.epochNumber.setGeometry(QtCore.QRect(720, 80, 50, 27))
        self.epochNumber.setObjectName("epochNumber")
        # Rozwiaz
        self.complate = QtGui.QPushButton(Form)
        self.complate.setGeometry(QtCore.QRect(660, 110, 50, 27))
        self.complate.setObjectName("complateButton")
        # Rozwiaz bez rysowania
        self.complate_without_draw = QtGui.QPushButton(Form)
        self.complate_without_draw.setGeometry(QtCore.QRect(660, 140, 120, 27))
        self.complate_without_draw.setObjectName("complatewithoutdrawButton")
        # Funkcja celu:
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 500, 70, 20))
        self.label.setObjectName("label")
        # Wartosc funkcji celu
        self.targetLabel = QtGui.QLabel(Form)
        self.targetLabel.setGeometry(QtCore.QRect(210, 500, 120, 20))
        self.targetLabel.setObjectName("targetLabel")
        # Koordynaty
        self.coordsLabel = QtGui.QLabel(Form)
        self.coordsLabel.setGeometry(QtCore.QRect(140, 520, 500, 90))
        self.coordsLabel.setObjectName("coordsLabel")
        # Funkcja
        self.flabel = QtGui.QLabel(Form)
        self.flabel.setGeometry(QtCore.QRect(140, 30, 50, 30))
        self.flabel.setObjectName("flabel")
        # Funkcja edit
        self.function_recipce = QtGui.QTextEdit(Form)
        self.function_recipce.setGeometry(QtCore.QRect(140, 50, 180, 30))
        self.function_recipce.setObjectName('function_recipse')
        # Zakres
        self.range_label = QtGui.QLabel(Form)
        self.range_label.setGeometry(QtCore.QRect(330, 30, 50, 30))
        self.range_label.setObjectName("range_label")
        # Zakres EDIT
        self.range = QtGui.QTextEdit(Form)
        self.range.setGeometry(QtCore.QRect(330, 50, 60, 30))
        self.range.setObjectName('function_recipse')
        # Mi
        self.milabel = QtGui.QLabel(Form)
        self.milabel.setGeometry(QtCore.QRect(400, 30, 40, 30))
        self.milabel.setObjectName("milabel")
        # Mi edit
        self.mi = QtGui.QTextEdit(Form)
        self.mi.setGeometry(QtCore.QRect(400, 50, 40, 30))
        self.mi.setObjectName('mi')
        # Lambda
        self.lambdalabel = QtGui.QLabel(Form)
        self.lambdalabel.setGeometry(QtCore.QRect(450, 30, 40, 30))
        self.lambdalabel.setObjectName("lambdalabel")
        # Lambda edit
        self.lambd = QtGui.QTextEdit(Form)
        self.lambd.setGeometry(QtCore.QRect(450, 50, 40, 30))
        self.lambd.setObjectName('lambd')
        # Ilosc iteracji
        self.nlabel = QtGui.QLabel(Form)
        self.nlabel.setGeometry(QtCore.QRect(500, 30, 50, 30))
        self.nlabel.setObjectName("nlabel")
        # EDIT ILOSC ITERACJI
        self.n = QtGui.QTextEdit(Form)
        self.n.setGeometry(QtCore.QRect(500, 50, 50, 30))
        self.n.setObjectName("n")
        # % Mutacji
        self.proc_mutation_label = QtGui.QLabel(Form)
        self.proc_mutation_label.setGeometry(QtCore.QRect(560, 30, 50, 30))
        self.proc_mutation_label.setObjectName("procent_mutation")
        # EDIT ILOSC ITERACJI
        self.proc_mutation = QtGui.QTextEdit(Form)
        self.proc_mutation.setGeometry(QtCore.QRect(560, 50, 50, 30))
        self.proc_mutation.setObjectName("n")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("Form", "Rysuj", None, QtGui.QApplication.UnicodeUTF8))
        self.complate.setText(QtGui.QApplication.translate("Form", "Rozwiaz", None, QtGui.QApplication.UnicodeUTF8))
        self.complate_without_draw.setText(QtGui.QApplication.translate("Form", "Rozwiaz bez rysowania", None, QtGui.QApplication.UnicodeUTF8))
        self.selection.setTitle(QtGui.QApplication.translate("Form", "Krzyżowanie", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_simple_2.setText(QtGui.QApplication.translate("Form", "Proste", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_artmetic_2.setText(QtGui.QApplication.translate("Form", "Arytmetyczne", None, QtGui.QApplication.UnicodeUTF8))

        self.strategy.setTitle(QtGui.QApplication.translate('Form', 'Strategie', None, QtGui.QApplication.UnicodeUTF8))
        self.strategy_genetic.setText(QtGui.QApplication.translate('Form', 'Alg. Genetyczny', None, QtGui.QApplication.UnicodeUTF8))
        self.strategy_mipluslambda.setText(QtGui.QApplication.translate('Form', 'Strat. (mi + lambda)', None, QtGui.QApplication.UnicodeUTF8))
        self.strategy_milambda.setText(QtGui.QApplication.translate('Form', 'Strat. (mi lambda)', None, QtGui.QApplication.UnicodeUTF8))
        self.strategy_two.setText(QtGui.QApplication.translate('Form', 'Strat. jednoelementowa', None, QtGui.QApplication.UnicodeUTF8))

        self.mutation.setTitle(QtGui.QApplication.translate("Form", "Mutacja", None, QtGui.QApplication.UnicodeUTF8))
        self.mutation_unity_2.setText(QtGui.QApplication.translate("Form", "Równomierna", None, QtGui.QApplication.UnicodeUTF8))
        self.mutacion_gradient_2.setText(QtGui.QApplication.translate("Form", "Gradientowa", None, QtGui.QApplication.UnicodeUTF8))
        self.mutation_nonunity_2.setText(QtGui.QApplication.translate("Form", "Nierównomierna", None, QtGui.QApplication.UnicodeUTF8))

        self.function.setTitle(QtGui.QApplication.translate("Form", "Funkcje", None, QtGui.QApplication.UnicodeUTF8))
        self.function_akley_2.setText(QtGui.QApplication.translate("Form", "Akley", None, QtGui.QApplication.UnicodeUTF8))
        self.function_rastring_2.setText(QtGui.QApplication.translate("Form", "Rastringa", None, QtGui.QApplication.UnicodeUTF8))
        self.function_golstein_2.setText(QtGui.QApplication.translate("Form", "Goldsteina-Prica", None, QtGui.QApplication.UnicodeUTF8))
        self.function_gem_2.setText(QtGui.QApplication.translate("Form", "Geem", None, QtGui.QApplication.UnicodeUTF8))
        self.function_rosenbrock_2.setText(QtGui.QApplication.translate("Form", "Rosenbrock\'a", None, QtGui.QApplication.UnicodeUTF8))
        self.function_other.setText(QtGui.QApplication.translate("Form", "Inna", None, QtGui.QApplication.UnicodeUTF8))

        self.stepButton.setText(QtGui.QApplication.translate("Form", "Epoka", None, QtGui.QApplication.UnicodeUTF8))
        self.drawButton.setText(QtGui.QApplication.translate("Form", "Rysuj kroki", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Funkcja celu:", None, QtGui.QApplication.UnicodeUTF8))
        self.flabel.setText(QtGui.QApplication.translate("Form", "Funkcja:", None, QtGui.QApplication.UnicodeUTF8))
        self.range_label.setText(QtGui.QApplication.translate("Form", "Zakres:", None, QtGui.QApplication.UnicodeUTF8))

        self.milabel.setText(QtGui.QApplication.translate("Form", "mi (N):", None, QtGui.QApplication.UnicodeUTF8))
        self.lambdalabel.setText(QtGui.QApplication.translate("Form", "lambda:", None, QtGui.QApplication.UnicodeUTF8))
        self.nlabel.setText(QtGui.QApplication.translate("Form", "Ilość iter.", None, QtGui.QApplication.UnicodeUTF8))
        self.proc_mutation_label.setText(QtGui.QApplication.translate("Form", "% mutacji", None, QtGui.QApplication.UnicodeUTF8))

        # default text edit
        self.mi.setText("100")
        self.lambd.setText("100")
        self.n.setText("50")
        self.range.setText("-5 5; -5 5")
        self.proc_mutation.setText("10")
        #self.function_recipce.setText("sin(x[0])+cos(x[1])+sin(x[2]*x[3])+cos(x[4]*x[5])")
        self.function_recipce.setText("(x[0]-2)**2+(x[0]-x[1]**2)**2")