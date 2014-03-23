__author__ = 'Kamil'
from matplotlib import pyplot as plt
from tempfile import NamedTemporaryFile
import numpy


def paint_function(limit_x, limit_y, function, count=1000):
  X,Y = numpy.meshgrid(numpy.linspace(limit_x[0], limit_x[1], count),
                       numpy.linspace(limit_y[0], limit_y[1], count))
  Z = function(X, Y)
  plt.figure()
  plt.contourf(X, Y, Z)
  f = NamedTemporaryFile(delete=False)
  plt.savefig(f)
  return f

def rosenbrock(x, y):
    return (1-x**2)+100*(y-x**2)**2


def geem(x, y):
    return 4*x**2-2.1*x**4+(x**6)/3+x*y-4*y**2+4*y**4


def ackley(x, y):
    return -20*numpy.exp(-0.2*numpy.sqrt(0.5)*(x**2+y**2))\
           -numpy.exp(0.5*(numpy.cos(2*numpy.pi*x) + numpy.cos(2*numpy.pi+y)))


def restring(x, y):
    return (x**2-numpy.cos(18*x)) + (y**2-numpy.cos(18*y))


def goldstein(x, y):
    return ((1+(x+y+1)**2)*(19-14*x+3*x**2-14**y+6*x*y+3*y**2))\
           *((30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)))