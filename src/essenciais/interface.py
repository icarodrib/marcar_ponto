""" import tkinter as tk
from App import calcular_horas

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
root.mainloop() """