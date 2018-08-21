import unittest

class Submarino(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0 # 0 = superfície
        self.posicionamento = 0 # 0 norte, 1 leste, 2 sul, 3 oeste

    def coordenada(self, comando=''):
        for c in comando:
            if c == 'R':
                self.right()
            elif c == 'L':
                self.left()
            elif c == 'U':
                self.up()
            elif c == 'D':
                self.down()
            elif c == 'M':
                self.movimentar()

        direcao = ['NORTE', 'LESTE', 'SUL', 'OESTE']
        return "%s %s %s %s" % (self.x, self.y, self.z, direcao[self.posicionamento])

    def movimentar(self):
        # Todo movimento quando o submarino estiver apontando para o NORTE,
        # somará 1 ao eixo Y
        if (self.posicionamento == 0):
            self.y += 1
        elif (self.posicionamento == 2):
            self.y -= 1

        # Todo movimento quando o submarino estiver apontando para o LESTE
        # somará 1 ao eixo X
        if (self.posicionamento == 1):
            self.x += 1
        elif (self.posicionamento == 3):
            self.x -= 1

        return True

    def right(self):
        self.posicionamento = 0 if self.posicionamento == 3 else self.posicionamento + 1
        return self.posicionamento

    def left(self):
        self.posicionamento = 3 if self.posicionamento == 0 else self.posicionamento - 1
        return self.posicionamento

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

    def testPosicaoInicial(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.coordenada())

    def testPosicaoInicial(self):
        sub = Submarino()
        self.assertEqual('0 1 0 NORTE', sub.coordenada('M'))

    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.posicionamento)
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    def testProfundidade(self):
        sub = Submarino()
        self.assertEqual(0, sub.z)
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
        self.assertEqual(0, sub.x)

        sub.movimentar()
        self.assertEqual(2, sub.y)
        self.assertEqual(0, sub.x)

        sub.movimentar()
        self.assertEqual(3, sub.y)
        self.assertEqual(0, sub.x)

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