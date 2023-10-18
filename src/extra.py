# Import
from conexão import *
import time
import os

# Função para conseguir limpar o console com o comando do proprio SO
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Função para mostrar o menu ao usuario
def menuPrincipal():
    menu = """-------------------------------------
|  -  -  -  -  M E N U  -  -  -  -  |
-------------------------------------
|             O P Ç Õ E S           |
| 1) Ver tabelas existentes         |
| 2) Criar novo item em uma tabela  |
| 3) Ver itens de uma tabela        |
| 4) Modificar itens de uma tabela  |
| 5) Deletar itens de uma tabela    |
| 0) Sair                           |
-------------------------------------"""
    print(menu)

def menuTabelas():
    menu = """-------------------------
|  -  T A B E L A S  -  |
-------------------------
| Opções:               |
| 1) Departamento       |
| 2) Cargo              |
| 3) Funcionario        |
| 4)                    |
| 0) Sair               |
-------------------------"""
    print(menu)