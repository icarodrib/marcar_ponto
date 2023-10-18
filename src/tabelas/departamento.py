def criarDepartamento(cur,conn):
    
    # O nome do novo departamento é alocado em uma variavel
    nome_departamento = input("Digite o nome do depatamento: ")
    
    # Usando o cursor executamos o codigo de PostgreSQL para criação do novo departamento com o nome alocado na variavel
    cur.execute("INSERT INTO departamento(nome_departamento) VALUES (%s)",(nome_departamento,))
    
    # Verificamos se o usuario tem certeza que realmente quer criar um novo departamento com esse nome
    opcao = input(f"Tem certeza que deseja inserir um novo departamento chamado {nome_departamento}?\n")
    opcao = opcao.lower()
    
    # Se o usuario confirmar, damos commit na criação do novo departamento
    if(opcao == "sim" or opcao == "s" or opcao == "yes" or opcao == "y"):
        conn.commit()
        print(f"Departamento {nome_departamento} criado com sucesso!")
    
    # Se não, cancelamos a operação
    else:
        print("Operação cancelada.")

def verDepartamento(cur):
    cur.execute(f"SELECT * FROM departamento")
    resultados = cur.fetchall()
    i = 1
    for linha in resultados:
        print(i,") ",linha)
        i+=1
    x = input()
    if(x != None or x == None):
        None

def modificarDepartamento(cur):
    print("Modificiar departamento")

def deletarDepartamento(cur):
    print("Deletar departamento")

