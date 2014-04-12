__author__ = 'Kamil'
from window import MainForm
from PyQt4 import QtGui, QtCore, QtOpenGL
from functions import paint_function, rosenbrock, geem, ackley, restring, goldstein, simple
import sys, os
from genetic import Genetic
class Optymalizacja(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MainForm()
        self.ui.setupUi(self)
        self.genetic = Genetic(rosenbrock, None, None)
        self.genetic.randPopulation(10)
        self.epochNumber = 0
        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL("clicked()"), self.calculate)
        QtCore.QObject.connect(self.ui.stepButton, QtCore.SIGNAL("clicked()"), self.epoch)

    def calculate(self):
        if self.ui.function_rosenbrock_2.isChecked():
            function = rosenbrock
        elif self.ui.function_akley_2.isChecked():
            function = ackley
        elif self.ui.function_gem_2.isChecked():
            function = geem
        elif self.ui.function_golstein_2.isChecked():
            function = goldstein
        elif self.ui.function_rastring_2.isChecked():
            function = restring
        else:
            raise TypeError('Not selected function')
        f = paint_function([-2, 2], [-2, 2], function)
        self.genetic.Fd = function
        self.ui.graphicsView_2.setViewport(QtOpenGL.QGLWidget())
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(f.name))
        self.ui.graphicsView_2.setScene(scene)
        f.close()
        os.unlink(f.name)
        self.epochNumber = 0

    def epoch(self):
        for i in range(10):
            self.genetic.sort()
            self.genetic.newEpoch(0.01)
            self.epochNumber += 1
            self.ui.epochNumber.display(self.epochNumber)
            self.genetic.sort()
            self.ui.targetLabel.setText(str(round(self.genetic.population[0].cost, 7)))
            self.ui.coordsLabel.setText("x: {0}\ny: {1}".format(round(self.genetic.population[0].x, 7), round(self.genetic.population[0].y, 7)))
            print(self.genetic.population[0])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Optymalizacja()
    myapp.show()
    sys.exit(app.exec_())
