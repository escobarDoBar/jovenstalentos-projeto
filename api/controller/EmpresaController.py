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
		
		@api.get('/empresa/qnt_voo')
		def chamarGetQntVoosEmpresa(id_empresa: int = None):
			return self.getQntVoosEmpresa(api, id_empresa)
	
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
	
	def getQntVoosEmpresa(self, api, id_empresa: int = None) -> str|dict:
		''' Retorna quantos voos a empresa tem.
		@params
		api: FastAPI
		Carrega o objeto da API, utilizo para acessar outros DataFrames.
		id_empresa: int = None
		Se for definido, informa de qual empresa deve-se contar os voos.
		Senão, traz os valores de todas as empresas.
		'''
		# Inicializa o DataFrame temporario.
		df_retorno: pd.DataFrame = pd.DataFrame()

		# Se tiver o filtro.
		if id_empresa:
			# ID da empresa.
			df_retorno['id_empresa'] = self.df[ self.df.id_empresa == id_empresa ].id_empresa
			# Nome empresa.
			df_retorno['nome'] = self.df[ self.df.id_empresa == id_empresa ].nome
		# Senão, adiciona todas as empresas.
		else:
			# ID da Empresa.
			df_retorno['id_empresa'] = self.df.id_empresa
			# Define o nome das empresas.
			df_retorno['nome'] = self.df.nome

		# Aplica a função a cada empresa.
		df_retorno['qnt_voos'] = self.df.id_empresa.apply(lambda id_empresa, **kwargs: self.extractQntsVoo(kwargs['api'], id_empresa), api=api)

		# DEBUG.
		print(df_retorno.head())

		# Retorno.
		return df_retorno.to_json(orient='records')
				
	@staticmethod
	def extractQntsVoo(api, id_empresa: int) -> pd.DataFrame:
		''' Extrai quantos voos a empresa tem. '''
		# Conta quantos voos ela possui.
		qnt_voos: int = api.ctrl_voo.df[ api.ctrl_voo.df.id_empresa == id_empresa ].id_empresa.count()
		# Retorno.
		return qnt_voos