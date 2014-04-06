__author__ = 'Kamil'
import unittest
from genetic import Chromosome, Genetic
from functions import rosenbrock

class TestGeneric(unittest.TestCase):

    def test_function(self):
        print(rosenbrock(-1.941553467769264, 3.935348520369992)) #0.023362700730180652

    def test_chromosome(self):
        c1 = Chromosome(1.121, 0.121)
        c2 = Chromosome(0.412, 1.231)
        r1, r2 = c1.mix_simple(c2)
        print(r1, r2)

    def test_random(self):
        g = Genetic(rosenbrock, None, None)
        g.randPopulation(1000)
        for i in range(1000):
            g.sort()
            g.newEpoch(0.1)
        print(g.population[0].cost, g.population[0])


if __name__ == '__main__':
    unittest.main()