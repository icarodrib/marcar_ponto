def criarCargo(cur,conn):
    
    # O nome do novo cargo é alocado em uma variavel
    nome_cargo = input("Digite o nome do depatamento: ")
    salario_cargo = float(input("Digite o salario do cargo\nExemplo: $ 1200.00\n\n$ "))
    
    # Usando o cursor executamos o codigo de PostgreSQL para criação do novo cargo com o nome alocado na variavel
    cur.execute("INSERT INTO cargo(nome_cargo,salario_cargo) VALUES (%s,%s)",(nome_cargo,salario_cargo,))
    
    # Verificamos se o usuario tem certeza que realmente quer criar um novo cargo com esse nome
    opcao = input(f"Tem certeza que deseja inserir um novo cargo chamado {nome_cargo} com um salario de R${salario_cargo} ?\n")
    opcao = opcao.lower()
    
    # Se o usuario confirmar, damos commit na criação do novo cargo
    if(opcao == "sim" or opcao == "s" or opcao == "yes" or opcao == "y"):
        conn.commit()
        print(f"cargo {nome_cargo} criado com sucesso!")
    
    # Se não, cancelamos a operação
    else:
        print("Operação cancelada.")

def verCargo(cur):
    cur.execute(f"SELECT * FROM cargo")
    resultados = cur.fetchall()
    i = 1
    for linha in resultados:
        print(i,") ",linha)
        i+=1
    x = input()
    if(x != None or x == None):
        None

def modificarCargo(cur):
    print("Modificiar cargo")

def deletarCargo(cur):
    print("Deletar cargo")
