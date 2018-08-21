import unittest

class Submarino(object):

    def __init__(self):
        self.direcao = {'id': 0, 'label': 'NORTE'}

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

    def virar_direita(self):
        direcao_atual = self.direcao['id']
        nova_direcao = 0 if direcao_atual == 3 else direcao_atual + 1
        self.direcao = self.ret_direcao(nova_direcao)
        return nova_direcao

    def virar_esquerda(self):
        direcao_atual = self.direcao['id']
        nova_direcao = 3 if direcao_atual == 0 else direcao_atual - 1
        self.direcao = self.ret_direcao(nova_direcao)
        return nova_direcao

    def ret_direcao(self, id):
        direcoes = [
            {'id': 0, 'label': 'NORTE'},
            {'id': 1, 'label': 'LESTE'},
            {'id': 2, 'label': 'SUL'},
            {'id': 3, 'label': 'OESTE'}
        ]
        return direcoes[id]




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
        self.assertEqual(0, sub.direcao['id'])
        self.assertEqual(3, sub.virar_esquerda())
        self.assertEqual(0, sub.virar_direita())
        self.assertEqual(1, sub.virar_direita())
        self.assertEqual(2, sub.virar_direita())

if __name__ == '__main__':
    unittest.main()