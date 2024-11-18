import tkinter.messagebox
import customtkinter
import tkinter
import numpy as np
import time

def main_window():
    global app
    customtkinter.set_appearance_mode("system")
    app = customtkinter.CTk()  
    app.geometry("800x700")  
    app.title("Calculadora de Matrices")  

    app.resizable(width=False, height=False)  

    start()  
    app.mainloop()  

def start():
    global frame1
    global entry1, entry2, entry4, entry3
    frame1 = customtkinter.CTkFrame(master=app)  
    frame1.pack(fill=tkinter.BOTH, expand=True)  

    label1 = customtkinter.CTkLabel(master=frame1, text="Calculadora de Matrices", font=("Arial", 20))  
    label1.place(relx=0.35, rely=0.1)

    label2 = customtkinter.CTkLabel(master=frame1, text="Matriz 1", font=("Arial", 20))  
    label2.place(relx=0.15, rely=0.2)

    entry1 = customtkinter.CTkEntry(master=frame1, width=140, height=16, corner_radius=4)
    entry1.place(relx=0.1, rely=0.3)
    entry2 = customtkinter.CTkEntry(master=frame1, width=140, height=16, corner_radius=4)
    entry2.place(relx=0.1, rely=0.4)

    label3 = customtkinter.CTkLabel(master=frame1, text=("Matriz 2"), font=("Arial", 20))
    label3.place(relx=0.7, rely=0.2)
    entry3 = customtkinter.CTkEntry(master=frame1, width=140, height=15, corner_radius=4)
    entry3.place(relx=0.7, rely=0.3)
    entry4 = customtkinter.CTkEntry(master=frame1, width=140, height=15, corner_radius=4)
    entry4.place(relx=0.7, rely=0.4)

    label4 = customtkinter.CTkLabel(master=frame1, text=("<- Rows ->"), font=("Arial", 20))
    label4.place(relx=0.42, rely=0.3)
    label5 = customtkinter.CTkLabel(master=frame1, text=("<- columns ->"), font=("Arial", 20))
    label5.place(relx=0.42, rely=0.4)

    button1 = customtkinter.CTkButton(master=frame1, width=140, height=40, corner_radius=10, text="Continuar", command=register_matriz)
    button1.place(relx=0.42, rely=0.6)

def register_matriz():
    global row1, column1, row2, column2
    row1 = entry1.get()
    column1 = entry2.get()
    row2 = entry3.get()
    column2 = entry4.get()


    set_first_matriz()

def set_first_matriz():
    global entradas_matriz
    row_matriz1 = int(row1)
    column_matriz1 = int(column1)
    clear_window()

    entradas_matriz = []  

    for i in range(row_matriz1):
        fila = []
        for j in range(column_matriz1):
            entry = customtkinter.CTkEntry(master=frame1, width=50)
            entry.grid(row=i, column=j, padx=15, pady=10)
            fila.append(entry)
        entradas_matriz.append(fila)

    button = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Siguiente", command=get_first_matriz)
    button.place(relx=0.42, rely=0.8)


def get_first_matriz():
    global entradas_matriz
    global matriz_np


    matriz = []
    for fila in entradas_matriz:
        valores_fila = []
        for entry in fila:
            valor = entry.get()
            valores_fila.append(float(valor) if valor else 0.0)  
        matriz.append(valores_fila)

    matriz_np = np.array(matriz)  
    print(matriz_np)
    set_second_matriz()


def set_second_matriz():
    global entradas_matriz2
    row = int(row2)
    column = int(column2)
    clear_window()

    entradas_matriz2 = []  # Crear una lista nueva para la segunda matriz
    for i in range(row):
        fila = []
        for j in range(column):
            entry = customtkinter.CTkEntry(master=frame1, width=50)
            entry.grid(row=i, column=j, padx=15, pady=10)
            fila.append(entry)
        entradas_matriz2.append(fila)  # Almacenar en la lista correcta
    
    # Botón para obtener la segunda matriz
    button = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Obtener Matriz 2", command=get_second_matriz)
    button.place(relx=0.42, rely=0.8)

def get_second_matriz():
    global entradas_matriz2
    global matriz2_np

    matriz2 = []
    for fila in entradas_matriz2:
        valores_fila = []
        for entry in fila:
            valor = entry.get()
            valores_fila.append(float(valor) if valor else 0.0)
        matriz2.append(valores_fila)
    
    matriz2_np = np.array(matriz2)  # Convertir a numpy array
    print(matriz2_np)
    calculator()

def calculator():
    clear_window()
    label1 = customtkinter.CTkLabel(master=frame1, text=("Operators"), font=("Helvetica", 30))
    label1.place(relx=0.42, rely=0.1)

    button1 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Multiplicate", command=multiplcated)
    button1.place(relx=0.2, rely=0.3)

    button2 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="add", command=add)
    button2.place(relx=0.4, rely=0.3)

    button3 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="subtract", command=subtract)
    button3.place(relx=0.6, rely=0.3)

def back():
    clear_window()
    calculator()

def new():
    clear_window()
    app.destroy()
    main_window()

def multiplcated():
    A = matriz_np
    B = matriz2_np
    try:
        C = np.dot(A, B)
        
        clear_window()
        label1 = customtkinter.CTkLabel(master=frame1, text="Resultado de la Multiplicación", font=("Arial", 20))
        label1.place(relx=0.35, rely=0.8)

        button1 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Back", command=back)
        button1.place(relx=0.2, rely=0.9)

        button2 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="new matriz", command=new)
        button2.place(relx=0.6, rely=0.9)

        for i, fila in enumerate(C):
            for j, valor in enumerate(fila):
                label = customtkinter.CTkLabel(master=frame1, text=f"{valor:.2f}", width=50, height=20, corner_radius=4)
                label.grid(row=i, column=j, padx=15, pady=10)

    except ValueError as e:
        tkinter.messagebox.showerror(title="Error", message=f"{e}")
        clear_window()
        calculator()

def add():
    A = matriz_np
    B = matriz2_np
    try:
        C = (A + B)
        
        clear_window()
        label1 = customtkinter.CTkLabel(master=frame1, text="Equiality of addition", font=("Arial", 20))
        label1.place(relx=0.35, rely=0.8)

        
        button1 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Back", command=back)
        button1.place(relx=0.2, rely=0.9)

        button2 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="new matriz", command=new)
        button2.place(relx=0.6, rely=0.9)

        for i, fila in enumerate(C):
            for j, valor in enumerate(fila):
                label = customtkinter.CTkLabel(master=frame1, text=f"{valor:.2f}", width=50, height=20, corner_radius=4)
                label.grid(row=i, column=j, padx=15, pady=10)

    except ValueError as e:
        tkinter.messagebox.showerror(title="Error", message=f"{e}")
        clear_window()
        calculator()

def subtract():
    A = matriz_np
    B = matriz2_np

    try:
        C = (A - B)
        
        clear_window()
        label1 = customtkinter.CTkLabel(master=frame1, text="Equality of the subtraction", font=("Arial", 20))
        label1.place(relx=0.35, rely=0.8)

        
        button1 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="Back", command=back)
        button1.place(relx=0.2, rely=0.9)

        button2 = customtkinter.CTkButton(master=frame1, width=140, height=28, corner_radius=10, text="new matriz", command=new)
        button2.place(relx=0.6, rely=0.9)

        # Mostrar matriz resultado
        for i, fila in enumerate(C):
            for j, valor in enumerate(fila):
                label = customtkinter.CTkLabel(master=frame1, text=f"{valor:.2f}", width=50, height=20, corner_radius=4)
                label.grid(row=i, column=j, padx=15, pady=10)

    except ValueError as e:
        tkinter.messagebox.showerror(title="Error", message=f"{e}")
        clear_window()
        calculator()


def clear_window():
    for widget in frame1.winfo_children():
        widget.destroy()

# Entry point :)
if __name__ == "__main__":
    main_window()

