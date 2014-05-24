__author__ = 'Kamil'
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from tempfile import NamedTemporaryFile
from random import randint, random
import numpy


def paint_function(limits, function, steps=None, count=1000):
  X,Y = numpy.meshgrid(numpy.linspace(limits[0][0], limits[0][1], count),
                       numpy.linspace(limits[1][0], limits[1][1], count))
  Z = function(X, Y)
  plt.figure()
  plt.contourf(X, Y, Z)
  if steps:
      for step in steps:
          plt.plot(step[0], step[1], 'ro')
  f = NamedTemporaryFile(delete=False)
  plt.savefig(f)
  return f

def rosenbrock(*args):
    return (1-args[0]**2)+(args[1]-args[0]**2)**2


def geem(*args):
    return 4*args[0]**2-2.1*args[0]**4+(args[0]**6)/3+args[0]*args[1]-4*args[1]**2+4*args[1]**4


def ackley(*args):
    return -20*numpy.exp(-0.2*numpy.sqrt(0.5)*(args[0]**2+args[1]**2))\
           -numpy.exp(0.5*(numpy.cos(2*numpy.pi*args[1]) + numpy.cos(2*numpy.pi+args[0])))


def restring(*args):
    return (args[0]**2-numpy.cos(18*args[0])) + (args[1]**2-numpy.cos(18*args[1]))


def goldstein(*args):
    return (1+((args[0]+args[1]+1)**2)*(19-14*args[0]+3*args[1]**2-14*args[0]+6*args[0]*args[1]+3*args[1]**2))*(30+((2*args[0]-3*args[1])**2)*(18-32*args[1]+12*args[0]**2+48*args[1]-36*args[0]*args[1]+27*args[0]**2))


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
    tmp, tmp2 = [], []
    for i in range(len(first)):
        t = randint(0, min(len(first.x[i]), len(other.x[i])))
        tmp.append(first.x[i][0:t] + other.x[i][t:])
        tmp2.append(other.x[i][0:t] + first.x[i][t:])
    ret1 = Chromosome(*tmp)
    ret2 = Chromosome(*tmp2)
    return ret1, ret2


def aritmic_selection(first, other):
    from genetic import Chromosome
    tmp, tmp2 = [], []
    for i in range(len(first)):
        alfa = random()
        fx = int(first.x[i], 2)
        ox = int(other.x[i], 2)
        tmp.append(to_bin(fx * alfa + (1 - alfa) * ox))
        tmp2.append(to_bin((1 - alfa) * fx + alfa * ox))
    ret1 = Chromosome(*tmp)
    ret2 = Chromosome(*tmp2)
    return ret1, ret2


# Mutetion
def mutation(chrom, chance, i):
    tmp = random()
    if tmp <= chance:
        gen = randint(0, len(chrom)-1)
        i = randint(0, len(chrom.x[gen])-1)
        chrom.x[gen] = chrom.x[gen][:i] + ('0' if chrom.x[gen][i] == '1' else '1') + chrom.x[gen][i+1:]


def mutation_nonlinear(chrom, chance, iter):
    c = 2
    delta = lambda t, y: y * (1 - random() ** ((1 - t / 100) * c))
    if random() < chance:
        gen = randint(0, len(chrom)-1)
        if random() > 0.5:
            chrom.x[gen] = to_bin(int(chrom.x[gen], 2) + delta(iter, 5 - int(chrom.x[gen], 2)))
        else:
            chrom.x[gen] = to_bin(int(chrom.x[gen], 2) - delta(iter, 5 - int(chrom.x[gen], 2)))