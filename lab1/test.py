import unittest

from G import G
S->SAS
S->A
A->aA
A->AB
A->b
B->bB
B->bBaB
B->a

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

    def test_two_task(self):
        print(self.G.check_left_rules([1, 3, 2, 1, 4]))

    def test_three_task(self):
        print(self.G.check_rules([1, 3, 2, 1, 4]))
if __name__ == '__main__':
    unittest.main()
