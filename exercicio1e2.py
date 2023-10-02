#no terminal o resultado fica bugado, mas no arquivo txt fica tudo certo
import random

def ler_lista_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        lista = [linha.strip() for linha in arquivo.readlines()]
    return lista

def geraridade(qtdNum, arquivo):
    nomes = ler_lista_arquivo('nomesex1.txt')
    sobrenomes = ler_lista_arquivo('sobrenomesex1.txt')
    
    with open(arquivo, 'w') as arquivoNum:
        for k in range(qtdNum):
            nome_completo = random.choice(nomes) + " " + random.choice(sobrenomes)
            idade = random.randint(18, 37)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivoNum.write(f"{nome_completo} {idade} {altura}\n")

def lerarquivos(nome, sobrenome, idade):
    with open(nome, 'r') as arquivoN, open(sobrenome, 'r') as arquivoS, open(idade, 'r') as arquivoI:
        for i in range(20):
            nomee = arquivoN.readline().strip()
            sobrenomee = arquivoS.readline().strip()
            idadee = arquivoI.readline().strip()
            print(nomee, sobrenomee, idadee)

def gerararquivo(arquivo):
    with open(arquivo, 'w') as arquivoC:
        for j in range(20):
            nomes = ler_lista_arquivo('nomesex1.txt') 
            sobrenomes = ler_lista_arquivo('sobrenomesex1.txt')
            nome_completo = random.choice(nomes) + " " + random.choice(sobrenomes)
            idade = random.randint(18, 37)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivoC.write(f"Nome: {nome_completo}/ Idade: {idade}/ Altura: {altura}\n")

geraridade(20, 'idadeex1.txt')
lerarquivos('nomesex1.txt', 'sobrenomesex1.txt', 'idadeex1.txt')
gerararquivo('nomecompletoex1.txt')
