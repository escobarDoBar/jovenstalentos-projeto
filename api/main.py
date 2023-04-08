from fastapi import FastAPI
from rich import print

from api.controller import (MainController, VooController, EmpresaController, AeroportoController)


class api(FastAPI):
	''' Classe da API. '''

	ctrl_principal: MainController = None
	''' Controladora principal. Provê funções básicas. '''
	ctrl_voo: VooController = None
	''' Controlodara dos Voos. '''
	ctrl_emp: EmpresaController = None
	''' Controlodara das Empresas. '''
	ctrl_aer: AeroportoController = None
	''' Controlodara dos Aeroportos. '''


	def __init__(self):
		''' Constructo. '''
		super().__init__()

		# Controladoras.
		# Envia o self junto para conseguir criar as rotas.
		print('[cyan][*][/cyan] Inicializando controladoras...')
		self.ctrl_principal = MainController(self)
		print('[cyan][*][/cyan] [green]Empresa[/green]...')
		self.ctrl_emp = EmpresaController(self)
		print('[cyan][*][/cyan] [green]Aeroporto[/green]...')
		self.ctrl_aer = AeroportoController(self)
		print('[cyan][*][/cyan] [green]Voo[/green]...')
		self.ctrl_voo = VooController(self)
		print('[cyan][*][/cyan] Controladoras inicializadas.')