import unittest

class Submarino(object):

    def __init__(self):
        #
        # 0 norte, 1 leste, 2 sul, 3 oeste
        #
        self.posicionamento = 0
        self.profundidade   = 0

    # def coordenada(self, comando=''):
    #     return '0 0 0 NORTE'
        # return '2 3 -2 SUL'

    def movimentar(self, comando=''):
        if (comando == 'L' or comando == 'R'):
            self.virar(comando)
        elif (comando == 'U' or comando == 'D'):
            self.profundidade(comando)
        else:
            self.andar(comando)


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

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())

    def testVirarDireitaEsquerda(self):
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




if __name__ == '__main__':
    unittest.main()