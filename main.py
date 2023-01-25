##############################################################
# Jogo da Velha
#
# Feito por Waldyr Turquetti
##############################################################

import numpy as np
import random
from colorama import Fore


JOGADOR = 1
COMPUTADOR = 2
JOGADOR_GANHOU = False
COMPUTADOR_GANHOU = False

def gera_matrix():
    return np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

def define_quem_joga_primeiro():
    return random.choice([JOGADOR, COMPUTADOR])

def define_ordem():
    quem_joga_primeiro = define_quem_joga_primeiro()

    if quem_joga_primeiro == JOGADOR:
        print(Fore.GREEN + 'Você que inicia!')
        ordem = (JOGADOR, COMPUTADOR)
    else:
        print(Fore.RED + 'É o Computador que inicia!')
        ordem = (COMPUTADOR, JOGADOR)

    return ordem

def imprime_matrix(matrix):
    print()
    for i in matrix:
        print(Fore.CYAN + '|'.join(i))
    print()

def jogo(matrix, ordem):

    while not ( JOGADOR_GANHOU or COMPUTADOR_GANHOU ):
        jogador_joga(matrix)
        computador_joga(matrix)

def jogador_joga(matrix):
    print('Sua vez!')

def computador_joga(matrix):
    print('Vez do Computador!')

if __name__ == '__main__':

    matrix_inicial = gera_matrix()
    imprime_matrix(matrix_inicial)
    ordem_do_jogo = define_ordem()
    jogo(matrix_inicial, ordem_do_jogo)
