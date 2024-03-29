# -*- coding: utf-8 -*-
"""Método1_4_SL_Perceptrons_4_Classes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13TyMfHDP8Kw2JysnL0jZniLaVcvggyCe

#Perceptron para predição de gênero de filme favorito de um indivído.
"""

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, tam_entrada, camadas=1, iteracoes=1000):
        self.W1 = np.zeros(tam_entrada+1)       #+1 para o BIAS
        self.W2 = np.zeros(tam_entrada+1)       #+1 para o BIAS
        self.W3 = np.zeros(tam_entrada+1)       #+1 para o BIAS
        self.W4 = np.zeros(tam_entrada+1)       #+1 para o BIAS

        self.iteracoes = iteracoes
        self.camadas = camadas
    
    def func_ativacao(self, x):                                 # função de ativação tipo degrau, retorna 0 ou 1 (1 para valores positivos maiores que 0)
        return 1 if x > 0 else 0
 
    def predicao(self, x):
        z1 = self.W1.T.dot(x)                                   # somatório da multiplicação das entradas pelos pesos (.T = Transposta, .dot = produto)
        z2 = self.W2.T.dot(x)                                   # somatório da multiplicação das entradas pelos pesos (.T = Transposta, .dot = produto)
        z3 = self.W3.T.dot(x)                                   # somatório da multiplicação das entradas pelos pesos (.T = Transposta, .dot = produto)
        z4 = self.W4.T.dot(x)                                   # somatório da multiplicação das entradas pelos pesos (.T = Transposta, .dot = produto)
        a = [self.func_ativacao(z1), self.func_ativacao(z2), self.func_ativacao(z3), self.func_ativacao(z4)]    # função de ativação, retorna 0 ou 1
        return a
 
    def ajuste(self, X, d1, d2, d3, d4):
        for _ in range(self.iteracoes):
            for i in range(d1.shape[0]):
                
                x = np.insert(X[i], 0, 1)                       # insere o valor do BIAS em cada entrada 
                
                y1 = self.predicao(x)[0]                        # realiza a predição (somatório da multiplicação dos pares [entrada * pesos])
                y2 = self.predicao(x)[1]
                y3 = self.predicao(x)[2]
                y4 = self.predicao(x)[3]
                
                e1 = d1[i] - y1                                 # calcula o erro (pode ser zero) 
                e2 = d2[i] - y2
                e3 = d3[i] - y3 
                e4 = d4[i] - y4     

                self.W1 = self.W1 + self.camadas * e1 * x       # Se Erro (e1) for igual a 0 (zero), nada é atualizado
                self.W2 = self.W2 + self.camadas * e2 * x       # Se Erro (e2) for igual a 0 (zero), nada é atualizado
                self.W3 = self.W3 + self.camadas * e3 * x       # Se Erro (e1) for igual a 0 (zero), nada é atualizado
                self.W4 = self.W4 + self.camadas * e4 * x       # Se Erro (e2) for igual a 0 (zero), nada é atualizado

            if (e1 == 0 and e2 == 0):
              print(_)
              break

def imprimeGenero(d1, d2, d3, d4):
    if(d1 == 0 and d2 == 0 and d3 == 0 and d4 == 1):
        print('Ficção Científica')
    if(d1 == 0 and d2 == 0 and d3 == 1 and d4 == 0):
        print('Terror')
    if(d1 == 0 and d2 == 1 and d3 == 0 and d4 == 0):
        print('Suspense')
    if(d1 == 1 and d2 == 0 and d3 == 0 and d4 == 0):
        print('Romance')

import numpy as np

X = np.array([                          # Array inicial
        [1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 0],
])

d1 = np.array([1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1])              # saída desejada (Neurônio 1)
d2 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])              # saída desejada (Neurônio 2)
d3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0])              # saída desejada (Neurônio 3)
d4 = np.array([0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0])              # saída desejada (Neurônio 4)

perceptron = Perceptron(tam_entrada=6)  # cria perceptron com tamanho de entrada = 6
perceptron.ajuste(X, d1, d2, d3, d4)    # ajusta os pesos
  
print('\nPesos ajustados (Perceptron 1): ', perceptron.W1)
print('Pesos ajustados (Perceptron 2): ', perceptron.W2, '\n')

# Teste Perceptrons
cont = 0
for i in range(d1.shape[0]):
  if(perceptron.predicao(np.insert(X[i], 0, 1))[0] == d1[i] and perceptron.predicao(np.insert(X[i], 0, 1))[1] == d2[i] and perceptron.predicao(np.insert(X[i], 0, 1))[2] == d3[i] and perceptron.predicao(np.insert(X[i], 0, 1))[3] == d4[i]):
    print('predição OK! \t' , X[i], '->\t', d1[i], d2[i], d3[i], d4[i], '\t',end="")
    imprimeGenero(d1[i], d2[i], d3[i], d4[i])
    cont += 1

print('\nAcurácia: ', (cont/d1.shape[0])*100, '%')

predicaoGenerica = [1, 1, 1, 0, 1, 0]
print('Predição do indivíduo: ', predicaoGenerica, ' -> Resultado: ', end="")
imprimeGenero(perceptron.predicao(np.insert(predicaoGenerica, 0, 1))[0], perceptron.predicao(np.insert(predicaoGenerica, 0, 1))[1], perceptron.predicao(np.insert(predicaoGenerica, 0, 1))[2], perceptron.predicao(np.insert(predicaoGenerica, 0, 1))[3])