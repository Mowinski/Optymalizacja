__author__ = 'Kamil'
from random import random, randint, uniform, expovariate, gauss
from functions import to_bin

class Chromosome:

    def __init__(self, *args):
        self.x = list(args)
        self.cost = None

    def getValue(self, min_x, max_x, i):
        x = int(self.x[i], 2)
        n = len(self.x[i])
        return min_x + (max_x - min_x) * x / (2**n + 1)

    def getValues(self, range):
        ret = []
        i = 0
        for x in self.x:
            n = len(x)
            x = int(x, 2)
            ret.append(range[i][0] + (range[i][1] - range[i][0]) * x / (2**n + 1))
            i += 1
        return ret

    def setCost(self, cost):
        self.cost = float(cost)

    def __len__(self):
        return len(self.x)

    def __str__(self):
        return "{0}".format(self.x)

class Genetic:
    """ Desc
    """

    def __init__(self, Fd, Fselection, Fmutation, strategy, mi, lambd, range, m, chance):
        self.Fd = Fd # Funkcja celu
        self.selection =  Fselection # Funkcja selekcji
        self.mutation = Fmutation
        self.range = range
        self.population = []
        self.mi = int(mi)
        self.lambd = int(lambd)
        self.mutation_chance = chance / 100.0
        if strategy == 'genetic':
            self.strategy = self.genetic
        elif strategy == 'two':
            self.strategy = self.two
        elif strategy == 'mi_lambda':
            self.strategy = self.mi_lambda
        elif strategy == 'mi_plus_lambda':
            self.strategy = self.mi_plus_lambda
        self.N = 36
        self.m = m
        self.randPopulation(self.mi)


    def randPopulation(self, count):
        for i in range(count):
            x = []
            for j in range(self.m):
                x.append(self.random_chromosome())
            c = Chromosome(*x)
            c.setCost(self.Fd(*c.getValues(self.range)))
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
            self.mutation(c1, self.mutation_chance, iter)
            self.mutation(c2, self.mutation_chance, iter)
            c1.setCost(self.Fd(*c1.getValues(self.range)))
            c2.setCost(self.Fd(*c2.getValues(self.range)))
            new_population.append(c1)
            new_population.append(c2)
        return new_population

    def two(self, iter):
        new_population = []
        for chrom in self.population:
            tmp = []
            for i in range(len(chrom)):
                r = randint(-2**36, 2**36)
                tmp.append(to_bin(chrom.getValue(self.range[i][0], self.range[i][1], i) + r))
            c = Chromosome(*tmp)
            c.setCost(self.Fd(*c.getValues(self.range)))
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
            self.mutation(c1, self.mutation_chance, iter)
            self.mutation(c2, self.mutation_chance, iter)
            c1.setCost(self.Fd(*c1.getValues(self.range)))
            c2.setCost(self.Fd(*c2.getValues(self.range)))
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
            self.mutation(c1, self.mutation_chance, iter)
            self.mutation(c2, self.mutation_chance, iter)
            c1.setCost(self.Fd(*c1.getValues(self.range)))
            c2.setCost(self.Fd(*c2.getValues(self.range)))
            new_population.append(c1)
            new_population.append(c2)
            new_population.append(self.population[par1])
            new_population.append(self.population[par2])
        if self.lambd > self.mi:
            new_population = sorted(new_population, key=lambda c: c.cost)[0:self.mi]
        return new_population