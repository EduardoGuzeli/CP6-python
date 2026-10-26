
# Comparador de Clubes Brasileiros

Projeto desenvolvido para o CP6, com o objetivo de consultar e comparar clubes do Campeonato Brasileiro Série A utilizando Python e uma API pública de dados esportivos.

## Integrante

- Eduardo Guzeli — RM 571143

## Objetivo do projeto

Desenvolver um programa que consuma dados de uma API, apresente a tabela do campeonato e permita consultar clubes, comparar desempenhos e visualizar estatísticas gerais.

## Funcionalidades

O programa possui um menu com cinco opções:

1. **Exibir tabela do campeonato:** apresenta a posição, o nome do clube, os pontos e a quantidade de jogos.
2. **Consultar clube:** exibe informações como posição, pontos, jogos, vitórias, empates, derrotas, gols marcados, gols sofridos e saldo de gols.
3. **Comparar dois clubes:** compara os clubes considerando pontos, vitórias e saldo de gols, nessa ordem.
4. **Estatísticas do campeonato:** apresenta a quantidade de clubes, o líder em pontos, o melhor ataque, a melhor defesa e a média de pontos.
5. **Sair:** encerra o programa.

O sistema também possui tratamento para erros de conexão, problemas na leitura dos dados e opções inválidas no menu.

## Tecnologias utilizadas

- Python 3
- Biblioteca Requests
- API Dados Esportivos

## API utilizada

**Endpoint da tabela:**

https://www.dadosesportivos.com.br/api/campeonato/brasileirao-serie-a/tabela

**Documentação da API:**

https://www.dadosesportivos.com.br/api-docs

Os resultados dependem dos dados disponibilizados pela API no momento da consulta.

## Como executar o projeto

### 1. Instalar o Python

É necessário ter o Python 3 instalado no computador.

### 2. Instalar a biblioteca Requests

Abra o terminal na pasta do projeto e execute:

```bash
python -m pip install requests
```

No Windows, caso o comando anterior não funcione, utilize:

```bash
py -m pip install requests
```

### 3. Executar o programa

No terminal, execute:

```bash
python comparador_clubes.py
```

Ou, no Windows:

```bash
py comparador_clubes.py
```

### 4. Utilizar o sistema

Após iniciar o programa, escolha uma opção de 1 a 5 no menu e siga as instruções exibidas no terminal.

Para consultar ou comparar clubes, digite seus nomes conforme aparecem na tabela do campeonato.

## Critério de comparação

A comparação considera os seguintes critérios, nesta ordem:

1. Maior quantidade de pontos.
2. Maior quantidade de vitórias, em caso de empate em pontos.
3. Maior saldo de gols, se os critérios anteriores forem iguais.

Se os clubes apresentarem os mesmos valores nos três critérios, o programa informa que estão empatados na comparação.

## Tratamento de erros

O programa contempla situações como:

- Falha de conexão com a API.
- Resposta HTTP com erro.
- Problemas na interpretação dos dados recebidos.
- Clube não encontrado.
- Opção inválida no menu.
- Indisponibilidade dos dados do campeonato.

## Estrutura dos arquivos

```text
CP6-Comparador-de-Clubes/
├── comparador_clubes.py
└── README.md
```

## Considerações finais

O projeto utiliza funções para organizar o código e facilitar a manutenção. Os dados do campeonato são obtidos pela API no início da execução, sendo necessária uma conexão com a internet para utilizar o sistema.
