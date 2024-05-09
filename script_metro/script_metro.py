import requests
from datetime import datetime
from time import sleep

print()
x = requests.get("http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanasAppV3?versao=4").text

def escrever_em_arquivo(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'a', encoding="utf-8") as arquivo:
            arquivo.write(conteudo+"\n")
        print(f"Conteúdo foi escrito com sucesso no arquivo. {datetime.now()}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")


while True:
    escrever_em_arquivo("log_metro.txt", x)
    sleep(3600)
