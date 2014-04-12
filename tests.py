__author__ = 'Kamil'
import unittest
from genetic import Chromosome, Genetic
from functions import rosenbrock, float_to_bin, bin_to_float

class TestGeneric(unittest.TestCase):

    def test_function(self):
        pass

    def test_chromosome(self):
        c1 = Chromosome(1.121, 0.121)
        c2 = Chromosome(0.412, 1.231)
        r1, r2 = c1.mix_simple(c2)

    def test_random(self):
        #g = Genetic(rosenbrock, None, None)
        #g.randPopulation(100)
        #for i in range(100):
        #    g.sort()
        #    g.newEpoch(0.1)
        pass

    def test_chromosome(self):
        pass

    def test_floattobin(self):
        f = -15.125
        b = float_to_bin(f)
        fb = bin_to_float(b)
        self.assertEqual(f, fb)

if __name__ == '__main__':
    unittest.main()