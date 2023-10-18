import psycopg2
from tabelas.cargo import *
from tabelas.departamento import *
from tabelas.funcionario import *
from tabelas.banco_horas import * 

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

# Função para mostrar todas as tabelas dentro do banco de dados
def mostrarTabelas(cur):
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    resultados = cur.fetchall()
    for linha in resultados:
        i = len(resultados)
        print(i,") ",linha)
