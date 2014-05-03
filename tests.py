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
        g = Genetic(rosenbrock, None, None, [-5, 5], [-5, 5])
        for pop in g.population:
            print(pop.getValueX(-5, 5), pop.getValueY(-5, 5))
        pass

    def test_chromosome(self):
        c = Chromosome('1111111111', '0000000000')
        print(c.getValueX(-5, 5), c.getValueY(-5, 5))
        c = Chromosome('1100110011', '0010011110')
        print(c.getValueX(-5, 5), c.getValueY(-5, 5))

    def test_floattobin(self):
        f = -15.125
        b = float_to_bin(f)
        fb = bin_to_float(b)
        self.assertEqual(f, fb)

if __name__ == '__main__':
    unittest.main()