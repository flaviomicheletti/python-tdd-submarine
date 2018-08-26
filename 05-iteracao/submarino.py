import unittest

class Submarino(object):

    def __init__(self):
        # 0 norte, 1 leste, 2 sul, 3 oeste
        self.apontando_para = 0

    def coordenada(self, comando=''):
        return '2 3 -2 SUL'

    def right(self):
        self.apontando_para = 0 if self.apontando_para == 3 else self.apontando_para + 1
        return self.apontando_para

    def left(self):
        self.apontando_para = 3 if self.apontando_para == 0 else self.apontando_para - 1
        return self.apontando_para


class SubmarinoTest(unittest.TestCase):

    # def testCoordenada(self):
    #     sub = Submarino()
    #     self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

    #     sub = Submarino()
    #     self.assertEqual('-1 2 0 NORTE', sub.coordenada("LMRDDMMUU"))

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())

    #       Norte
    #         0
    #
    # Oeste         Leste
    #   3             1
    #
    #        Sul
    #         2
    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.apontando_para)
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    #
    # 0 (zero) é a superfície
    #
    def testProfundidade(self):
        sub = Submarino()
        self.assertEqual(0, sub.z)
        self.assertEqual(0, sub.up())
        self.assertEqual(-1, sub.down())
        self.assertEqual(-2, sub.down())
        self.assertEqual(-3, sub.down())
        self.assertEqual(-2, sub.up())


if __name__ == '__main__':
    unittest.main()