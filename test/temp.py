import psycopg2

conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "e-enterprise",
        user = "postgres",
        password = "123"
    )
cur = conn.cursor()

while(True):
    opcao = int(input("opção: "))
    if(opcao == 1):
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        # Recuperar os resultados
        resultados = cur.fetchall()

        # Imprimir os resultados
        for linha in resultados:
            print(linha)
    elif(opcao == 0):
        break


cur.close()
conn.close()