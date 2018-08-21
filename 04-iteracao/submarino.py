import unittest

class Submarino(object):

    def __init__(self):
        self.posicionamento = {'id': 0, 'label': 'NORTE'}

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
        direcao_atual = self.posicionamento['id']
        nova_direcao  = 0 if direcao_atual == 3 else direcao_atual + 1
        return self.definir_posicionamento(nova_direcao)

    def left(self):
        direcao_atual = self.posicionamento['id']
        nova_direcao  = 3 if direcao_atual == 0 else direcao_atual - 1
        return self.definir_posicionamento(nova_direcao)

    def definir_posicionamento(self, id):
        direcoes = [
            {'id': 0, 'label': 'NORTE'},
            {'id': 1, 'label': 'LESTE'},
            {'id': 2, 'label': 'SUL'},
            {'id': 3, 'label': 'OESTE'}
        ]
        self.posicionamento = direcoes[id]
        return id




class SubmarinoTest(unittest.TestCase):

    # def testcoordenada(self):
    #     sub = Submarino()
    #     self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())


    #
    # 0 norte, 1 leste, 2 sul, 3 oeste
    #
    def testVirarDireitaEsquerda(self):
        sub = Submarino()
        self.assertEqual(0, sub.posicionamento['id'])
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    # def testFoo(self):
    #     sub = Submarino()
    #     self.assertEqual(0, sub.posicionamento['id'])
    #     self.assertEqual(0, sub.up())
    #     self.assertEqual(-1, sub.down())
    #     self.assertEqual(-2, sub.down())
    #     self.assertEqual(-3, sub.down())
    #     self.assertEqual(-2, sub.up())




if __name__ == '__main__':
    unittest.main()