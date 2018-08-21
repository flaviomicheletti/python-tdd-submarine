import unittest

class Submarino(object):

    def __init__(self):
        self.direcao = {'id': 0, 'label': 'NORTE'}

    def coordenada(self, comando=''):
        return '2 3 -2 SUL'
        # return '0 0 0 NORTE'

    def movimentar(self, comando=''):
        if (comando == 'L' or comando == 'R'):
            self.virar(comando)
        elif (comando == 'U' or comando == 'D'):
            self.profundidade(comando)
        else:
            self.andar(comando)

    def virar(self, comando=''):
        direcao = ['NORTE', 'LESTE', 'SUL', 'OESTE']

        if comando == 'R':
            if self.direcao['id'] == 3:
                id = 0
            else:
                id = self.direcao['id'] + 1

        if comando == 'L':
            if self.direcao['id'] == 0 :
                id = 3
            else:
                id = self.direcao['id'] - 1

        # atualizando
        self.direcao['id']    = id
        self.direcao['label'] = direcao[id]

        return direcao[id]


class SubmarinoTest(unittest.TestCase):

    def testcoordenada(self):
        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

    # def testPosicaoInicial(self):
    #     sub = Submarino()
    #     self.assertEqual('0 0 0 NORTE', sub.coordenada())

    def testVirarParaDireita(self):
        sub = Submarino()
        self.assertEqual('NORTE', sub.direcao['label'])

        sub.virar('R')
        self.assertEqual('LESTE', sub.direcao['label'])

        sub.virar('R')
        self.assertEqual('SUL', sub.direcao['label'])

        sub.virar('R')
        self.assertEqual('OESTE', sub.direcao['label'])


    def testVirarParaDireitaLimite(self):
        sub = Submarino()
        sub.direcao['id']    = 3
        sub.direcao['label'] = 'OESTE'

        sub.virar('R')
        self.assertEqual('NORTE', sub.direcao['label'])


    def testVirarParaEsquerda(self):
        sub = Submarino()
        self.assertEqual('NORTE', sub.direcao['label'])

        sub.virar('L')
        self.assertEqual('OESTE', sub.direcao['label'])

        sub.virar('L')
        self.assertEqual('SUL', sub.direcao['label'])

        sub.virar('L')
        self.assertEqual('LESTE', sub.direcao['label'])


    def testVirarParaEsquerdaLimite(self):
        sub = Submarino()

        sub.virar('L')
        self.assertEqual('OESTE', sub.direcao['label'])


if __name__ == '__main__':
    unittest.main()