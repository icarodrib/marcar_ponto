from essenciais.extra import clear

def criarDepartamento(cur,conn):
    
    # O nome do novo departamento é alocado em uma variavel
    nome_departamento = input("Digite o nome do depatamento: ")

    # Verificamos se o usuario tem certeza que realmente quer criar um novo departamento com esse nome
    print(f"Tem certeza que deseja inserir um novo departamento chamado {nome_departamento}?")
    print("1) Sim\n2) Não")
    opcao = input("Digite o numero da opção: ")
    opcao = opcao.lower()
    
    # Se o usuario confirmar, damos commit na criação do novo departamento
    if(opcao == '1' or opcao == "sim" ):
        # Usando o cursor executamos o codigo de PostgreSQL para criação do novo departamento com o nome alocado na variavel
        cur.execute("INSERT INTO departamento(nome_departamento) VALUES (%s)",(nome_departamento,))
        conn.commit()
        clear()
        print(f"*Departamento {nome_departamento} criado com sucesso!")
    
    # Se não, cancelamos a operação
    else:
        clear()
        print("*Operação cancelada.")

def verDepartamento(cur):
    cur.execute("SELECT * FROM departamento")
    resultados = cur.fetchall()
    linhas = len(resultados)
    colunas = len(resultados[0])
    i = 1
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas -1):
                print("%s" %resultados[i][j], end = " ")
            else:
                print("%s" %resultados[i][j], end = " ")
    print()
            
def modificarDepartamento(cur):
    print("Modificiar departamento")

def deletarDepartamento(cur,conn):
    verDepartamento(cur)
    id_departamento = input("Digite o id do departamento que você deseja deletar: ")

    # Verificamos se o usuario tem certeza que realmente quer criar um novo departamento com esse nome
    print(f"Tem certeza que deseja deletar o departamento {cur.execute('SELECT nome_departamento FROM departamento WHERE id_departamento = %s',(id_departamento))}?")
    print("1) Sim\n2) Não")
    opcao = input("Digite o numero da opção: ")
    opcao = opcao.lower()

    # Se o usuario confirmar, damos commit na criação do novo departamento
    if(opcao == '1' or opcao == "sim" ):
        # Usando o cursor executamos o codigo de PostgreSQL para criação do novo departamento com o nome alocado na variavel
        cur.execute("DELETE FROM departamento WHERE id_departamento = %s;",(id_departamento,))
        conn.commit()
        clear()
        print(f"*Departamento {id_departamento} deletado com sucesso!")
    
    # Se não, cancelamos a operação
    else:
        clear()
        print("*Operação cancelada.")

