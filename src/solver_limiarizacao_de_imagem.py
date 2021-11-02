import os
import numpy as np
import matplotlib.pyplot as plt
import utils.transformacoes as transformacoes
import tkinter as tk
from tkinter import filedialog

# Limpa root do tkinter para não abrir nenhum dialog adicional
root = tk.Tk()
root.withdraw()

def calcular_treshold(histograma, linhas, colunas):
  contador, treshold = 0, 0
  metade = linhas * colunas / 2

  for cor in range(256):
      contador += histograma[cor]
      if (contador + histograma[cor]) > metade:
          treshold = cor
          break;
  
  return treshold

def calcular_histograma(matriz: np.array):
    histograma = np.zeros(256).astype(int)
    linhas = matriz.shape[0]
    colunas = matriz.shape[1]

    for i in range(linhas):
        for j in range(colunas):
            cor = matriz[i,j]
            cor = int(cor)
            histograma[cor] += 1

    return histograma

def solve_limiarizar_imagem(imagem):
  print('Iniciando limiarização... (Dependendo do tamanho da imagem este processo pode demorar um pouco)')

  # Recebe imagem e transforma em matriz
  matriz_colorida = transformacoes.imagem_to_matriz(imagem)

  # Transforma imagem em tons de cinza
  matriz_cinza = transformacoes.imagem_to_cinza(matriz_colorida)

  # Calcula o histograma da matriz em tons de cinza
  histograma = calcular_histograma(matriz_cinza)

  linhas = matriz_cinza.shape[0]
  colunas = matriz_cinza.shape[1]

  # Define threshold
  ## O criterio para definição do treshold é achar o ponto em que divide a quantidade de pixels em duas metades quase iguais, ordenados pela cor
  treshold = calcular_treshold(histograma, linhas, colunas)

  # Limiariza a imagem de acordo com o threshold
  matriz_limiarizada = np.zeros((linhas, colunas))

  for i in range(linhas):
      for j in range(colunas):
          cor = matriz_cinza[i,j]
          if cor < treshold:
              matriz_limiarizada[i,j] = 0
          else:
              matriz_limiarizada[i,j] = 255

  plt.imshow(matriz_limiarizada, cmap='gray')

  img_limiarizada = str(os.path.basename(imagem)).split('.')[0] + ' (limiarizada)'
  plt.savefig(os.path.join('imagens_resultado', img_limiarizada))
  print('Imagem limiarizada com sucesso! Sua nova imagem foi salva na pasta "imagens_resultado"!')
