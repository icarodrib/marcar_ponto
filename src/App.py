""" from interface import * """
from extra import *

# Abrindo conexão com o banco de dados
clear()
conexão = abrirConexão()
time.sleep(0.5)
cursor = abrirCursor(conexão)
time.sleep(0.85)
clear()

# Programa princiapl
while(True):
    menuPrincipal()
    operacao = input("Digite o numero da opção que deseja realizar(0-5): ")
    clear()

    # Opção para encerrar o programa principal.
    if(operacao == '0'):
        break

    # Opção para ver todas as tabelas existentes dentro do banco de dados
    elif(operacao == '1'):
        while(True):
            mostrarTabelas(cursor)
            x = input()
            if(x != None or x == None):
                clear()
                break
    
    # Escolha de tabela para efetuar operação
    elif(operacao == '2' or operacao == '3' or operacao == '4' or operacao == '5'):
        while(True):
            clear()
            menuTabelas()
            # Aqui o usuario vai escolher a tabela para fazer a ação que havia escolhido
            if(operacao == '2'):
                tabela = input("Criar um novo item em qual tabela?\n(0-3): ")

            elif(operacao == '3'):
                tabela = input("Ver os itens de qual tabela?\n(0-3): ")

            elif(operacao == '4'):
                tabela = input("Modificar itens de qual tabela?\n(0-3): ")

            elif(operacao == '5'):
                tabela = input("Deletar itens de qual tabela?\n(0-3): ")

            clear()
#####################################################################################################
            if(tabela == '0'):
                break

            # FUNÇÕES CRUD RELACIONADAS AS TABELAS 

        # CRIAR INICIO
            # DEPARTAMENTO
            elif(operacao == '2' and tabela == '1'):
                print("Novo item em Departamento")

            # CARGO
            elif(operacao == '2' and tabela == '2'):
                print("Novo item em Cargo")

            # FUNCIONARIO
            elif(operacao == '2' and tabela == '3'):
                print("Novo item em Funcionario")
        # FIM CRIAR

        # VER INICIO
            # DEPARTAMENTO
            elif(operacao == '3' and tabela == '1'):
                print("Itens em Departamento:")
                verDepartamento (cursor)
                
            # CARGO
            elif(operacao == '3' and tabela == '2'):
                print("Itens em Cargo:")
                verCargo(cursor)

            # FUNCIONARIO
            elif(operacao == '3' and tabela == '3'):
                print("Itens em Funcionario:")
                verFuncionario(cursor)
        # FIM VER

        # MODIFICAR INICIO
            # DEPARTAMENTO
            elif(operacao == '4' and tabela == '1'):
                print("Modificar itens em Departamento")

            # CARGO
            elif(operacao == '4' and tabela == '2'):
                print("Modificar itens em Cargo")

            # FUNCIONARIO
            elif(operacao == '4' and tabela == '3'):
                print("Modificar itens em Funcionario")
        #FIM MODIFICAR

        # DELETAR INICIO
            # DEPARTAMENTO
            elif(operacao == '5' and tabela == '1'):
                print("Deletar itens em Departamento")

            # CARGO
            elif(operacao == '5' and tabela == '2'):
                print("Deletar itens em Cargo")

            # FUNCIONARIO
            elif(operacao == '5' and tabela == '3'):
                print("Deletar itens em Funcionario")
        # FIM DELETAR

            else:
                print("*Opção invalida, por favor escolha uma opção valida.")

    # Caso o usuario digite um valor invalido
    else:
        print("*Opção invalida, por favor escolha uma opção valida.")

# Fechando conexão com o banco de dados e encerrando o programa
clear()
time.sleep(0.85)
fecharCursor(cursor)
time.sleep(0.5)
fecharConexão(conexão)
print("\n\nF I M  D O  P R O G R A M A\n")