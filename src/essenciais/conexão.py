# BIBLIOTECAS
import psycopg2
from essenciais.extra import clear

# Criamos a conexão entre o psycopg2 e o nosso banco de dados
def abrirConexão():
    conn = psycopg2.connect(
        host = "127.0.0.1",         # localhost padrão
        database = "e-enterprise",  # Nome do Banco de dados
        user = "postgres",          # Usuario padrão do PostgreSQL
        password = "123"            # Senha definida pelo usuario
    )
    print("Conectado com sucesso!")
    return conn

# Criamos um 'cursor' que serve para podermos executar os comandos SQL apartir dele
def abrirCursor(conn):
    cur = conn.cursor()
    print("Cursor criado com sucesso!")
    return cur

# Fechamos o cursor quando terminarmos de utilizar a conexão
def fecharCursor(cur):
    if(cur != None):
        cur.close()
        print("Cursor encerrado com sucesso!")

# Fechamos a conexão por ultimo quando terminarmos de usa-la
def fecharConexão(conn):
    if(conn != None):
        conn.close() 
        print("Conexão encerrada com sucesso!")
    else:
        print("Erro")

# VER DEPARTAMENTOS FUNCTION
def verDepartamentos(cur):
    cur.execute("SELECT * FROM departamentos ORDER BY id_departamento")
    resultados = cur.fetchall()
    linhas = len(resultados)
    colunas = len(resultados[0])
    print("Ordem dos dados:")
    print("| Id | Nome ")
    print()
    for i in range(linhas):
        for j in range(colunas):
            print("| %s " %resultados[i][j], end = "")
        print()

# VER CARGOS FUNCTION
def verCargos(cur):
    cur.execute("SELECT * FROM cargos ORDER BY id_cargo")
    resultados = cur.fetchall()
    linhas = len(resultados)
    colunas = len(resultados[0])
    print("Ordem dos dados:")
    print("| Id | Nome | Salario ")
    print()
    for i in range(linhas):
        for j in range(colunas):
            print("| %s " %resultados[i][j], end = "")
        print()

# VER FUNCIONARIOS FUNCTION
def verFuncionarios(cur):
    cur.execute(
        """
        SELECT f.id_funcionario,f.nome_funcionario,f.cpf,f.endereco,f.telefone,d.nome_departamento,c.nome_cargo,c.salario_cargo
        FROM funcionarios f
        JOIN departamentos d ON f.id_departamento = d.id_departamento
        JOIN cargos c ON f.id_cargo = c.id_cargo
        ORDER BY f.id_funcionario
        """
    )
    resultados = cur.fetchall()
    linhas = len(resultados)
    colunas = len(resultados[0])
    print("Ordem dos dados:")
    print("| Id | Nome | CPF | Endereço | Telefone | Departamento | Cargo | Salario ")
    print()
    for i in range(linhas):
        for j in range(colunas):
            print("| %s " %resultados[i][j], end = "")
        print()

# INSERIR FUNCIONARIO FUNCTION
def criarFuncionario(cur,conn):
    # DADOS DO FUNCIONARIO
    # NOME
    nome_funcionario = input("Digite o nome do novo funcionario: ")
    clear()

    # CPF
    cpf = input("Digite os 11 digitos do cpf, apenas numeros: ")
    clear()

    # ENDERECO
    endereco = input("Digite o endereço: ")
    clear()

    # TELEFONE
    telefone = input("Digite o telefone com o DDD na frente, apenas numeros: ")
    clear()

    # ID DEPARTAMENTO
    print("---------------------------------------")
    print("|I D| Nome           |I D| Nome       |")
    print("---------------------------------------")
    print("| 1 | Administrativo | 5 | TI         |")
    print("| 2 | Financeiro     | 6 | Produção   |")
    print("| 3 | RH             | 7 | Jurídico   |")
    print("| 4 | Comercial                       |")
    print("---------------------------------------")
    id_departamento = input("Digite o id do departamento: ")
    cur.execute("SELECT nome_departamento FROM departamentos WHERE id_departamento = %s",(id_departamento))
    resultado = cur.fetchall()
    nome_departamento = resultado[0][0]
    clear()

    # ID CARGO
    print("---------------------------------------")
    print("|I D| Nome           |I D| Nome       |")
    print("---------------------------------------")
    print("| 1 | Presidência    | 5 | Analista   |")
    print("| 2 | Diretoria      | 6 | Assistente |")
    print("| 3 | Gerência       | 7 | Auxiliar   |")
    print("| 4 | Supervisão                      |")
    print("---------------------------------------")
    id_cargo = input("Digite o id do cargo: ")
    cur.execute("SELECT nome_cargo FROM cargos WHERE id_cargo = %s",(id_cargo))
    resultado = cur.fetchall()
    nome_cargo = resultado[0][0]
    clear()

    # FINALIZAÇÃO DA FUNÇÃO
    while(True):
        # CONFIRMAÇÃO DOS DADOS POR PARTE DO USUARIO
        print("Ordem dos dados:")
        print("|  Nome  |  CPF  |  Endereço  |  Telefone  |  Departamento  |  Cargo  |")
        print()
        print("| ",nome_funcionario," | ",cpf," | ",endereco," | ",telefone," | ",nome_departamento," | ",nome_cargo," |")
        print("")
        print("Tem certeza que deseja inserir o funcionario acima?")
        print("1) Sim\n0) Não")
        opcao = input("Digite o numero da opção: ")
        opcao = opcao.lower()
    
        # COMMIT DA CRIAÇÃO DOS DADOS NO BANCO DE DADOS
        if(opcao == '1' or opcao == "sim"):
            cur.execute("INSERT INTO funcionarios(nome_funcionario,cpf,endereco,telefone,id_departamento,id_cargo) VALUES (%s,%s,%s,%s,%s,%s)",(nome_funcionario,cpf,endereco,telefone,id_departamento,id_cargo))
            conn.commit()
            clear()
            print(f"*Funcionario {nome_funcionario} criado com sucesso!")
            break
    
        # CANCELAMENTO DA OPERAÇÃO
        elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
            clear()
            print("*Operação cancelada.")
            break

        # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
        else:
            clear()
            print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")

# UPDADE FUNCIONARIO FUNCTION
def modificarFuncionario(cur,conn):
    # MOSTRAR OS FUNCIONARIOS PARA O USUARIO ESCOLHER PELO ID QUAL FUNCIONARIO ALTERAR
    verFuncionarios(cur)
    print()
    id_funcionario = input("Digite o id do funcionario que deseja alterar os dados: ")
    clear()
    while(True):
        cur.execute(
            """
            SELECT f.id_funcionario,f.nome_funcionario,f.cpf,f.endereco,f.telefone,d.nome_departamento,c.nome_cargo,c.salario_cargo
            FROM funcionarios f
            JOIN departamentos d ON f.id_departamento = d.id_departamento
            JOIN cargos c ON f.id_cargo = c.id_cargo
            WHERE id_funcionario = %s""",(id_funcionario)
        )

        # PEGO ESSE RESULTADO E ALOCO EM VARIAVEIS REPARADAS DE ACORDO COM O CAMPO
        resultado = cur.fetchall()
        id = (resultado[0][0])
        nome = (resultado[0][1])
        cpf = (resultado[0][2])
        endereco = (resultado[0][3])
        telefone = (resultado[0][4])
        nome_departamento = (resultado[0][5])
        nome_cargo = (resultado[0][6])
        salario_cargo = (resultado[0][7])

        # MOSTRO AO USUARIO O FUNCIONARIO ESCOLHIDO E DEIXO O USUARIO ESCOLHER O CAMPO A SER ALTERADO
        print("Ordem dos dados:")
        print("|  Id  |  Nome  |  CPF  |  Endereço  |  Telefone  |  Departamento  |  Cargo  | Salario do Cargo")
        print()
        print("| ",id," | ",nome," | ",cpf," | ",endereco," | ",telefone," | ",nome_departamento," | ",nome_cargo," | ",salario_cargo)
        print("")
        print("Escolha um dos campos abaixo que deseja alterar do funcionario escolhido (0-6):")
        print()
        print("1) Nome          4) Telefone")
        print("2) CPF           5) Departamento")
        print("3) Endereço      6) Cargo")
        print("0) Sair")
        opcao = input("Digite o numero da opção: ")
        clear()
        # SAIR DE MODIFICAR
        if(opcao == '0'):
            break
        
        # NOME
        elif(opcao == '1'):
            novo_nome = input("Digite o novo nome do funcionario: ")
            clear()

            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o nome do funcionario de {nome} para {novo_nome}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET nome_funcionario = %s WHERE id_funcionario = %s", (novo_nome, id_funcionario))
                    conn.commit()
                    clear()
                    break
                
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # CPF
        elif(opcao == '2'):
            novo_cpf = input("Digite o novo CPF do funcionario: ")
            clear()

            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o CPF do funcionario de {cpf} para {novo_cpf}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET cpf = %s WHERE id_funcionario = %s", (novo_cpf, id_funcionario))
                    conn.commit()
                    clear()
                    break
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # ENDEREÇO
        elif(opcao == '3'):
            novo_endereco = input("Digite o novo endereço do funcionario: ")
            clear()

            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o endereço do funcionario de {endereco} para {novo_endereco}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET endereco = %s WHERE id_funcionario = %s", (novo_endereco, id_funcionario))
                    conn.commit()
                    clear()
                    break
                
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # TELEFONE
        elif(opcao == '4'):
            novo_telefone = input("Digite o novo telefone do funcionario: ")
            clear()

            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o telefone do funcionario de {telefone} para {novo_telefone}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET telefone = %s WHERE id_funcionario = %s", (novo_telefone, id_funcionario))
                    conn.commit()
                    clear()
                    break
                
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # DEPARTAMENTO
        elif(opcao == '5'):
            # MOSTRA OS DEPARTAMENTOS E O USUARIO ESCOLHE O QUE QUISER TROCAR PARA
            verDepartamentos(cur)
            novo_id_departamento = input("Digite o ID do novo departamento do funcionario: ")
            
            # PESQUISA NO BANCO DE DADOS O NOME DO DEPARTAMENTO USANDO O ID QUE O USUARIO DEU E ALOCA EM UMA VARIAVEL
            cur.execute("SELECT nome_departamento FROM departamentos WHERE id_departamento = %s",(novo_id_departamento))
            resultado = cur.fetchall()
            novo_nome_departamento = resultado[0][0]
            clear()
            
            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o departamento do funcionario de {nome_departamento} para {novo_nome_departamento}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET id_departamento = %s WHERE id_funcionario = %s", (novo_id_departamento, id_funcionario))
                    conn.commit()
                    clear()
                    break
                
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # CARGO
        elif(opcao == '6'):
            # MOSTRA OS CARGOS E O USUARIO ESCOLHE O QUE QUISER TROCAR PARA
            verCargos(cur)
            novo_id_cargo = input("Digite o ID do novo cargo do funcionario: ")
            
            # PESQUISA NO BANCO DE DADOS O NOME DO CARGO USANDO O ID QUE O USUARIO DEU E ALOCA EM UMA VARIAVEL
            cur.execute("SELECT nome_cargo FROM cargos WHERE id_cargo = %s",(novo_id_cargo))
            resultado = cur.fetchall()
            novo_nome_cargo = resultado[0][0]
            clear()
            
            # CONFIRMAÇÃO DA MUDANÇA DOS DADOS POR PARTE DO USUARIO
            while(True):
                print(f"Tem certeza que deseja alterar o cargo do funcionario de {nome_cargo} para {novo_nome_cargo}?")
                print("1) Sim\n0) Não")
                opcao = input("Digite o numero da opção: ")
                opcao = opcao.lower()
                
                # COMMIT DA ALTERAÇÃO DOS DADOS NO BANCO DE DADOS
                if(opcao == '1' or opcao == "sim"):
                    cur.execute("UPDATE funcionarios SET id_cargo = %s WHERE id_funcionario = %s", (novo_id_cargo, id_funcionario))
                    conn.commit()
                    clear()
                    break
                
                # CANCELAMENTO DA OPERAÇÃO
                elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
                    clear()
                    print("*Operação cancelada.")
                    break

                # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
                else:
                    clear()
                    print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")
        
        # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
        else:
            clear()
            print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 a 6)")

# DELETAR FUNCIONARIO FUNCTION
def deletarFuncionario(cur,conn):
    verFuncionarios(cur)
    print()
    id_funcionario = input("Digite o id do funcionario que você deseja deletar: ")
    clear()
    cur.execute(
        """
        SELECT f.id_funcionario,f.nome_funcionario,f.cpf,f.endereco,f.telefone,d.nome_departamento,c.nome_cargo,c.salario_cargo
        FROM funcionarios f
        JOIN departamentos d ON f.id_departamento = d.id_departamento
        JOIN cargos c ON f.id_cargo = c.id_cargo
        WHERE id_funcionario = %s""",(id_funcionario)
    )
    resultado = cur.fetchall()
    id = (resultado[0][0])
    nome_funcionario = (resultado[0][1])
    cpf = (resultado[0][2])
    endereco = (resultado[0][3])
    telefone = (resultado[0][4])
    nome_departamento = (resultado[0][5])
    nome_cargo = (resultado[0][6])
    salario_cargo = (resultado[0][7])

    # FINALIZAÇÃO DA FUNÇÃO
    while(True):
        # CONFIRMAÇÃO DOS DADOS POR PARTE DO USUARIO
        print("Ordem dos dados:")
        print("|  Id  |  Nome  |  CPF  |  Endereço  |  Telefone  |  Departamento  |  Cargo  |  Salario  ")
        print()
        print("| ",id," | ",nome_funcionario," | ",cpf," | ",endereco," | ",telefone," | ",nome_departamento," | ",nome_cargo," | ",salario_cargo)
        print("")
        print("Tem certeza que deseja excluir o funcionario acima?")
        print("1) Sim\n0) Não")
        opcao = input("Digite o numero da opção: ")
        opcao = opcao.lower()

        # COMMIT DA REMOÇÃO DOS DADOS NO BANCO DE DADOS
        if(opcao == '1' or opcao == "sim"):
            cur.execute("DELETE FROM funcionarios WHERE id_funcionario = %s;",(id_funcionario,))
            conn.commit()
            clear()
            print(f"*Funcionario {nome_funcionario} deletado com sucesso!")
            break
        
        # CANCELAMENTO DA OPERAÇÃO
        elif(opcao == '0' or opcao == 'não' or opcao == 'nao'):
            clear()
            print("*Operação cancelada.")
            break

        # LOOP CASO INSIRA UMA OPÇÃO INVALIDA
        else:
            clear()
            print("*A opção digitada foi invalida, por favor digite uma opção valida!(0 ou 1)")