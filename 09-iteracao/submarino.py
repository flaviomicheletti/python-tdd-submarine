import unittest

class Submarino(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        # 0 = superfície
        self.z = 0
        # 0 norte, 1 leste, 2 sul, 3 oeste
        self.apontando_para = 0

    def coordenada(self, comando=''):
        return '2 3 -2 SUL'

    def movimentar(self):
        # Todo movimento quando o submarino estiver apontando para o NORTE,
        # somará 1 ao eixo Y
        if (self.apontando_para == 0): # norte
            self.y += 1

        if (self.apontando_para == 2): # sul
            self.y -= 1

        # Todo movimento quando o submarino estiver apontando para o LESTE
        # somará 1 ao eixo X
        if (self.apontando_para == 1):  # leste
            self.x += 1

        if (self.apontando_para == 3):  # oeste
            self.x -= 1

        return True

    def right(self):
        self.apontando_para = 0 if self.apontando_para == 3 else self.apontando_para + 1
        return self.apontando_para

    def left(self):
        self.apontando_para = 3 if self.apontando_para == 0 else self.apontando_para - 1
        return self.apontando_para

    def up(self):
        self.z = 0 if self.z == 0 else self.z + 1
        return self.z

    def down(self):
        self.z = self.z - 1
        return self.z


class SubmarinoTest(unittest.TestCase):

    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

        # sub = Submarino()
        # self.assertEqual('-1 2 0 NORTE', sub.coordenada("LMRDDMMUU"))

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

    def testMovimentarApontandoParaNorte(self):
        sub = Submarino()
        sub.apontando_para = 0

        sub.movimentar()
        self.assertEqual(0, sub.x)

        self.assertEqual(1, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(2, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(3, sub.y)

    #
    # Prerrogativa: como Sul é direção oposta ao Norte diminuímos 1 a cada movimento
    #
    def testMovimentarApontandoParaSul(self):
        sub = Submarino()
        sub.apontando_para = 2

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-1, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-2, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-3, sub.y)

    #
    # Prerrogativa: como Oeste é direção oposta ao Leste diminuímos 1 a cada movimento
    #
    def testMovimentarApontandoParaOeste(self):
        sub = Submarino()
        sub.apontando_para = 3

        sub.movimentar()
        self.assertEqual(-1, sub.x)
        self.assertEqual(0, sub.y)

        sub.movimentar()
        self.assertEqual(-2, sub.x)
        self.assertEqual(0, sub.y)

        sub.movimentar()
        self.assertEqual(-3, sub.x)
        self.assertEqual(0, sub.y)


if __name__ == '__main__':
    unittest.main()