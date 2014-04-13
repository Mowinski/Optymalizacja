__author__ = 'Kamil'
from random import random, randint
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

    def setCost(self, cost):
        self.cost = float(cost)

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
    COUNT_POPULATION = 10
    MUTATION_CHANCE = 0.1

    def __init__(self, Fd, Fselection, Fmutation):
        self.Fd = Fd # Funkcja celu
        self.selection =  Fselection # Funkcja selekcji
        self.mutation = Fmutation
        self.population = []
        self.randPopulation(self.COUNT_POPULATION)

    def randPopulation(self, count):
        for i in range(count):
            x = (random() - 0.5) * 2
            y = (random() - 0.5) * 2
            c = Chromosome(x, y)
            c.setCost(self.Fd(x, y))
            self.population.append(c)

    def sort(self):
        self.population = sorted(self.population, key=lambda c: c.cost)

    def newEpoch(self, iter):
        newpopulation = []
        for i in range(1, int(len(self.population)/2), 2):
            c1, c2 = self.selection(self.population[i-1], self.population[i])
            self.mutation(c1, self.MUTATION_CHANCE, iter)
            self.mutation(c2, self.MUTATION_CHANCE, iter)
            c1.setCost(self.Fd(c1.x, c1.y))
            c2.setCost(self.Fd(c2.x, c2.y))
            newpopulation.append(c1)
            newpopulation.append(c2)
            newpopulation.append(self.population[i-1])
            newpopulation.append(self.population[i])
        self.population = newpopulation
        self.sort()