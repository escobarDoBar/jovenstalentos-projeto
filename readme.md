# Projeto Jovem Aprendiz

### Proposta

O processo de migração de dados necessita da análise dos dados que estão sendo fornecidos para gerar um banco de dados consistente e não-redundante.

Uma das fases requer a análise das relações entre as informações fornecidas e aplicação de técnicas de normalização para gerar um volume menor de dados, que podemos denominar de preparação de dados. No entanto, também há falta de informações completas para que o processo possa gerar 100% de consistência nos dados que serão salvos. Assim também há a necessidade de imputar valores para ajustar as informações a fim de não perder dados. Podemos denominar esta fase de transformação, tratamento ou até enriquecimento dos dados antes do salvamento final.

É importante gerar um modelo de dados mais consistente possível e com a menor possibilidade de redundância de informação utilizando pacotes do python para agilizar o processo de conversão de um arquivo que contém informações salvas em linhas e colunas para um banco de dados.

Seu objetivo nesse projeto é, portanto, utilizar as técnicas e abordagens aprendidas em python para lidar com uma base de dados não-normalizada e apresentar um modelo de dados com o resultado final em um banco de dados relacional.

### Entregas

Suas entregas serão compostas pelos códigos de API, além das principais conclusões sobre como foram tratados e enriquecidos os dados em um arquivo pdf.

### Dados

| Coluna | Descrição |
| :---------------- | :--------|
| empresa_sigla | sigla da companhia aérea |
| empresa_nome | nome da companhia aérea |
| empresa_nacionalidade | tipo de nacionalidade da companhia aérea (estrangeira ou brasileira) |
| ano | ano de registro |
| mes | mês de registro |
| aeroporto_de_origem_sigla | sigla do aeroporto de origem do vôo |
| aeroporto_de_origem_nome | nome do aeroporto de origem do vôo |
| aeroporto_de_origem_uf | sigla do estado de origem do vôo |
| aeroporto_de_origem_regiao | nome da região de origem do vôo |
| aeroporto_de_origem_pais | nome do país de origem do vôo |
| aeroporto_de_origem_continente | nome do continente de origem do vôo |
| aeroporto_de_destino_sigla | sigla do aeroporto de destino do vôo |
| aeroporto_de_destino_nome | nome do aeroporto de destino do vôo |
| aeroporto_de_destino_uf | sigla do estado de destino do vôo |
| aeroporto_de_destino_regiao | nome da região de destino do vôo |
| aeroporto_de_destino_pais | nome do país de destino do vôo |
| aeroporto_de_destino_continente | nome do continente de destino do vôo |
| natureza | tipo da vôo (internacional ou doméstica) |
| grupo_de_voo | grupo (não regular, regular, improdutivo) |
| passageiros_pagos | quantidade de passageiros embarcados com passagens pagas |
| passageiros_gratis | quantidade de passageiros embarcados com passagens gratuitas |
| carga_paga_kg | quantidade de kgs de cargas embarcadas pagas  |
| carga_gratis_kg | quantidade de kgs de cargas embarcadas gratuitas |
| correio_kg | quantidade de kgs de cargas embarcadas do correio |
| combustivel_litros | quantidade de litros de combustíveis consumidos nos vôos |
| distancia_voada_km | quantidade de km voados no mês |
| decolagens | número de decolagens no mês |
| assentos | numéro de assentos registrados nos vôo no mês |
| horas_voadas | número de horas voadas no mês |
| bagagem_kg | quantidade de bagagem em kg registradas no mês |

### Objetivo

Seu objetivo agora é aplicar os recursos aprendidos para preparar e tratar dados, criar API com rotas como consultas de empresas, aeroportos, voos conforme natureza, total de passageiros embarcados em um aeroporto por mês, entre outras. O número de rotas deve ser entre 10 e 15.

### Informações Gerais

A entrega deve ser 100% de sua autoria e resultado de trabalho individual. O projeto foi disponibilizado no dia 04/04 e a data limite para entrega é o dia 11/04. Todos terão 2h para trabalhar durante o dia 31/03, e poderão tirar dúvidas com o Marco nesse período.