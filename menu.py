import funcoes
import sys

if (len(sys.argv) < 2):
    print("Arquivo não informado por linha de comando")
    sys.exit
elif (len(sys.argv) < 4):
    texto = open(sys.argv[1], "r")
    arq_inst = texto.readlines()
    funcoesSemParametro(arq_inst)
else:
    texto = open(sys.argv[1], "r")
    arq_inst = texto.readlines()
    saida = sys.argv[len(sys.argv)-1] + ".asm"
    funcoesComParametro(arq_inst, saida)