#!/usr/bin/env python
# coding: utf-8

# In[26]:

#Procesamiento de Textos Inteligente


import nltk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re

##Articulo Ingles
texto_html_Eng1 = urllib.request.urlopen('https://en.wikipedia.org/wiki/Donald_Trump')
texto_html_Eng1 = texto_html_Eng1.read()

texto_html = bs.BeautifulSoup(texto_html_Eng1, 'lxml')
paragrafos_Eng1 = texto_html.find_all('p')
articulo_Eng1 = ''

for para in paragrafos_Eng1:
    articulo_Eng1 += para.text
    
articulo_Eng1  = articulo_Eng1.lower()

articulo_Eng1 = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙäëïöüÄËÏÖÜçÇßâêîôûÂÊÎÔÛ]', '', articulo_Eng1)

##Articulo Espaniol
texto_html_Esp1 = urllib.request.urlopen('https://es.wikipedia.org/wiki/Rosal%C3%ADa_Vila')
texto_html_Esp1 = texto_html_Esp1.read()

texto_html = bs.BeautifulSoup(texto_html_Esp1, 'lxml')
paragrafos_Esp1 = texto_html.find_all('p')
articulo_Esp1 = ''

for para in paragrafos_Esp1:
    articulo_Esp1 += para.text
    
articulo_Esp1  = articulo_Esp1.lower()

articulo_Esp1= re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙäëïöüÄËÏÖÜçÇßâêîôûÂÊÎÔÛ]', '', articulo_Esp1)


##Articulo Portuges
texto_html_Port1 = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Portugal')
texto_html_Port1 = texto_html_Port1.read()

texto_html = bs.BeautifulSoup(texto_html_Port1, 'lxml')
paragrafos_Port1 = texto_html.find_all('p')
articulo_Port1 = ''

for para in paragrafos_Port1:
    articulo_Port1 += para.text
    
articulo_Port1  = articulo_Port1.lower()

articulo_Port1= re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙäëïöüÄËÏÖÜçÇßâêîôûÂÊÎÔÛ]', '', articulo_Port1)

##Terminamos de leer los archivos de entrenamiento
nGramasTotales = 0
probIdioma = 1/3
ngramasEng = {}
ngramasEsp = {}
ngramasPort = {}
totalEsp = 0
totalEng = 0
totalPort = 0
chars = 3
pIng=0
pEsp=0
pPort=0
pWord=0
word="ros"
##Separamos los ngramas del archivo en Ingles y sacamos sus probabilidades 
##por ngrama en ingles

for i in range(len(articulo_Eng1)-chars):
    seq = articulo_Eng1[i:i+chars]
    if seq not in ngramasEng.keys():
        ngramasEng[seq] = [1]
        nGramasTotales += 1
        totalEng += 1
    ngramasEng[seq][0] += 1
    
for key, val in ngramasEng.items():
    ngramasEng[key].append(val[0]/totalEng)

##Para los Ngramas en Espanol
    
for i in range(len(articulo_Esp1)-chars):
    seq = articulo_Esp1[i:i+chars]
    if seq not in ngramasEsp.keys():
        ngramasEsp[seq] = [1]
        nGramasTotales += 1
        totalEsp += 1
    ngramasEsp[seq][0] += 1

for key, val in ngramasEsp.items():
    ngramasEsp[key].append(val[0]/totalEsp)

##Para los Ngramas en Portuges
    
for i in range(len(articulo_Port1)-chars):
    seq = articulo_Port1[i:i+chars]
    if seq not in ngramasPort.keys():
        ngramasPort[seq] = [1]
        nGramasTotales += 1
        totalPort += 1
    ngramasPort[seq][0] += 1

for key, val in ngramasPort.items():
    ngramasPort[key].append(val[0]/totalPort)

    
##Ngramas para las probabilidades de las palabras 

    
dict(list(ngramasEng.items())[0:50])

pIng=totalEng/(totalPort+totalEng+totalEsp)
pEsp=totalEsp/(totalPort+totalEng+totalEsp)
pPort=totalPort/(totalPort+totalEng+totalEsp)

pWord=ngramasEsp.get(word,0)[1]*pEsp
# In[ ]: