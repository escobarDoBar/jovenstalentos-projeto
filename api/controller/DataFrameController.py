import pandas as pd

from .controller import Controller


class DataFrameController(Controller):
	''' Classe controladora do DataFrame. '''

	df: pd.DataFrame = None
	''' DataFrame. '''

	lst_tbs: list = None
	''' Lista de DataFrames derivados do principal. '''

	pth_csv: str = 'db/anac.csv'
	''' Caminho do CSV. '''

	def __init__(self, api):
		''' Constructo. '''
		# Chama a herança.
		super().__init__(api)
		# Inicializa variáveis.
		self.lst_tbs = []

	def criarRotas(self, api):

		@api.get('/dataframe/abrir')
		def abrir() -> int:
			''' Abre o DataFrame. '''
			try:
				self.df = pd.read_csv(self.pth_csv)
				return 1
			except:
				return 0
		
		@api.get('/dataframe/aberto')
		def isOpen() -> int:
			''' Verifica se o DataFrame está aberto. '''
			if isinstance(self.df, pd.DataFrame):
				return 1
			return 0
		
		@api.get('/dataframe/head')
		def head(linhas: int = 10) -> str:
			''' Retorna as primeiras linhas.

			@parametros
			linhas: int = 10
			Quantas linhas serão retornadas.
			'''
			return self.df.head(linhas).to_json(orient='records')
		
		@api.get('/dataframe/tail')
		def head(linhas: int = 10) -> str:
			''' Retorna as últimas linhas.

			@parametros
			linhas: int = 10
			Quantas linhas serão retornadas.
			'''
			return self.df.tail(linhas).to_json(orient='records')
		
		@api.get('/dataframe/ajustar')
		def ajustarDF():
			''' Ajusta o DataFrame. '''
			
