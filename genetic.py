from bisect import insort_right

__author__ = 'Kamil'
from random import random, randint

class Chromosome:
    def __init__(self, x, y):
        self.x = float(x)
        self.xc = str(x)
        self.y = float(y)
        self.yc = str(y)
        self.cost = None

    def mix_simple(self, other):
        tmp = randint(3, len(other.xc)-1)
        ret1 = Chromosome(self.xc[0:tmp] + other.xc[tmp:], self.yc[0:tmp] + other.yc[tmp:])
        ret2 = Chromosome(other.xc[0:tmp] + self.xc[tmp:], other.yc[0:tmp] + self.yc[tmp:])
        return ret1, ret2

    def setCost(self, cost):
        self.cost = float(cost)

    def __str__(self):
        return "({0} {1})".format(self.x, self.y)

    def __repr__(self):
        return str(self.cost)

class Genetic:
    """ Desc
    """
    def __init__(self, Fd, Fselection, Fcrossing):
        self.Fd = Fd # Funkcja celu
        self.selection =  Fselection # Funkcja selekcji
        self.crossing = Fcrossing
        self.population = []
        self.randPopulation(100)

    def randPopulation(self, count):
        for i in range(count):
            x = (random() - 0.5) * 2
            y = (random() - 0.5) * 2
            c = Chromosome(x, y)
            c.setCost(self.Fd(x, y))
            self.population.append(c)

    def sort(self):
        self.population = sorted(self.population, key=lambda c: c.cost)

    def newEpoch(self):
        newpopulation = []
        for i in range(1, int(len(self.population)/2), 2):
            c1, c2 = self.population[i-1].mix_simple(self.population[i])
            c1.setCost(self.Fd(c1.x, c1.y))
            c2.setCost(self.Fd(c2.x, c2.y))
            newpopulation.append(c1)
            newpopulation.append(c2)
            newpopulation.append(self.population[i-1])
            newpopulation.append(self.population[i])
        self.population = newpopulation