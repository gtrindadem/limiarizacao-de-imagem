import os
import numpy as np
import matplotlib.pyplot as plt
import utils.transformacoes as transformacoes

## Recebe imagem e transforma em matriz
arquivo = os.path.join('imagens', 'morangos.jpg')
matriz_colorida = transformacoes.imagem_to_matriz(arquivo)

## Transforma imagem em tons de cinza
matriz_cinza = transformacoes.imagem_to_cinza(matriz_colorida)

## Calcula o histograma da matriz em tons de cinza
histograma = np.zeros(256).astype(int)
linhas = matriz_cinza.shape[0]
colunas = matriz_cinza.shape[1]

for i in range(linhas):
    for j in range(colunas):
        cor = matriz_cinza[i,j]
        cor = int(cor)
        histograma[cor] += 1

## Define threshold
### O criterio para definição do treshold é achar o ponto em que divide a quantidade de pixels em duas metades quase iguais, ordenados pela cor
contador, treshold = 0, 0
metade = linhas * colunas / 2

for cor in range(256):
    contador += histograma[cor]
    if (contador + histograma[cor]) > metade:
        treshold = cor
        break;

## Limiariza a imagem de acordo com o threshold
matriz_limiarizada = np.zeros((linhas, colunas))

for i in range(linhas):
    for j in range(colunas):
        cor = matriz_cinza[i,j]
        if cor < treshold:
            matriz_limiarizada[i,j] = 0
        else:
            matriz_limiarizada[i,j] = 255

plt.imshow(matriz_limiarizada, cmap='gray')
plt.savefig(os.path.join('img_limiarizada.png'))