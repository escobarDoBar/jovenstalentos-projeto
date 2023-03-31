from fastapi import FastAPI
from rich import print

from api.controller import ControllerPrincipal

class api(FastAPI):
	''' Classe da API. '''

	ctrl_principal = None
	''' Controladora principal. Provê funções básicas. '''

	def __init__(self):
		''' Constructo. '''
		super().__init__()

		# Controladoras.
		# Envia o self junto para conseguir criar as rotas.
		print('[cyan][*][/cyan] Inicializando controladoras...')
		self.ctrl_principal = ControllerPrincipal(self)
		print('[cyan][*][/cyan] Controladoras inicializadas.')