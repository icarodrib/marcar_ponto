import datetime as dt # substituindo o nome datetime por dt dentro do código
from datetime import date # quando se quer apenas 1 dos submódulos

import tkinter as tk
import psycopg2

# Conectar-se ao banco de dados PostgreSQL
conn = psycopg2.connect(
    database="Horas_Empresa_2",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Função para calcular horas trabalhadas e extras
def calcular_horas():
    funcionario_id = int(funcionario_id_entry.get())
    data = data_entry.get()
    hora_base = float(hora_base_entry.get())
    horas_trabalhadas = float(horas_trabalhadas_entry.get())

    horas_extras = horas_trabalhadas - hora_base

    # Inserir os dados no banco de dados
    cursor.execute("INSERT INTO horas_trabalhadas (funcionario_id, data, hora_base, horas_trabalhadas, horas_extras) VALUES (%s, %s, %s, %s, %s)",
                   (funcionario_id, data, hora_base, horas_trabalhadas, horas_extras))
    conn.commit()

    resultado_label.config(text=f"Horas trabalhadas: {horas_trabalhadas} horas\nHoras extras: {horas_extras} horas")

# Criar a janela principal
root = tk.Tk()
root.title("Contador de Banco de Horas")

# Elementos da interface
funcionario_id_label = tk.Label(root, text="ID do Funcionário:")
funcionario_id_entry = tk.Entry(root)
data_label = tk.Label(root, text="Data (AAAA-MM-DD):")
data_entry = tk.Entry(root)
hora_base_label = tk.Label(root, text="Hora Base:")
hora_base_entry = tk.Entry(root)
horas_trabalhadas_label = tk.Label(root, text="Horas Trabalhadas:")
horas_trabalhadas_entry = tk.Entry(root)
calcular_button = tk.Button(root, text="Calcular Horas", command=calcular_horas)
resultado_label = tk.Label(root, text="")

# Posicionar elementos na interface
funcionario_id_label.pack()
funcionario_id_entry.pack()
data_label.pack()
data_entry.pack()
hora_base_label.pack()
hora_base_entry.pack()
horas_trabalhadas_label.pack()
horas_trabalhadas_entry.pack()
calcular_button.pack()
resultado_label.pack()

# Iniciar a aplicação
root.mainloop()

# Fechar a conexão com o banco de dados quando a janela for fechada
conn.close()