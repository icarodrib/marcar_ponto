# BIBLIOTECAS
from time import sleep
from os import system,name

# Função para conseguir limpar o console com o comando do proprio SO
def clear():
    system('cls' if name=='nt' else 'clear')

# Função para mostrar o menu ao usuario
def menuPrincipal():
    menu = """-------------------------------------------
|  -  -  -  -  M E N U  -  -  -  -        |
-------------------------------------------
|             O P Ç Õ E S                 |
| 1) Ver Dados das Tabelas                |
| 2) Inserir novo funcionario             |
| 3) Modificar os dados de um funcionario |
| 4) Excluir um funcionario               |
| 0) Sair                                 |
-------------------------------------------"""
    print(menu)

def menuTabelas():
    menu = """---------------------------
| - -  T A B E L A S  - - |
---------------------------
| Opções:                 |
| 1) Departamentos        |
| 2) Cargos               |
| 3) Funcionarios         |
| 0) Parar de ver tabelas |
---------------------------"""
    print(menu)

## Funcionario -> Criar Ler Modificar Deletar
## Departamento -> Ver
## Cargo -> Ver
## Banco_Horas ->Ver