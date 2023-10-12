import psycopg2

# Parâmetros para a conexão com o banco de dados
host = "127.0.0.1"
database = "e-enterprise"
user = "postgres"
password = "123"

# Estabelecer a conexão
conn = psycopg2.connect(host=host, database=database, user=user, password=password)

# Criar um cursor a partir da conexão para executar comandos SQL
cur = conn.cursor()

# Executar uma consulta SQL
cur.execute("SELECT * FROM FUNCIONARIO")

# Recuperar os resultados
resultados = cur.fetchall()

# Imprimir os resultados
for linha in resultados:
    print(linha)

# Fechar o cursor e a conexão
cur.close()
conn.close()