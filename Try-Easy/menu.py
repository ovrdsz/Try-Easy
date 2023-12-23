import tkinter as tk
from tkinter import ttk

def mostrar_menu(parent_frame):
    from materias import frame_materias
    from ejercicios import frame_ejercicios

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()  
    frame_menu = tk.Toplevel()
    frame_menu.title("Try-Easy")
    frame_menu.geometry("1600x900")
    frame_menu.configure(bg="#1E1E1E")

    frame_menu.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
    frame_menu,
    text="Trigonometría",
    font=("JetBrains Mono Medium", 80),
    foreground="white",
    background="#1E1E1E"
    )
    titulo.pack(pady=30)
    
    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_materia = ttk.Button(
        frame_menu,
        text="Materia",
        command=lambda: frame_materias(frame_menu),
        style="TButton"
    )
    boton_materia.pack(pady=20)

    boton_ejercicios = ttk.Button(
        frame_menu,
        text="Ejercicios",
        command=lambda: frame_ejercicios(frame_menu),
        style="TButton"
    )
    boton_ejercicios.pack(pady=20)
    
    boton_salir = ttk.Button(
        frame_menu,
        text="Salir",
        command=lambda: frame_menu.destroy(),
        style="TButton"
    )
    boton_salir.pack(pady=20)







