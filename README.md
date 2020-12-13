# Ciência de dados para filosofia e literatura

O objetivo desse projeto é facilitar os estudos nas áreas de filosofia e literatura (podendo, claro, se expandir para outras ciências humanas e sociais). Utilizando uma técnica chamada *web scraping*, extrairemos as principais citações de alguns filósofos, desse modo, podemos resumir o que um pensador dedicou seu tempo estudando e pesquisando.

A ideia principal é: **Pegar frases famosas de filósofos e escritores, mostrá-las e verificar as palavras mais comuns. Mas por que fazer isso? Bem, eu acredito que esse seja um bom método para analisar sobre o que um filósofo/escritor dedica seus pensamentos.**

Para mais informações sobre, acesse meu post no Medium: https://tinyurl.com/yxnuocdz

**O notebook no Google Colab é esse:** https://tinyurl.com/y4gkvds8

## Etapas do código

**Primeira etapa: Extração e manipulação**

1: Fazer a extração dos dados do site, para nome do autor e frase da citação

1.1: Manipular/fazer a limpeza desses dados

Aqui já temos nossa citação + nome do autor dessa citação
_________________________________________________________________________________________________________________________________________________________________________________
**Segunda etapa: Criar uma grande string com todas as citações**

2: Unir as citações numa única *string*

2.1: Fazer a limpeza dessa string, removendo pontos e vírgulas, tal como letras maíusculas.

Aqui já temos nossa string, que será usada na terceira etapa
_________________________________________________________________________________________________________________________________________________________________________________
**Terceira etapa: Análise visual dos dados (as citações)**

3: Separamos essa string por palavra. Agora cada palavra é uma string

3.1: Jogamos essas palavras numa lista

3.2: Criamos uma tabela de dados com essas palavras

3.3: Com essa tabela, conseguimos plotar um gráfico de barras

3.4: Com essa mesma tabela, conseguimos criar uma nuvem de palavras
_________________________________________________________________________________________________________________________________________________________________________________
**Etapa final: Exibição do resultado do código**

4: Criamos uma função que agregará todo o código descrito acima, usando como parâmetros o nome do autor e o número de páginas a serem vasculhadas

4.1: A exibição aparecerá na seguinte ordem: Citações --> gráfico de barras --> nuvem de palavras

_________________________________________________________________________________________________________________________________________________________________________________
## Resultados

Usarei 4 filósofos/escritores de diferentes áreas como exemplo para verificar se o algoritmo está funcionando de maneira satisfatória e mostrar que o algoritmo não possui viés, assim, cumprindo seu objetivo.

