import pandas as pd

from api.controller import DataFrameController
from normalizacao.normalizacaoDF import pth_pqe_voo


class VooController(DataFrameController):
	''' Controlador do Voo. '''

	def criarRotas(self, api):
		''' Cria as rotas. '''

		@api.get('/voo/abrirDF')
		def chamarAbrir() -> int:
			return self.abrir()
		@api.get('/voo/simples')
		def chamarGetVoosSimples(qnt_exibir: int = 0):
			return self.getVoosSimples(qnt_exibir)
		@api.get('/voo/get')
		def chamarGetVoos(qnt_exibir: int = 0):
			return self.getVoos(api, qnt_exibir)
		@api.get('/voo/tipos')
		def chamarGetTipoVoo(tp_voo: str = '', qnt_exibir: int = 0):
			return self.getTipoVoo(api, tp_voo, qnt_exibir)
		@api.get('/voo/peso')
		def chamarGetPesoVoo(id_voo: int):
			return self.getPesoVoo(id_voo)

	def __getMerged(self, api):
		''' Retorna um DataFrame dos voos com Joins aplicados. 
		@params
		api: FastAPI
		Carrega o objeto da API, utilizo para acessar outros DataFrames.
		'''
		# Join com Origem.
		join_df: pd.DataFrame = self.df.merge(right = api.ctrl_aer.df, how = 'inner', left_on='id_origem', right_on='id_aeroporto').rename(columns={
			'sigla' : 'origem_sigla',
			'nome' : 'origem_nome',
			'uf' : 'origem_uf',
			'regiao' : 'origem_regiao',
			'pais' : 'origem_pais',
			'continente' : 'origem_continete'
		})
		# Join com Destino.
		join_df = join_df.merge(right = api.ctrl_aer.df, how = 'inner', left_on='id_destino', right_on='id_aeroporto').rename(columns={
			'sigla' : 'destino_sigla',
			'nome' : 'destino_nome',
			'uf' : 'destino_uf',
			'regiao' : 'destino_regiao',
			'pais' : 'destino_pais',
			'continente' : 'destino_continete'
		})
		# Join com Empresa.
		join_df = join_df.merge(right = api.ctrl_emp.df, how = 'inner', left_on='id_empresa', right_on='id_empresa').rename(columns={
			'sigla' : 'empresa_sigla',
			'nome' : 'empresa_nome',
			'nacionalidade' : 'empresa_nacionalidade'
		})

		# Retorno.
		return join_df
	
	def abrir(self) -> int:
		''' Abre o DataFrame. '''
		try:
			# Adiciona o DataFrame à lista.
			self.df = pd.read_parquet(pth_pqe_voo)
			return 1
		except Exception as excp:
			print(excp)
			# Retorna 0 quando der erro.
			return 0

	def getVoosSimples(self, qnt_exibir: int = 0):
		''' Retorna apenas os voos.
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

	def getVoos(self, api, qnt_exibir: int = 0):
		''' Retorna os voos. 
		@params
		api: FastAPI
		Carrega o objeto da API, utilizo para acessar outros DataFrames.
		qnt_exibir: int = None
		Quantos voos serão exibidos.
		0: Desativa o limite;
		>0: Informa o limite.
		'''
		# Define o JOIN.
		join_df: pd.DataFrame = self.__getMerged(api)

		# DEBUG.
		print(join_df.head(10))

		# Retorno.
		if qnt_exibir:
			return self.head(join_df, qnt_exibir)
		return join_df.to_json(orient='records')
	
	def getTipoVoo(self, api, tp_voo: str = '', qnt_exibir: int = 0):
		''' Retorna a origem, destino e empresa do voo, junto com o seu tipo.
		@params
		api: FastAPI
		Carrega o objeto da API, utilizo para acessar outros DataFrames.
		tp_voo: str = ''
		Natureza do voo.
		'' = Indefinido (sem filtro)
		'd' ou 'd' = DOMÉSTICA
		'i' ou 'I' = INTERNACIONAL
		qnt_exibir: int = None
		Quantos voos serão exibidos.
		0: Desativa o limite;
		>0: Informa o limite.
		'''
		# Define o JOIN.
		join_df: pd.DataFrame = self.__getMerged(api)

		# Se houver filtro.
		if tp_voo:
			tp_voo = tp_voo.lower()
			if tp_voo == 'i':
				join_df = join_df[ join_df.natureza == 'INTERNACIONAL' ]
			elif tp_voo == 'd':
				join_df = join_df[ join_df.natureza == 'DOMÉSTICA' ]

		# Salva só as colunas desejadas.
		join_df = join_df[ [ 'id_voo', 'ano', 'mes', 'natureza', 'grupo_de_voo', 'origem_sigla', 'destino_sigla', 'empresa_sigla' ]]

		#DEBUG.
		print(join_df.head(10))

		# Retorno.
		if qnt_exibir:
			return self.head(join_df, qnt_exibir)
		return join_df.to_json(orient='records')
	
	def getPesoVoo(self, id_voo: int):
		''' Retorna o peso de carga do voo. '''
		# Cria o DF filtrado.
		df_filtro: pd.DataFrame = self.df[ self.df.id_voo == id_voo ].fillna(0) # Fillna para substituir NaN por 0

		# Cria um DataFrame temporário.
		temp_df: pd.DataFrame = df_filtro[ [ 'id_voo', 'mes', 'ano', 'natureza' ] ]

		# Soma os pesos da carga.
		temp_df['carga_total'] = df_filtro['carga_paga_kg'] + df_filtro['carga_gratis_kg'] + df_filtro['correio_kg'] + df_filtro['bagagem_kg']

		#DEBUG.
		print(temp_df.head())

		# Retorno.
		return temp_df.to_json(orient='records')
		