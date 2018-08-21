import unittest

class Submarino(object):

    def __init__(self):
        self.posicionamento = 0 # 0 norte, 1 leste, 2 sul, 3 oeste
        self.profundidade   = 0 # 0 = superfície
        self.x = 0
        self.y = 0
        self.z = 0

    def coordenada(self, comando=''):
        direcao = ['NORTE', 'LESTE', 'SUL', 'OESTE']
        posicionamento = direcao[self.posicionamento]
        return "%s %s %s %s" % (self.x, self.x, self.z, posicionamento)

    def movimentar(self):
        # Todo movimento quando o submarino estiver apontando para o NORTE,
        # somará 1 ao eixo Y
        if (self.posicionamento == 0):
            self.y += 1
        else:
            self.y -= 1

        # Todo movimento quando o submarino estiver apontando para o LESTE
        # somará 1 ao eixo X
        if (self.posicionamento == 1):
            self.x += 1
        else:
            self.x -= 1

        return True

    def right(self):
        self.posicionamento = 0 if self.posicionamento == 3 else self.posicionamento + 1
        return self.posicionamento

    def left(self):
        self.posicionamento = 3 if self.posicionamento == 0 else self.posicionamento - 1
        return self.posicionamento

    def up(self):
        self.profundidade = 0 if self.profundidade == 0 else self.profundidade + 1
        return self.profundidade

    def down(self):
        self.profundidade = self.profundidade - 1
        return self.profundidade


class SubmarinoTest(unittest.TestCase):

    # def testcoordenada(self):
    #     sub = Submarino()
    #     self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

    def testPosicaoInicial(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.coordenada())

    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.posicionamento)
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    def testProfundidade(self):
        sub = Submarino()
        self.assertEqual(0, sub.profundidade)
        self.assertEqual(0, sub.up())
        self.assertEqual(-1, sub.down())
        self.assertEqual(-2, sub.down())
        self.assertEqual(-3, sub.down())
        self.assertEqual(-2, sub.up())

    def testMovimentoNorte(self):
        sub = Submarino()
        sub.posicionamento = 0 # norte

        sub.movimentar()
        self.assertEqual(1, sub.y)

        sub.movimentar()
        self.assertEqual(2, sub.y)

        sub.movimentar()
        self.assertEqual(3, sub.y)

    def testMovimentoLeste(self):
        sub = Submarino()
        sub.posicionamento = 1 # leste

        sub.movimentar()
        self.assertEqual(1, sub.x)

        sub.movimentar()
        self.assertEqual(2, sub.x)

        sub.movimentar()
        self.assertEqual(3, sub.x)

    def testMovimentoSul(self):
        sub = Submarino()
        sub.posicionamento = 2 # Sul

        sub.movimentar()
        self.assertEqual(-1, sub.y)

        sub.movimentar()
        self.assertEqual(-2, sub.y)

        sub.movimentar()
        self.assertEqual(-3, sub.y)

    def testMovimentoOeste(self):
        sub = Submarino()
        sub.posicionamento = 3 # oeste

        sub.movimentar()
        self.assertEqual(-1, sub.x)

        sub.movimentar()
        self.assertEqual(-2, sub.x)

        sub.movimentar()
        self.assertEqual(-3, sub.x)


if __name__ == '__main__':
    unittest.main()