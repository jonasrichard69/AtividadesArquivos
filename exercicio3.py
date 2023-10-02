def copiaArquivo(escrever, copiar):
    with open(escrever, 'r') as f1, open(copiar, 'w') as f2:
        for linha in f1:
            if not linha.strip().startswith("//"):
                f2.write(linha)


copiaArquivo("escreverex3.txt", "copiarex3.txt")