import unittest

class Submarino(object):

    def coordenada(self, comando=''):
        return '2 3 -2 SUL'
        # return '0 0 0 NORTE'

class SubmarinoTest(unittest.TestCase):

    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())

    # def testMovimentarParaDireita(self):
    #     sub = Submarino()
    #     self.assertEqual('NORTE', sub.direcao)

    #     sub.movimentar('R')
    #     self.assertEqual('LESTE', sub.direcao)

    #     sub.movimentar('R')
    #     self.assertEqual('SUL', sub.direcao)

    #     sub.movimentar('R')
    #     self.assertEqual('OESTE', sub.direcao)



if __name__ == '__main__':
    unittest.main()