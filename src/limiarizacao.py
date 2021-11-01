import os
import numpy as np
import matplotlib.pyplot as plt
import utils.transformacoes as transformacoes
import tkinter as tk
from tkinter import filedialog

# Limpa root do tkinter para não abrir nenhum dialog adicional
root = tk.Tk()
root.withdraw()

def escolher_imagem():
  root = tk.Tk()
  root.withdraw()

  file_path = filedialog.askopenfilename()
  return file_path

def limiarizar_imagem(imagem):
  print('Iniciando limiarização... (Dependendo do tamanho da imagem este processo pode demorar um pouco)')

  # Recebe imagem e transforma em matriz
  matriz_colorida = transformacoes.imagem_to_matriz(imagem)

  # Transforma imagem em tons de cinza
  matriz_cinza = transformacoes.imagem_to_cinza(matriz_colorida)

  # Calcula o histograma da matriz em tons de cinza
  histograma = np.zeros(256).astype(int)
  linhas = matriz_cinza.shape[0]
  colunas = matriz_cinza.shape[1]

  for i in range(linhas):
      for j in range(colunas):
          cor = matriz_cinza[i,j]
          cor = int(cor)
          histograma[cor] += 1

  # Define threshold
  ## O criterio para definição do treshold é achar o ponto em que divide a quantidade de pixels em duas metades quase iguais, ordenados pela cor
  contador, treshold = 0, 0
  metade = linhas * colunas / 2

  for cor in range(256):
      contador += histograma[cor]
      if (contador + histograma[cor]) > metade:
          treshold = cor
          break;

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

# Menu interativo
resp=True
while resp:
    print ("""
    1.Escolher imagem para limiarizacao
    2.Sair
    """)
    resp=input("Esolha uma opção:") 
    if resp=="1":
      imagem_path = ''
      try:
        imagem_path = filedialog.askopenfilename()
        print(imagem_path)
      except:
        print('Ocorreu um erro ao escolher imagem, tente novamente')
      try:
        limiarizar_imagem(imagem_path)
      except:
        print('Ocorreu um erro ao limiarizar a imagem, tente novamente')
    elif resp=="2":
      print("\n FIM") 
      break
    elif resp !="":
      print("\n Opção inválida, tente novamente")
