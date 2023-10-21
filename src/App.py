# BIBLIOTECAS
from essenciais.conexão import *
from essenciais.extra import *
from essenciais.criarbd import criarBD

# GARANTINDO QUE O BANCO DE DADOS VAI EXISTIR
criarBD()

# Abrindo conexão com o banco de dados
clear()
conexão = abrirConexão()
sleep(0.5)
cursor = abrirCursor(conexão)
sleep(0.85)
clear()

# Programa princiapl
while(True):
    menuPrincipal()
    operacao = input("Digite o numero da operação que deseja realizar(0-4): ")
    clear()

    # Opção para encerrar o programa principal.
    if(operacao == '0'):
        break

    # VER TABELAS
    elif(operacao == '1'):
        while(True):
            menuTabelas()
            tabela = input("Digite o numero da tabela que deseja visualizar(0-3): ")
            clear()

            # Cancelando operacao escolhida e voltando para o menu principal
            if(tabela == '0'):
                break
             
            # VER DEPARTAMENTO
            elif(tabela == '1'):
                print("Departamentos")
                print()
                verDepartamentos(cursor)
                x = input()
                clear()
                
            # VER CARGO
            elif(tabela == '2'):
                print("Cargos")
                print()
                verCargos(cursor)
                x = input()
                clear()

            # VER FUNCIONARIO
            elif(tabela == '3'):
                print("Funcionarios")
                print()
                verFuncionarios(cursor)
                x = input()
                clear()

            else:
                print("*Opção invalida, por favor escolha uma opção valida.")
    
    # CRIAR FUNCIONARIO
    elif(operacao == '2'):
        criarFuncionario(cursor,conexão)

    # MODIFICAR FUNCIONARIO
    elif(operacao == '3'):
        modificarFuncionario(cursor,conexão)

    # DELETAR FUNCIONARIO
    elif(operacao == '4'):
        deletarFuncionario(cursor,conexão)
    
    # Caso o usuario digite um valor invalido
    else:
        print("*Opção invalida, por favor escolha uma opção valida.")

# Fechando conexão com o banco de dados e encerrando o programa
clear()
sleep(0.85)
fecharCursor(cursor)
sleep(0.5)
fecharConexão(conexão)
print("\n\nF I M  D O  P R O G R A M A\n")