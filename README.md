# Ciência de dados para filosofia e literatura

<p align="center">
  <img src="https://miro.medium.com/max/700/1*pvSawq0JHuvNg8k9uFfVHg.png" width="80%" title="hover text">
</p>

O objetivo desse projeto é facilitar os estudos nas áreas de filosofia e literatura (podendo, claro, se expandir para outras ciências humanas e sociais). Utilizando uma técnica chamada *web scraping*, extrairemos as principais citações de alguns filósofos, desse modo, podemos resumir o que um pensador dedicou seu tempo estudando e pesquisando.

A ideia principal é: **Pegar frases famosas de filósofos e escritores, mostrá-las e verificar as palavras mais comuns. Mas por que fazer isso? Bem, eu acredito que esse seja um bom método para analisar sobre o que um filósofo/escritor dedica seus pensamentos.**

Para mais informações sobre, acesse meu post no Medium: https://tinyurl.com/yxnuocdz

**Streamlit:**

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
**Quarta etapa: Criação de um arquivo em PDF**

4: Será criado um resumo em pdf contendo as 10 principais citações, o gráfico de barras e a nuvem de palavras

4.1: Além do PDF, o algoritmo gera uma imagem em png do gráfico e outra da nuvem de palavras
_________________________________________________________________________________________________________________________________________________________________________________
**Etapa final: Exibição do resultado do código**

5: Criamos uma função que agregará todo o código descrito acima, usando como parâmetros o nome do autor e o número de páginas a serem vasculhadas

5.1: A exibição aparecerá na seguinte ordem: Citações --> gráfico de barras --> nuvem de palavras

_________________________________________________________________________________________________________________________________________________________________________________
## Resultados

Usarei 4 filósofos/escritores de diferentes áreas como exemplo para verificar se o algoritmo está funcionando de maneira satisfatória e mostrar que o algoritmo não possui viés, assim, cumprindo seu objetivo.

### 1. Adam Smith

Adam Smith (1723–1790) foi um economista e filósofo escocês.

Resultado: **riqueza, universal, produção, superioridade, verdadeiro**

<img src="https://miro.medium.com/max/581/1*zZ5ikoz4fm4QKUtKPYhAbQ.png" width="50%" title="Termos mais encontrados em Adam Smith">

### 2. Karl Marx

Karl Heinrich Marx (1818–1883) foi um filósofo e revolucionário socialista alemão.

Resultado: **trabalho, história, homens, essência, social**

<img src="https://miro.medium.com/max/581/1*zZ5ikoz4fm4QKUtKPYhAbQ.png" width="50%" title="Termos mais encontrados em Karl Marx">

### 3. Sócrates

Conhecido como patrono da Filosofia, Sócrates influencia até hoje o pensamento ocidental. Não deixou nenhuma obra escrita, sendo seus discípulos Platão e Xenofontes responsáveis por difundir seu pensamento.

Resultado: **ignorância, sabedoria, devemos, pessoa, conhecimento**

<img src="https://miro.medium.com/max/532/1*nlduZgbBaKqJU3j5ic3tkA.png" width="50%" title="Termos mais encontrados em Sócrates">


### 4. Carl Sagan

Carl Edward Sagan (1934–1996) foi um cientista, astrônomo e divulgador científico norte-americano. Escreveu mais de 600 trabalhos científicos. Realizou a série de TV “Cosmos: Uma Viagem Pessoal”.

Resultado: **universo, ciência, evidência, ausência, estrelas**

<img src="https://miro.medium.com/max/535/1*v9q2dnVKxCbYfJRAA6VnGA.png" width="50%" title="Termos mais encontrados em Sócrates">

## Conclusão dos resultados

Podemos observar que o mecanismo de busca e seleção de termos funcionou de maneira legal, pois se analisarmos:

**Adam Smith sobre riqueza e produção:** um exemplo é o livro “A riqueza das nações”, nele, o autor explora as causas dessa riqueza e o funcionamento da produção, explicando, por exemplo, a divisão do trabalho;

**Karl Marx sobre história e trabalho:** no Manifesto do Partido Comunista, Karl Marx mostra que a luta de classes é o motor da história, e o trabalho como meio de exploração do homem sob o homem através dos meios de produção;

**Sócrates sobre ignorância e sabedoria:** Sócrates não deixou livros escritos, mas Platão em “Apologia de Sócrates”, descreve os diálogos no julgamento de Sócrates. Nesse texto, encontramos falas de Sócrates contra a ignorância e a importância da sabedoria e conhecimento na sociedade;

**Carl Sagan sobre universo e ciência:** Carl Sagan foi um exímio divulgador científico, seus livros e entrevistas mostram a genialidade do autor e seu profundo interesse e amor pela ciência e pelo conhecimento. Uma recomendação de texto é “Um pálido ponto azul”, tirado de seu livro com o mesmo nome. O texto mostra nossa insignificância perante o tamanho do cosmo. É um texto reflexivo sobre a humanidade e a sociedade.

Conhecendo esses pensadores, podemos concluir que nossa ferramenta é viável para resumir e sintetizar os pensamentos desses pensadores. Não é a ferramenta perfeita, ainda, mas em breve receberá atualizações de forma que a torne mais eficiente na busca e no resumo dos pensadores. **Até lá, bons estudos!**

