import random

def escreverNumA(qtdNum, NomeArquivo):
    with open(NomeArquivo, 'w') as arquivoNum:
        for i in range (qtdNum):
            arquivoNum.write(str(random.randint(0, 100)))
            arquivoNum.write("\n")


escreverNumA(100, 'aleatorios.txt')