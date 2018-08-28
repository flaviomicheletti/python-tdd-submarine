import unittest

class Submarino(object):

    def coordenada(self, comando=''):
        return '2 3 -2 SUL'


class SubmarinoTest(unittest.TestCase):

    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

        sub = Submarino()
        self.assertEqual('-1 2 0 NORTE', sub.coordenada("LMRDDMMUU"))

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())


if __name__ == '__main__':
    unittest.main()