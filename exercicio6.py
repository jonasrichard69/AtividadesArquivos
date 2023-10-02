import re

def validar_ip(ip):
    regex = r'^([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$'
    
    if re.match(regex, ip):
        return True
    else:
        return False

def separar_ips(arquivo_entrada, arquivo_validos, arquivo_invalidos):
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_validos, 'w') as validos, open(arquivo_invalidos, 'w') as invalidos:
        for linha in entrada:
            ip = linha.strip()
            if validar_ip(ip):
                validos.write(ip + '\n')
            else:
                invalidos.write(ip + '\n')

separar_ips('escreveripex6.txt', 'ipvalidoex6.txt', 'ipinvalidoex6.txt')
