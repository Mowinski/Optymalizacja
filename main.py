__author__ = 'Kamil'
from window import MainForm
from PyQt4 import QtGui, QtCore, QtOpenGL
from functions import paint_function, rosenbrock, geem, ackley, restring, goldstein
from functions import mix_simple, aritmic_selection
from functions import mutation, mutation_nonlinear
import sys, os
from genetic import Genetic


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
        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL("clicked()"), self.calculate)
        QtCore.QObject.connect(self.ui.stepButton, QtCore.SIGNAL("clicked()"), self.epoch)
        QtCore.QObject.connect(self.ui.drawButton, QtCore.SIGNAL("clicked()"), self.draw)

    def calculate(self):
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
            raise TypeError('Not selected function')
        f = paint_function(self.LIMIT_X, self.LIMIT_Y, self.function)
        self.genetic = Genetic(self.function, crossing, fmutation)
        self.steps = []

        self.ui.graphicsView_2.setViewport(QtOpenGL.QGLWidget())
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(f.name))
        self.ui.graphicsView_2.setScene(scene)
        f.close()
        os.unlink(f.name)
        self.epochNumber = 0

    def epoch(self):
        self.genetic.sort()
        self.genetic.newEpoch(self.epochNumber)
        self.epochNumber += 1
        self.ui.epochNumber.display(self.epochNumber)
        self.genetic.sort()
        self.ui.targetLabel.setText(str(round(self.genetic.population[0].cost, 7)))
        self.ui.coordsLabel.setText("x: {0}\ny: {1}".format(round(self.genetic.population[0].x, 7), round(self.genetic.population[0].y, 7)))
        self.steps.append((round(self.genetic.population[0].x, 7), round(self.genetic.population[0].y, 7)))

    def draw(self):
        f = paint_function(self.LIMIT_X, self.LIMIT_Y, self.function, self.steps)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(f.name))
        self.ui.graphicsView_2.setScene(scene)
        f.close()
        os.unlink(f.name)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Optymalizacja()
    myapp.show()
    sys.exit(app.exec_())
