from .controller import Controller

class MainController(Controller):
	''' Controlador principal. '''

	def criarRotas(self, api):
		@api.get('/')
		def raiz() -> str:
			''' Rota raiz. '''
			return 'Rota raiz.'
		
		@api.get('/dataframe/abrir')
		def abrir() -> int:
			''' Abre os DataFrames. '''
			try:
				# Abre os DataFrames.
				api.ctrl_voo.abrir()
				api.ctrl_emp.abrir()
				api.ctrl_aer.abrir()
			except Exception as exc:
				print(exc)
				# Retorna 0 quando der erro.
				return 0
			## DEBUG
			print(api.ctrl_voo.df.head())
			print(api.ctrl_emp.df.head())
			print(api.ctrl_aer.df.head())
			# Retorno 1 se conseguir importar tudo.
			return 1