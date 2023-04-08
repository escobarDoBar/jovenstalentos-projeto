import pandas as pd

from .controller import Controller
from normalizacao.normalizacaoDF import pth_pqe_aer, pth_pqe_empresa, pth_pqe_voo, pth_csv


class DataFrameController(Controller):
	''' Classe controladora do DataFrame. '''

	aeroporto: pd.DataFrame = None
	''' DataFrame do Aerporto. '''

	voo: pd.DataFrame = None
	''' DataFrame dos Voos. '''

	empresa: pd.DataFrame = None
	''' DataFrame das Empresas. '''

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
			# Inicializa a lista.
			self.lst_df: list = []
			# Loop.
			# for pth in [pth_pqe_voo, pth_pqe_aer, pth_pqe_empresa]: 
			try:
				# Adiciona o DataFrame à lista.
				self.voo = pd.read_parquet(pth_pqe_voo)
				self.aeroporto = pd.read_parquet(pth_pqe_aer)
				self.empresa = pd.read_parquet(pth_pqe_empresa)
			except:
				# Retorna 0 quando der erro.
				return 0
			## DEBUG
			print(self.voo.head())
			print(self.aeroporto.head())
			print(self.empresa.head())
			# Retorno 1 se conseguir importar tudo.
			return 1
		
		@api.get('/dataframe/aberto')
		def isOpen() -> int:
			''' Verifica se o DataFrame está aberto. '''
			return { 
				'voo' : 1 if isinstance(self.voo, pd.DataFrame) else 0,
				'aeroporto' : 1 if isinstance(self.aeroporto, pd.DataFrame) else 0,
				'empresa' : 1 if isinstance(self.empresa, pd.DataFrame) else 0
			}

		def head(df: pd.DataFrame, linhas: int = 10) -> str:
			''' Retorna as primeiras linhas.

			@parametros
			linhas: int = 10
			Quantas linhas serão retornadas.
			'''
			return df.head(linhas).to_json(orient='records')

		def tail(df: pd.DataFrame, linhas: int = 10) -> str:
			''' Retorna as últimas linhas.

			@parametros
			linhas: int = 10
			Quantas linhas serão retornadas.
			'''
			return df.tail(linhas).to_json(orient='records')
		
		@api.get('/voo/simples')
		def getVoosSimples(qnt_exibir: int = 0):
			''' Retorna apenas os voos.

			@params
			qnt_exibir: int = 0
			0: Desativa o limite;
			>0: Define o limite.
			'''
			if qnt_exibir:
				return head(self.voo, qnt_exibir)
			return self.voo.to_json(orient='records')

		@api.get('/voo/get')
		def getVoos(qnt_exibir: int = 0):
			''' Retorna os voos. 
			@params
			qnt_exibir: int = None
			Quantos voos serão exibidos.
			0: Desativa o limite;
			>0: Informa o limite.
			'''
			# Join com Origem.
			tmp_df: pd.DataFrame = self.voo.merge(right = self.aeroporto, how = 'inner', left_on='id_origem', right_on='id_aeroporto').rename(columns={
				'sigla' : 'origem_sigla',
				'nome' : 'origem_nome',
				'uf' : 'origem_uf',
				'regiao' : 'origem_regiao',
				'pais' : 'origem_pais',
				'continente' : 'origem_continete'
			})
			# Join com Destino.
			tmp_df = tmp_df.merge(right = self.aeroporto, how = 'inner', left_on='id_destino', right_on='id_aeroporto').rename(columns={
				'sigla' : 'destino_sigla',
				'nome' : 'destino_nome',
				'uf' : 'destino_uf',
				'regiao' : 'destino_regiao',
				'pais' : 'destino_pais',
				'continente' : 'destino_continete'
			})
			# Join com Empresa.
			tmp_df = tmp_df.merge(right = self.empresa, how = 'inner', left_on='id_empresa', right_on='id_empresa')

			# Retorno.
			if qnt_exibir:
				return head(tmp_df, qnt_exibir)
			return tmp_df.to_json(orient='records')
			
