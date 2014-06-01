__author__ = 'Kamil'
from window import MainForm
from PyQt4 import QtGui, QtCore, QtOpenGL
from functions import paint_function, rosenbrock, geem, ackley, restring, goldstein
from functions import mix_simple, aritmic_selection
from functions import mutation, mutation_nonlinear
from numpy import *
from genetic import Genetic
import sys, os, re


class Optymalizacja(QtGui.QMainWindow):
    LIMIT_X = [-5, 5]
    LIMIT_Y = [-5, 5]

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MainForm()
        self.ui.setupUi(self)
        self.genetic = None
        self.epochNumber = 0
        self.steps = []
        self.function = None
        self.range = []
        self.chance = 10
        self.m = 2
        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL("clicked()"), self.calculate)
        QtCore.QObject.connect(self.ui.stepButton, QtCore.SIGNAL("clicked()"), self.epoch)
        QtCore.QObject.connect(self.ui.drawButton, QtCore.SIGNAL("clicked()"), self.draw)
        QtCore.QObject.connect(self.ui.complate, QtCore.SIGNAL("clicked()"), self.complate)
        QtCore.QObject.connect(self.ui.complate_without_draw, QtCore.SIGNAL("clicked()"), self.complate_without_draw)
        QtCore.QObject.connect(self.ui.points, QtCore.SIGNAL("clicked()"), self.points)

    def calculate(self, draw=True):
        # Cross
        if self.ui.cross_simple_2.isChecked():
            crossing = mix_simple
        elif self.ui.cross_artmetic_2.isChecked():
            crossing = aritmic_selection
        else:
            raise TypeError('Not selected crossing')
        # Mutation
        if self.ui.mutation_unity_2.isChecked():
            fmutation = mutation
        elif self.ui.mutation_nonunity_2.isChecked():
            fmutation = mutation_nonlinear
        elif self.ui.mutacion_gradient_2.isChecked():
            fmutation = None
        else:
            raise TypeError('Not selected mutattion')
        # Function
        if self.ui.function_rosenbrock_2.isChecked():
            self.function = rosenbrock
        elif self.ui.function_akley_2.isChecked():
            self.function = ackley
        elif self.ui.function_gem_2.isChecked():
            self.function = geem
        elif self.ui.function_golstein_2.isChecked():
            self.function = goldstein
        elif self.ui.function_rastring_2.isChecked():
            self.function = restring
        else:
            tmp_function = self.ui.function_recipce.toPlainText()
            self.function = lambda *x: eval(tmp_function)
            m = re.findall("x\[\d\]", tmp_function)
            chop = lambda x: int(x[2:-1])
            self.m = max(list(map(chop, m))) + 1
        if self.ui.strategy_genetic.isChecked():
            strategy = 'genetic'
        elif self.ui.strategy_two.isChecked():
            strategy = 'two'
        elif self.ui.strategy_milambda.isChecked():
            strategy = 'mi_lambda'
        elif self.ui.strategy_mipluslambda.isChecked():
            strategy = 'mi_plus_lambda'
        #limit
        try:
            tmp = self.ui.range.toPlainText()
            tmp = tmp.split(";")
            self.range = [list(map(float, t.split())) for t in tmp]
        except:
            self.range = [self.LIMIT_X, self.LIMIT_Y]
        try:
            self.chance = float(self.ui.proc_mutation.toPlainText().split(';')[0])
        except:
            self.chance = 10
        if draw:
            f = paint_function(self.range, self.function)
            scene = QtGui.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap(f.name))
            self.ui.graphicsView_2.setScene(scene)
            f.close()
            os.unlink(f.name)

        mi = int(self.ui.mi.toPlainText())
        lambd = int(self.ui.lambd.toPlainText())
        self.genetic = Genetic(self.function, crossing, fmutation, strategy, mi, lambd, self.range, self.m, self.chance)
        self.steps = []
        self.ui.graphicsView_2.setViewport(QtOpenGL.QGLWidget())
        self.epochNumber = 0

    def epoch(self):
        self.genetic.sort()
        self.genetic.newEpoch(self.epochNumber)
        self.epochNumber += 1
        self.ui.epochNumber.display(self.epochNumber)
        self.genetic.sort()
        self.ui.targetLabel.setText(str(round(self.genetic.population[0].cost, 7)))
        self.ui.coordsLabel.setText("Rozwiązanie: x: {0} y: {1}".format(round(self.genetic.population[0].getValue(self.range[0][0], self.range[0][1], 0), 7),
                                                                        round(self.genetic.population[0].getValue(self.range[1][0], self.range[1][1], 1), 7)))
        self.steps.append((round(self.genetic.population[0].getValue(self.range[0][0], self.range[0][1], 0), 7),
                           round(self.genetic.population[0].getValue(self.range[1][0], self.range[1][1], 1), 7)))

    def complate(self):
        n = int(self.ui.n.toPlainText())
        if not n:
            raise TypeError('Nie podano warunku zakończenia')
        for i in range(n):
            self.genetic.sort()
            self.genetic.newEpoch(self.epochNumber)
            self.epochNumber += 1
            self.ui.epochNumber.display(self.epochNumber)
            self.genetic.sort()
            self.steps.append((round(self.genetic.population[0].getValue(self.range[0][0], self.range[0][1], 0), 7),
                           round(self.genetic.population[0].getValue(self.range[1][0], self.range[1][1], 1), 7)))
        self.ui.targetLabel.setText(str(round(self.genetic.population[0].cost, 7)))
        self.ui.coordsLabel.setText("Rozwiązanie: x: {0} y: {1}".format(round(self.genetic.population[0].getValue(self.range[0][0], self.range[0][1], 0), 7),
                                                                        round(self.genetic.population[0].getValue(self.range[1][0], self.range[1][1], 1), 7)))

    def complate_without_draw(self):
        self.calculate(False)
        n = int(self.ui.n.toPlainText())
        if not n:
            raise TypeError('Nie podano warunku zakończenia')
        for i in range(n):
            self.genetic.sort()
            self.genetic.newEpoch(self.epochNumber)
            self.epochNumber += 1
            self.ui.epochNumber.display(self.epochNumber)
            self.genetic.sort()
            self.steps.append(self.genetic.population[0].getValues(self.range))
        self.ui.targetLabel.setText(str(round(self.genetic.population[0].cost, 7)))
        result = self.genetic.population[0].getValues(self.range)
        tmp = "Rozwiazanie: "
        i = 1
        for r in result:
            tmp += "x{0} = {1} ".format(i, round(r, 6))
            if i % 4 == 0:
                tmp += '\n'
            i += 1
        self.ui.coordsLabel.setText(tmp)

    def draw(self):
        f = paint_function(self.range, self.function, self.steps)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(f.name))
        self.ui.graphicsView_2.setScene(scene)
        f.close()
        os.unlink(f.name)

    def points(self):
        with open('points.txt', 'w') as f:
            for point in self.steps:
                f.write("{0} : {1}\n".format(str(point), self.function(*point)))
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Optymalizacja()
    myapp.show()
    sys.exit(app.exec_())
