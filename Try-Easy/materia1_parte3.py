import tkinter as tk
from tkinter import ttk

def frame_materia1_parte3(parent_frame):
    from materia1 import frame_materia1

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_materia1_parte3 = tk.Toplevel()
    frame_materia1_parte3.title("Try-Easy")
    frame_materia1_parte3.geometry("1600x900")
    frame_materia1_parte3.configure(bg="#1E1E1E")

    frame_materia1_parte3.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia1_parte3,
        text="Propiedades de los triángulos",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E"
    )
    titulo.pack(pady=30)

    descripcion = ttk.Label(
        frame_materia1_parte3,
        text="""
Los triángulos son figuras geométricas de tres lados y tres ángulos.
Poseen las siguientes propiedades:

1) La suma de los ángulos internos de un triángulo es igual a 180°.
2) Son el único polígono que no posee diagonales.
3) Por lo menos dos de los tres ángulos de un triángulo son agudos siempre.
4) Podemos aplicar las propiedades de los triángulos al estudio de los demás polígonos.
""",
        font=("JetBrains Mono Regular", 28),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack()


    boton_volver = ttk.Button(
        frame_materia1_parte3,
        text="Volver",
        command=lambda: frame_materia1(frame_materia1_parte3),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)