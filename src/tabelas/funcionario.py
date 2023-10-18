def criarFuncionario(cur,conn):
    
    # O nome do novo Funcionario é alocado em uma variavel
    nome_funcionario = input("Digite o nome do depatamento: ")
    
    # Usando o cursor executamos o codigo de PostgreSQL para criação do novo Funcionario com o nome alocado na variavel
    cur.execute("INSERT INTO Funcionario(nome_funcionario) VALUES (%s)",(nome_funcionario,))
    
    # Verificamos se o usuario tem certeza que realmente quer criar um novo Funcionario com esse nome
    opcao = input(f"Tem certeza que deseja inserir um novo Funcionario chamado {nome_funcionario}?\n")
    opcao = opcao.lower()
    
    # Se o usuario confirmar, damos commit na criação do novo Funcionario
    if(opcao == "sim" or opcao == "s" or opcao == "yes" or opcao == "y"):
        conn.commit()
        print(f"Funcionario {nome_funcionario} criado com sucesso!")
    
    # Se não, cancelamos a operação
    else:
        print("Operação cancelada.")

def verFuncionario(cur):
    cur.execute(f"SELECT * FROM funcionario")
    resultados = cur.fetchall()
    for linha in resultados:
        print(linha)
    x = input()
    if(x != None or x == None):
        None

def modificarFuncionario(cur):
    print("Modificiar Funcionario")

def deletarFuncionario(cur):
    print("Deletar Funcionario")
