import pandas as pd

from .controller import Controller
from normalizacao.normalizacaoDF import pth_pqe_aer, pth_pqe_empresa, pth_pqe_voo, pth_csv


class DataFrameController(Controller):
	''' Classe controladora do DataFrame. '''

	df: pd.DataFrame = None
	''' DataFrame. '''

	def __init__(self, api):
		''' Constructo. '''
		# Chama a herança.
		super().__init__(api)

	@staticmethod
	def head(df: pd.DataFrame, linhas: int = 10) -> str:
		''' Retorna as primeiras linhas.

		@parametros
		linhas: int = 10
		Quantas linhas serão retornadas.
		'''
		return df.head(linhas).to_json(orient='records')

	@staticmethod
	def tail(df: pd.DataFrame, linhas: int = 10) -> str:
		''' Retorna as últimas linhas.

		@parametros
		linhas: int = 10
		Quantas linhas serão retornadas.
		'''
		return df.tail(linhas).to_json(orient='records')
			
