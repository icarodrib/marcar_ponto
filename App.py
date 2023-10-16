import tkinter as tk
import psycopg2

# Conectar-se ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "e-enterprise",
    user = "postgres",
    password = "123"
)
cursor = conn.cursor()

# Função para calcular horas trabalhadas e extras
def calcular_horas():
    id_funcionario = int(id_funcionario_entry.get())
    data = data_entry.get()
    hora_base = int(hora_base_entry.get())
    
    horas_trabalhadas = f"{int(horas_trabalhadas_entry1.get())}:{int(horas_trabalhadas_entry2.get())}:{int(horas_trabalhadas_entry3.get())}"

    horas_extras = int(horas_trabalhadas_entry1.get()) - hora_base

    # Inserir os dados no banco de dados
    cursor.execute("INSERT INTO horas_trabalhadas (id_funcionario, data, hora_base, horas_trabalhadas, horas_extras) VALUES (%s, %s, %s, %s, %s)",
                   (id_funcionario, data, hora_base, horas_trabalhadas, horas_extras))
    conn.commit()

    resultado_label.config(text=f"Horas trabalhadas: {horas_trabalhadas} horas\nHoras extras: {horas_extras} horas")

# Criar a janela principal
root = tk.Tk()
root.title("Contador de Banco de Horas")

# Elementos da interface
id_funcionario_label = tk.Label(root, text="ID do Funcionário:")
id_funcionario_entry = tk.Entry(root)
data_label = tk.Label(root, text="Data (AAAA-MM-DD):")
data_entry = tk.Entry(root)
hora_base_label = tk.Label(root, text="Hora Base:")
hora_base_entry = tk.Entry(root)
horas_trabalhadas_label = tk.Label(root, text="Horas Trabalhadas:")
horas_trabalhadas_label1 = tk.Label(root, text="Horas")
horas_trabalhadas_entry1 = tk.Entry(root)
horas_trabalhadas_label2 = tk.Label(root, text="Minutos")
horas_trabalhadas_entry2 = tk.Entry(root)
horas_trabalhadas_label3 = tk.Label(root, text="Segundos")
horas_trabalhadas_entry3 = tk.Entry(root)
calcular_button = tk.Button(root, text="Calcular Horas", command=calcular_horas)
resultado_label = tk.Label(root, text="")

# Posicionar elementos na interface
id_funcionario_label.pack()
id_funcionario_entry.pack()
data_label.pack()
data_entry.pack()
hora_base_label.pack()
hora_base_entry.pack()
horas_trabalhadas_label.pack()
horas_trabalhadas_label1.pack()
horas_trabalhadas_entry1.pack()
horas_trabalhadas_label2.pack()
horas_trabalhadas_entry2.pack()
horas_trabalhadas_label3.pack()
horas_trabalhadas_entry3.pack()
calcular_button.pack()
resultado_label.pack()

# Iniciar a aplicação
root.mainloop()

# Fechar a conexão com o banco de dados quando a janela for fechada
conn.close()