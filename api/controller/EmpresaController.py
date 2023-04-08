import pandas as pd

from api.controller import DataFrameController
from normalizacao.normalizacaoDF import pth_pqe_empresa


class EmpresaController(DataFrameController):
	''' Controlador da Empresa. '''

	def criarRotas(self, api):
		''' Cria as rotas. '''

		@api.get('/empresa/abrirDF')
		def chamarAbrir() -> int:
			return self.abrir()
		
		@api.get('/empresa/get')
		def chamarGetEmpresa(qnt_exibir: int = 0):
			return self.getEmpresa(qnt_exibir)
	
	def abrir(self) -> int:
		''' Abre o DataFrame. '''
		try:
			# Adiciona o DataFrame à lista.
			self.df = pd.read_parquet(pth_pqe_empresa)
			return 1
		except Exception as excp:
			print(excp)
			# Retorna 0 quando der erro.
			return 0
		
	def getEmpresa(self, qnt_exibir: int = 0):
		''' Retorna as empresas.
		@params
		qnt_exibir: int = 0
		0: Desativa o limite;
		>0: Define o limite.
		'''
		# DEBUG.
		print(self.df.head(10))
		if qnt_exibir:
			return self.head(self.df, qnt_exibir)
		return self.df.to_json(orient='records')