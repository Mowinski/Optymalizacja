__author__ = 'Kamil'
from random import random, randint, uniform, expovariate
from functions import bin_to_float, float_to_bin

class Chromosome:

    def __init__(self, x, y):
        self.x = float(x)
        self.xc = float_to_bin(self.x)
        self.y = float(y)
        self.yc = float_to_bin(self.y)
        self.cost = None

    def mix_simple(self, other):
        tmp = randint(0, min(len(self.xc), len(other.xc)))
        tmp2 = randint(0, min(len(self.yc), len(other.yc)))
        ret1 = Chromosome(bin_to_float(self.xc[0:tmp] + other.xc[tmp:]), bin_to_float(self.yc[0:tmp2] + other.yc[tmp2:]))
        ret2 = Chromosome(bin_to_float(other.xc[0:tmp] + self.xc[tmp:]), bin_to_float(other.yc[0:tmp2] + self.yc[tmp2:]))
        return ret1, ret2

    def setCost(self, cost, rangex=None, rangey=None):
        self.cost = float(cost)
        if rangex:
            if self.x > rangex[1] or self.x < rangex[0]:
                self.cost *= 100
            if self.y > rangey[1] or self.y < rangey[0]:
                self.cost *= 100

    def mutation(self, chance):
        if random() > chance:
            if random() > 0.5:
                self.x += random()-0.5
                self.xc = float_to_bin(self.x)
            else:
                self.y += random()-0.5
                self.yc = float_to_bin(self.y)

    def __str__(self):
        return "({0} {1}) - ({2} {3})".format(self.x, self.y, self.xc, self.yc)

    def __repr__(self):
        return str(self.cost)


class Genetic:
    """ Desc
    """
    COUNT_POPULATION = 30
    MUTATION_CHANCE = 0.01

    def __init__(self, Fd, Fselection, Fmutation, rangex, rangey):
        self.Fd = Fd # Funkcja celu
        self.selection =  Fselection # Funkcja selekcji
        self.mutation = Fmutation
        self.rangex = rangex
        self.rangey = rangey
        self.population = []
        self.strategy = self.genetic
        self.randPopulation(self.COUNT_POPULATION)

    def randPopulation(self, count):
        for i in range(count):
            x = uniform(self.rangex[0], self.rangex[1])
            y = uniform(self.rangey[0], self.rangey[1])
            c = Chromosome(x, y)
            c.setCost(self.Fd(x, y), self.rangex, self.rangey)
            self.population.append(c)

    def sort(self):
        self.population = sorted(self.population, key=lambda c: c.cost)

    def newEpoch(self, iter):
        self.population = self.strategy(iter)
        self.sort()

    def genetic(self, iter):
        new_population = []
        for i in range(0, self.COUNT_POPULATION // 2):
            index = int(expovariate(1) * 10) % self.COUNT_POPULATION
            index2 = randint(0, self.COUNT_POPULATION-1)
            c1, c2 = self.selection(self.population[index], self.population[index2])
            self.mutation(c1, self.MUTATION_CHANCE, iter)
            self.mutation(c2, self.MUTATION_CHANCE, iter)
            c1.setCost(self.Fd(c1.x, c1.y), self.rangex, self.rangey)
            c2.setCost(self.Fd(c2.x, c2.y), self.rangex, self.rangey)
            new_population.append(c1)
            new_population.append(c2)
        return new_population

    def genetic_select(self, iter):
        pass

    def inrange(self, chrom):
        if not (self.rangex[0] <= chrom.x <= self.rangex[1]):
            print(chrom.x, 'x', self.rangex)
            return False
        if not(self.rangey[0] <= chrom.y <= self.rangey[1]):
            print(chrom.y, 'y', self.rangey)
            return False
        return True