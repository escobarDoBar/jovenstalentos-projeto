from .controller import Controller


class MainController(Controller):
	''' Controlador principal. '''

	def criarRotas(self, api):
		@api.get('/')
		def raiz() -> str:
			''' Rota raiz. '''
			return 'Rota raiz.'