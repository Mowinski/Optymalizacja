__author__ = 'Kamil'
from window import MainForm
from PyQt4 import QtGui, QtCore, QtOpenGL
from functions import paint_function, rosenbrock, geem, ackley, restring, goldstein
import sys, os

class Optymalizacja(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MainForm()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL("clicked()"), self.calculate)

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
        self.ui.graphicsView_2.setViewport(QtOpenGL.QGLWidget())
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
