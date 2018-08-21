import unittest

# Teste de programação do Buscapé
# disponível em: https://github.com/buscape-company/exercicios/tree/master/java

class Submarino(object):
	'''Definindo atributos iniciais da classe'''
	def __init__(self):
		self.x   = 0
		self.y   = 0
		self.z   = 0
		self.dir = 'Norte'
		self.n   = 0

	''' Procedimento principal, que recebe sequencia de comandos
		e chama outros procedimentos '''
	def movimentar(self, sequencia):
		for comando in sequencia:
			if (comando == 'L' or comando == 'R'):
				self.virar(comando)
			elif (comando == 'U' or comando == 'D'):
				self.profundidade(comando)
			else:
				self.andar(comando)

		retorno = [self.x, self.y, self.z, self.dir]

	''' Procecimento chamado para comandos 'R' ou 'L' '''
	def virar(self, comando):
		sentidos = {0:'Norte', 1:'Leste', 2:'Sul',3:'Oeste',\
					-1:'Oeste', -2:'Sul', -3:'Leste'}

		if(comando == 'R'):
			self.n += 1
			if(self.n == 4):
				self.n = 0
			self.dir = sentidos[self.n]
		else:
			self.n -= 1
			if(self.n == -4):
				self.n = 0
			self.dir = sentidos[self.n]

	''' Procedimento chamado para comandos 'U' ou 'D' '''
	def profundidade(self, comando):
		if (comando == 'U'):
			self.z += 1
		else:
			self.z -= 1

	''' Procedimento caso comando seja 'M' '''
	def andar(self, comando):
		if(self.dir == 'Norte'):
			self.y += 1
		elif(self.dir == 'Sul'):
			self.y -= 1
		elif(self.dir == 'Leste'):
			self.x += 1
		else:
			self.x -= 1


class SubmarinoTest(unittest.TestCase):
	def testFun(self):
		sub = Submarino()
		sub.movimentar('R')
		self.assertEqual('Leste', sub.dir)
		sub.movimentar('R')
		self.assertEqual('Sul', sub.dir)
		sub.movimentar('R')
		self.assertEqual('Oeste', sub.dir)
		sub.movimentar('R')
		self.assertEqual('Norte', sub.dir)
		sub.movimentar('RRRR')
		self.assertEqual('Norte', sub.dir)
		sub.movimentar('L')
		self.assertEqual('Oeste', sub.dir)
		sub.movimentar('L')
		self.assertEqual('Sul', sub.dir)
		sub.movimentar('L')
		self.assertEqual('Leste', sub.dir)
		sub.movimentar('L')
		self.assertEqual('Norte', sub.dir)
		sub.movimentar('LLLL')
		self.assertEqual('Norte', sub.dir)
		sub.movimentar('LLLLRRRRLRLRLRRRRRRLLRLLLL')
		self.assertEqual('Norte', sub.dir)




# Comandos : L, R, M, U, D

if __name__ == '__main__':
	unittest.main()