__author__ = 'Kamil'
from random import random, randint, uniform, expovariate, gauss
from functions import to_bin

class Chromosome:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.cost = None

    def getValueX(self, min_x, max_x):
        x = int(self.x, 2)
        n = len(self.x)
        return min_x + (max_x - min_x) * x / (2**n + 1)

    def getValueY(self, min_y, max_y):
        y = int(self.y, 2)
        n = len(self.y)
        return min_y + (max_y - min_y) * y / (2**n + 1)

    def setCost(self, cost):
        self.cost = float(cost)

    def __str__(self):
        return "({0} {1})".format(self.x, self.y)

    def __repr__(self):
        return "({0} {1}) : {2}".format(self.x, self.y, self.cost)


class Genetic:
    """ Desc
    """
    MUTATION_CHANCE = 0.01

    def __init__(self, Fd, Fselection, Fmutation, strategy, mi, lambd, rangex, rangey):
        self.Fd = Fd # Funkcja celu
        self.selection =  Fselection # Funkcja selekcji
        self.mutation = Fmutation
        self.rangex = rangex
        self.rangey = rangey
        self.population = []
        self.mi = int(mi)
        self.lambd = int(lambd)
        if strategy == 'genetic':
            self.strategy = self.genetic
        elif strategy == 'two':
            self.strategy = self.two
        elif strategy == 'mi_lambda':
            self.strategy = self.mi_lambda
        elif strategy == 'mi_plus_lambda':
            self.strategy = self.mi_plus_lambda
        self.N = 36
        self.randPopulation(self.mi)


    def randPopulation(self, count):
        for i in range(count):
            x = self.random_chromosome()
            y = self.random_chromosome()
            c = Chromosome(x, y)
            c.setCost(self.Fd(c.getValueX(self.rangex[0], self.rangex[1]), c.getValueY(self.rangey[0], self.rangey[1])))
            self.population.append(c)

    def random_chromosome(self):
        ret = ''
        for i in range(self.N):
            ret += '1' if random() > 0.5 else '0'
        return ret

    def sort(self):
        self.population = sorted(self.population, key=lambda c: c.cost)

    def newEpoch(self, iter):
        self.population = self.strategy(iter)
        self.sort()

    def genetic(self, iter):
        new_population = []
        for i in range(0, self.mi // 2):
            index = int(expovariate(1) * 10) % self.mi
            index2 = randint(0, self.mi-1)
            c1, c2 = self.selection(self.population[index], self.population[index2])
            self.mutation(c1, self.MUTATION_CHANCE, iter)
            self.mutation(c2, self.MUTATION_CHANCE, iter)
            c1.setCost(self.Fd(c1.getValueX(self.rangex[0], self.rangex[1]), c1.getValueY(self.rangey[0], self.rangey[1])))
            c2.setCost(self.Fd(c2.getValueX(self.rangex[0], self.rangex[1]), c2.getValueY(self.rangey[0], self.rangey[1])))
            new_population.append(c1)
            new_population.append(c2)
        return new_population

    def two(self, iter):
        new_population = []
        for chrom in self.population:
            randx = randint(-2**36, 2**36)
            randy = randint(-2**36, 2**36)
            c = Chromosome(to_bin(int(chrom.x, 2) + randx),
                           to_bin(int(chrom.y, 2) + randy))
            c.setCost(self.Fd(c.getValueX(self.rangex[0], self.rangex[1]),
                              c.getValueY(self.rangey[0], self.rangey[1])))
            if c.cost < chrom.cost:
                new_population.append(c)
            else:
                new_population.append(chrom)
        return new_population

    def mi_lambda(self, iter):
        new_population = []
        for i in range(self.lambd):
            par1, par2 = randint(0, self.mi-1), randint(0, self.mi-1)
            while par1 == par2:
                par1, par2 = randint(0, self.mi-1), randint(0, self.mi-1)
            c1, c2 = self.selection(self.population[par1], self.population[par2])
            self.mutation(c1, self.MUTATION_CHANCE, iter)
            self.mutation(c2, self.MUTATION_CHANCE, iter)
            c1.setCost(self.Fd(c1.getValueX(self.rangex[0], self.rangex[1]), c1.getValueY(self.rangey[0], self.rangey[1])))
            c2.setCost(self.Fd(c2.getValueX(self.rangex[0], self.rangex[1]), c2.getValueY(self.rangey[0], self.rangey[1])))
            new_population.append(c1)
            new_population.append(c2)
        if self.lambd > self.mi:
            new_population = sorted(new_population, key=lambda c: c.cost)[0:self.mi]
        return new_population

    def mi_plus_lambda(self, iter):
        new_population = []
        for i in range(self.mi + self.lambd):
            par1, par2 = randint(0, self.mi-1), randint(0, self.mi-1)
            while par1 == par2:
                par1, par2 = randint(0, self.mi-1), randint(0, self.mi-1)
            c1, c2 = self.selection(self.population[par1], self.population[par2])
            self.mutation(c1, self.MUTATION_CHANCE, iter)
            self.mutation(c2, self.MUTATION_CHANCE, iter)
            c1.setCost(self.Fd(c1.getValueX(self.rangex[0], self.rangex[1]), c1.getValueY(self.rangey[0], self.rangey[1])))
            c2.setCost(self.Fd(c2.getValueX(self.rangex[0], self.rangex[1]), c2.getValueY(self.rangey[0], self.rangey[1])))
            new_population.append(c1)
            new_population.append(c2)
            new_population.append(self.population[par1])
            new_population.append(self.population[par2])
        if self.lambd > self.mi:
            new_population = sorted(new_population, key=lambda c: c.cost)[0:self.mi]
        return new_population

    def genetic_select(self, iter):
        pass