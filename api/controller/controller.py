

class Controller:
	''' Controladora base. '''

	def __init__(self, api):
		''' Constructo. '''
		super().__init__()
		# Chama o criador de rotas.
		self.criarRotas(api)
	
	def criarRotas(self, api):
		''' Cria as rotas. '''