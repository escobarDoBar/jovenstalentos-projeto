from fastapi import FastAPI
from rich import print

from api.controller import MainController
from api.controller import DataFrameController

class api(FastAPI):
	''' Classe da API. '''

	ctrl_principal: MainController = None
	''' Controladora principal. Provê funções básicas. '''
	ctrl_DataFrame: DataFrameController = None

	def __init__(self):
		''' Constructo. '''
		super().__init__()

		# Controladoras.
		# Envia o self junto para conseguir criar as rotas.
		print('[cyan][*][/cyan] Inicializando controladoras...')
		self.ctrl_principal = MainController(self)
		self.ctrl_DataFrame = DataFrameController(self)
		print('[cyan][*][/cyan] Controladoras inicializadas.')