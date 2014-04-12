__author__ = 'Kamil'
import matplotlib
matplotlib.use("Agg")
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

def simple(x, y):
    return x*x+y*y

def float_to_bin(x):
    if x < 0:
        ret = '-'
        x *= -1
    else:
        ret = ''
    for i in [6, 5, 4, 3, 2, 1, 0]:
        tmp = x / 2**i;
        if tmp > 1:
            ret += '1'
            x -= 2**i
        else:
            ret += '0'
    for i in range(30):
        x *= 2
        if x >= 1:
            ret += '1'
            x -= 1
        else:
            ret += '0'
    return ret


def bin_to_float(x):
    if x[0] == '-':
        x = [x[1:8], x[8:]]
        ret = int(x[0], 2)
        diff = 1
    else:
        x = [x[0:7], x[7:]]
        ret = int(x[0], 2)
        diff = 0
    for i in range(diff, len(x[1])):
        ret += int(x[1][i-diff]) * 0.5 ** (i+1-diff)
    ret *= -1*diff
    return ret