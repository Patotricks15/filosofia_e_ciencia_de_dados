import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def citacoes(nome, pag): #Definindo nossa função
  autor_cont = 0 #Isso aqui serve para a informação do autor aparecer só uma vez, é um contador
  url = 'https://www.pensador.com/autor/' #Link que usaremos para webscraping
  autor = str(nome) #Nome do autor
  autor_nome = autor.upper().replace('_', ' ') #Trocando _ por espaco
  pag = int(pag) #Número de páginas
  frases_juntas = '' #Para depois juntar as frases
  frase_final = [] #Para plotar a frase inteira depois
  stop_words = ''' a, se, SE, autor:o, disse, apenas, melhor, acontece, agora, ainda, alguém, algum, alguma, algumas, alguns, ampla, amplas, amplo, amplos, ante, antes, ao, aos, após, aquela, aquelas, aquele, aqueles, aquilo, as, até, através,
  cada, coisa, coisas, com, como, conhece-te, contra, contudo, da, daquele, daqueles, das, de, dela, delas, dele, deles, depois, dessa, dessas, desse, desses, desta, destas, deste, deste, destes, deve, devem, devendo, dever, deverá, deverão, deveria, deveriam, devia, deviam, disse, disso, disto, dito, diz, dizem,
  do, dos, e, é, ela, elas, ele, eles, em, enquanto, entre, era, essa, essas, esse, esses, esta, está, estamos, estão, estas, estava, estavam, estávamos, este, estes, estou, eu, fazendo, fazer, feita, feitas, feito, feitos, foi, for, foram, fosse, fossem, grande, grandes, há, isso, isto, já, la, lá, lhe, lhes, lo,
  mas, me, mesma, mesmas, mesmo, mesmos, meu, meus, minha, minhas, muita, muitas, muito, muitos, na, não, nas, nem, nenhum, nessa, nessas, nesta, nestas, ninguém, no, nos, nós, nossa, nossas, nosso, nossos, num, numa, nunca, o, os, ou, outra, outras, outro, outros,
  para, pela, pelas, pelo, pelos, pequena, pequenas, pequeno, pequenos, per, perante, pode, pude, podendo, poderia, poderiam, podia, podiam, pois, por, porém, porque, posso, pouca, poucas, pouco, poucos, primeiro, primeiros, própria, próprias, próprio, próprios, quais, qual, quando, quanto, quantos, que, quem,
  são, se, seja, sejam, sem, sempre, sendo, será, serão, seu, seus, si, sido, só, sob, sobre, sua, suas, talvez, também, tampouco, te, tem, tendo, tenha, ter, teu, teus, ti, tido, tinha, tinham, toda, todas, todavia, todo, todos, tu, tua, tuas, tudo, última, últimas, último, últimos, um, uma, umas, uns,
  vendo, ver, vez, vindo, vir, vos, vós,''' #Palavras que serão retiradas
  print(f'FRASES DE {autor_nome}\n') #Mostrando o nome do autor
  for i in range(1, pag+1): #Uma repetição pra fazer o processo inteiro de webscraping
    url_final = url + autor + '/' + str(i) + '/' #Alterando o link para ter o nome do autor e o numero de paginas
    link =f'https://pt.wikipedia.org/wiki/{autor}'
    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')
    numero = []
    html = soup.find('p')
    sobre2 = html.text
    tirar = soup.find_all('a')
    for i in range(len(tirar)):
      retirar = tirar[i].text
      if '[' and ']'in retirar:
        numero.append(retirar)
      for j in numero:
        if j in sobre2:
          sobre2 = sobre2.replace(f'{j}', '')
    req = requests.get(url_final)
    soup = BeautifulSoup(req.content, 'html.parser')

    frase_lista = soup.find_all('p', class_='frase fr')
    try:
      sobre_lista = soup.find_all('span', class_='text')
      sobre = str(sobre_lista).split('>')[1][:-6] #Limpeza de dados
    except:
      sobre = ' '
      print('...')
    if autor_cont < 1: #Fazer a descrição do autor uma única vez, se não vai repetir sempre
      autor_cont +=1
      print(f'Sobre o autor: {sobre}\n')
      print(f'Wikipedia: {sobre2}\n\n\n')
    else:
      autor_cont +=0
      print('')
    for j in range(len(frase_lista)): #Unir todas as frases numa string só
      frase = str(frase_lista[j]).split('>')[1][:-3]
      print(f'{frase}\n')
      frases_juntas += frase
      frases_juntas2 = frases_juntas.replace('.', ' ').replace(';','').lower() #Tirar ponto, virgula e colocar tudo minusculo
    frases_juntas2 = frases_juntas2.split() #separar em palavras
  for palavra in frases_juntas2: #Jogando essas palavras numa lista
    if len(palavra) > 5 and palavra not in stop_words:
      frase_final.append(palavra)
  df = pd.DataFrame(np.array(frase_final)) #Criando um dataframe com essas palavras
  df.columns = ['coluna']
  grafico = df.value_counts()[:5].plot(kind='barh',title=f'Termos mais frequentes ({autor_nome})', xlabel='').get_figure() #Criando o gráfico de barras
  grafico.savefig(f'Gráfico {autor}',bbox_inches='tight')
  nuvem = WordCloud(stopwords=stop_words, background_color='black',width=1600, height=800).generate(' '.join(df['coluna'])) #Criando uma nuvem de palavras
  fig, ax = plt.subplots(figsize=(10,6))
  ax.imshow(nuvem, interpolation='bilinear')
  ax.set_axis_off()
  fig.savefig(f'Nuvem de palavras {autor}',bbox_inches='tight')
  plt.imshow(nuvem); #Mostrando a nuvem
  return (fig,grafico)
