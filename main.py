from requests import get
from sys import argv
from os import system

def consulta(placa):
	req=get('https://apicarros.com/v2/consultas/%s/f63e1e63dd231083d38ce929984aac7d'%placa, verify=False).json()
	system('cls||clear')
	msg='|| Consulta de Placa ||\n'
	for item in req:
		msg+=str('%s : %s\n'%(item.upper(),req[item]))
	print(msg.replace(',','\n').replace('[','').replace(']','').replace('{','').replace('}',''))

if len(argv) <=1:
	print('''
|| Consulta de Placa                                ||
|| Github: https://github.com/Kiny-Kiny/Kiny-Painel ||
--------------------

Modo de uso: python3 main.py bpm9099

--------------------
	''');exit()

consulta(argv[1])
