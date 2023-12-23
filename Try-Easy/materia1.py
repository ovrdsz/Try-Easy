import tkinter as tk
from tkinter import ttk

def frame_materia1(parent_frame):
    from materias import frame_materias
    from materia1_parte1 import frame_materia1_parte1
    from materia1_parte2 import frame_materia1_parte2
    from materia1_parte3 import frame_materia1_parte3

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()  
    frame_materia1 = tk.Toplevel()
    frame_materia1.title("Try-Easy")
    frame_materia1.geometry("1600x900")
    frame_materia1.configure(bg="#1E1E1E")

    frame_materia1.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia1,
        text="Introducción",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    titulo.pack(pady=30)
    

    boton1 = ttk.Button(
        frame_materia1,
        text="Ángulos y tipos de ángulos",
        command=lambda: frame_materia1_parte1(frame_materia1),
        style="TButton"
    )
    boton1.pack(pady=20)

    boton2 = ttk.Button(
        frame_materia1,
        text="Grados",
        command=lambda: frame_materia1_parte2(frame_materia1),
        style="TButton"
    )
    boton2.pack(pady=20)

    boton3 = ttk.Button(
        frame_materia1,
        text="Propiedades de los triángulos",
        command=lambda: frame_materia1_parte3(frame_materia1),
        style="TButton"
    )
    boton3.pack(pady=20)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_volver = ttk.Button(
        frame_materia1,
        text="Volver",
        command=lambda: frame_materias(frame_materia1),
        style="TButton"
    )
    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)