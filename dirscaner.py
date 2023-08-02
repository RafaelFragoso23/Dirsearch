#!/usr/bin/python3

#bibliotecas 
import requests

#declaração de lista de diretorios para serem testados
diretorios = ["backups", "senhas", "wp-admin"]

#apresentação
print('''
\033[1;31m
 ____ ___ ____  ____   ____    _    _   _ _____ ____  
|  _ \_ _|  _ \/ ___| / ___|  / \  | \ | | ____|  _ \ 
| | | | || |_) \___ \| |     / _ \ |  \| |  _| | |_) |
| |_| | ||  _ < ___) | |___ / ___ \| |\  | |___|  _ < 
|____/___|_| \_\____/ \____/_/   \_\_| \_|_____|_| \_\
                                                     
\033[1;37m
'''
)

#input
url = input("Digite a url:")

print("\033[1;32m realizando requisição em: https://www."+url+"/")

for pasta in diretorios:
	requisicao = requests.get("https://www."+url+"/"+pasta)
	print("Resultados de:"+pasta+":")
	print(requisicao)
