import unittest

from G import G


class GTest(unittest.TestCase):
    def setUp(self) -> None:
        self.G = G({'A', 'S'},
                   {'b', 'c', 'a'},
                   {'S': [['aAbS', 1], ['b', 2]], 'A': [['SAc', 3], ['e', 4]]},
                   "S")
        print(self.G.N)
        print(self.G.A)
        print(self.G.P)
        print(self.G.S)

    def test_peretty_prit(self):
        print(self.G)

    def test_left(self):
        self.G.left_vivod()


if __name__ == '__main__':
    unittest.main()
