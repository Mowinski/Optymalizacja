__author__ = 'Kamil'
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from tempfile import NamedTemporaryFile
from random import randint, random
import numpy


def paint_function(limit_x, limit_y, function, steps=None, count=1000):
  X,Y = numpy.meshgrid(numpy.linspace(limit_x[0], limit_x[1], count),
                       numpy.linspace(limit_y[0], limit_y[1], count))
  Z = function(X, Y)
  plt.figure()
  plt.contourf(X, Y, Z)
  if steps:
      for step in steps:
          plt.plot(step[0], step[1], 'ro')
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
    return (1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))


def to_bin(x):
    if x < 0:
        ret = '-'
        x *= -1
    else:
        ret = ''
    for i in sorted(range(36), reverse=True):
        tmp = x / 2**i
        if tmp > 1:
            ret += '1'
            x -= 2**i
        else:
            ret += '0'
    return ret


# Selection
def mix_simple(first, other):
    from genetic import Chromosome
    tmp = randint(0, min(len(first.x), len(other.x)))
    tmp2 = randint(0, min(len(first.y), len(other.y)))
    ret1 = Chromosome((first.x[0:tmp] + other.x[tmp:]), (first.y[0:tmp2] + other.y[tmp2:]))
    ret2 = Chromosome((other.x[0:tmp] + first.x[tmp:]), (other.y[0:tmp2] + first.y[tmp2:]))
    return ret1, ret2


def aritmic_selection(first, other):
    from genetic import Chromosome
    alfa = random()
    fx, fy = int(first.x, 2), int(first.y, 2)
    ox, oy = int(other.x, 2), int(other.y, 2)
    ret1 = Chromosome(to_bin(fx * alfa + (1 - alfa) * ox), to_bin(fy * alfa + (1 - alfa) * oy))
    ret2 = Chromosome(to_bin((1 - alfa) * fx + alfa * ox), to_bin((1 - alfa) * fy + alfa * oy))
    return ret1, ret2


# Mutetion
def mutation(chrom, chance, i):
    tmp = random()
    if tmp <= chance:
        i = randint(0, min(len(chrom.x), len(chrom.y))-1)
        if random() > 0.5:
            chrom.x = chrom.x[:i] + ('0' if chrom.x[i] == '1' else '1') + chrom.x[i+1:]
        else:
            chrom.y = chrom.y[:i] + ('0' if chrom.y[i] == '1' else '1') + chrom.y[i+1:]


def mutation_nonlinear(chrom, chance, iter):
    c = 2
    delta = lambda t, y: y * (1 - random() ** ((1 - t / 100) * c))
    if random() < chance:
        if random() > 0.5:
            if random() > 0.5:
                chrom.x = to_bin(int(chrom.x, 2) + delta(iter, 5 - int(chrom.x, 2)))
            else:
                chrom.y = to_bin(int(chrom.y, 2) + delta(iter, 5 - int(chrom.y, 2)))
        else:
            if random() > 0.5:
                chrom.x = to_bin(int(chrom.x, 2) - delta(iter, 5 - int(chrom.x, 2)))
            else:
                chrom.y = to_bin(int(chrom.y, 2) - delta(iter, 5 - int(chrom.y, 2)))