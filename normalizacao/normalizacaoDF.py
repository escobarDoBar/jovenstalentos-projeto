import pandas as pd

from rich import print

pth_db: str = 'db'

pth_csv: str = f'{pth_db}/anac.csv'

pth_pqe_org: str = f'{pth_db}/parquet.origem'
pth_pqe_dest: str = f'{pth_db}/parquet.destino'
pth_pqe_empresa: str = f'{pth_db}/parquet.empresa'
pth_pqe_voo: str = f'{pth_db}/parquet.voo'

m_df = pd.read_csv(pth_csv)

def getDadosVoo(voo_id: int):
	''' Retorna os dados do voo (m_df). '''
	# Extrai os dados do voo.
	dados_voo = m_df[ m_df.index == voo_id ]
	# Retorno.
	return dados_voo

# Separação dos aeroportos de origem.
print('[cyan][*][/cyan] Extraindo Aeroporto de Origem...')
org_df: pd.DataFrame = m_df[
	[ 'aeroporto_de_origem_sigla', 'aeroporto_de_origem_nome', 'aeroporto_de_origem_uf', 'aeroporto_de_origem_regiao', 'aeroporto_de_origem_pais', 'aeroporto_de_origem_continente' ]
].drop_duplicates().reset_index().rename( columns = {
		'index' : 'id_origem',
		'aeroporto_de_origem_sigla' : 'sigla',
		'aeroporto_de_origem_nome' : 'nome', 
		'aeroporto_de_origem_uf' : 'uf', 
		'aeroporto_de_origem_regiao' : 'regiao', 
		'aeroporto_de_origem_pais' : 'pais',
		'aeroporto_de_origem_continente' : 'continete'
	}
)
''' Aeorporto de Origem. '''

def getIdOrigemVoo(voo_id: int):
	''' Retorna o ID (dest_df.id_destino) do aeroport. '''
	# Extrai os dados de voo.
	dados_voo = getDadosVoo(voo_id)
	# Extrai o ID do aeroport.
	id_origem: int = org_df[ org_df.sigla.isin(dados_voo.aeroporto_de_origem_sigla) & org_df.nome.isin(dados_voo.aeroporto_de_origem_nome) ].id_origem.to_list()[0]
	# Retorno.
	return id_origem


# Separação dos aeroportos de destino.
print('[cyan][*][/cyan] Extraindo Aeroporto de Destino...')
dest_df: pd.DataFrame = m_df[
	[ 'aeroporto_de_destino_sigla', 'aeroporto_de_destino_nome', 'aeroporto_de_destino_uf', 'aeroporto_de_destino_regiao', 'aeroporto_de_destino_pais', 'aeroporto_de_destino_continente' ]
].drop_duplicates().reset_index().rename( columns={
		'index' : 'id_destino',
		'aeroporto_de_destino_sigla' : 'sigla',
		'aeroporto_de_destino_nome' : 'nome', 
		'aeroporto_de_destino_uf' : 'uf', 
		'aeroporto_de_destino_regiao' : 'regiao', 
		'aeroporto_de_destino_pais' : 'pais',
		'aeroporto_de_destino_continente' : 'continete'
	}
)
''' Aeorporto de Destino. '''
### As siglas estão duplicadas, mas não precisa filtrar os registros por elas.
# Para extrair o id do aeroporto correto:
# dest_df[ (dest_df.sigla == 'SWSI') & (dest_df.uf == 'PA') ].id_destino
# # Identifica as Siglas duplicadas.
# print(dest_df[ dest_df.sigla.duplicated() ])
# # Exibe os registros com essas siglas.
# print(dest_df[ dest_df.sigla.isin(['SWSI', 'SSZW', 'SDMC']) ])
# # Corrige dropa os duplicados baseando-se no GoogleMaps.
# print( dest_df[ (dest_df.sigla == 'SWSI') & (dest_df.uf == 'PA') ].index )
# sem_dpl = dest_df.sigla.drop_duplicates().count()
# com_dpl = dest_df.sigla.count()
# print(f'Sem: {sem_dpl}')
# print(f'Com: {com_dpl}')
# print(sem_dpl == com_dpl)

def getIdDestinoVoo(voo_id: int):
	''' Retorna o ID (dest_df.id_destino) do aeroport. '''
	# Extrai os dados de voo.
	dados_voo = getDadosVoo(voo_id)
	# Extrai o ID do aeroport.
	id_destino: int = dest_df[ dest_df.sigla.isin(dados_voo.aeroporto_de_destino_sigla) & dest_df.nome.isin(dados_voo.aeroporto_de_destino_nome) ].id_destino.to_list()[0]
	# Retorno.
	return id_destino


empresa_df: pd.DataFrame = m_df[
	[ 'empresa_sigla', 'empresa_nome', 'empresa_nacionalidade' ]
].drop_duplicates().reset_index().rename( columns={
	'index' : 'id_empresa',
	'empresa_sigla' : 'sigla',
	'empresa_nome' : 'nome',
	'empresa_nacionalidade' : 'nacionalidade'
})
''' Empresas. '''

# print(empresa_df[ empresa_df.nome.duplicated()])
# exit()
# print(empresa_df[ empresa_df.sigla.isin(['ETR', 'NCR', 'OWT'])])
# Para extrair o id da empresa correta:
# print( empresa_df[ (empresa_df.sigla == 'NCR') & (empresa_df.nome == 'NATIONAL AIRLINES') ].id_empresa )

def getIdEmpresaVoo(voo_id: int):
	''' Retorna o ID (empresa_df.id_empresa) da empresa responsável pelo voo. '''
	# Extrai os dados de voo.
	dados_voo = getDadosVoo(voo_id)
	# Extrai o ID da empresa.
	id_empresa = empresa_df[ empresa_df.sigla.isin(dados_voo.empresa_sigla) & empresa_df.nome.isin(dados_voo.empresa_nome) ].id_empresa.to_list()[0]
	# Retorno.
	return id_empresa

voos_df: pd.DataFrame = m_df[
	[
		'ano',
		'mes',
		'natureza',
		'grupo_de_voo',
		'passageiros_pagos',
		'passageiros_gratis',
		'carga_paga_kg',
		'carga_gratis_kg',
		'correio_kg',
		'combustivel_litros',
		'distancia_voada_km',
		'decolagens',
		'assentos',
		'horas_voadas',
		'bagagem_kg'
	]
].reset_index().rename(columns={'index' : 'id_voo'})

# # Testa a função getIdEmpresaVoo.
# print(m_df[m_df.index == 1][ [ 'empresa_sigla', 'empresa_nome' ] ])
# print(empresa_df[empresa_df.index.isin(getIdEmpresaVoo(1))][ ['sigla', 'nome'] ] )

# TODO: Tenho que unificar as tabelas aeroporto_origem com aeroporto_destino.

## Relacionamentos.
# Empresa.
print('[cyan][*][/cyan] Relacionando [green]Voo[/green] [blue]->[/blue] [green]Empresa[/green]...')
voos_df['id_empresa'] = voos_df.id_voo.apply(lambda id: getIdEmpresaVoo(id))
# Aeroporto Origem.
print('[cyan][*][/cyan] Relacionando [green]Voo[/green] [blue]->[/blue] [green]Aeroporto Origem[/green]...')
voos_df['id_origem'] = voos_df.id_voo.apply(lambda id: getIdOrigemVoo(id))
# Aeroport Destino.
print('[cyan][*][/cyan] Relacionando [green]Voo[/green] [blue]->[/blue] [green]Aeroporto Destino[/green]...')
voos_df['id_destino'] = voos_df.id_voo.apply(lambda id: getIdDestinoVoo(id))

## Exportação.
# Voos.
print(f'[cyan][*][/cyan] Convertendo [green]voo[blue]_DF[/blue][/green] para [yellow]{pth_pqe_voo}[/yellow]')
voos_df.to_parquet(pth_pqe_voo)
# Empresas.
print(f'[cyan][*][/cyan] Convertendo [green]empresa[blue]_DF[/blue][/green] para [yellow]{pth_pqe_empresa}[/yellow]')
voos_df.to_parquet(pth_pqe_empresa)
# Aeroportos Origem.
print(f'[cyan][*][/cyan] Convertendo [green]origem[blue]_DF[/blue][/green] para [yellow]{pth_pqe_org}[/yellow]')
voos_df.to_parquet(pth_pqe_org)
# Aeroportos Destino.
print(f'[cyan][*][/cyan] Convertendo [green]destino[blue]_DF[/blue][/green] para [yellow]{pth_pqe_dest}[/yellow]')
voos_df.to_parquet(pth_pqe_dest)