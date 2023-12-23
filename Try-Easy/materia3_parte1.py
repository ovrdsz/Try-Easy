import tkinter as tk
from tkinter import ttk

def frame_materia3_parte1(parent_frame):
    from materia3 import frame_materia3

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_materia3_parte1 = tk.Toplevel()
    frame_materia3_parte1.title("Try-Easy")
    frame_materia3_parte1.geometry("1600x900")
    frame_materia3_parte1.configure(bg="#1E1E1E")

    frame_materia3_parte1.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia3_parte1,
        text="Teorema del seno",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E"
    )
    titulo.pack(pady=30)

    descripcion = ttk.Label(
        frame_materia3_parte1,
        text="""
En un triángulo cualquiera, la razón entre la longitud de un lado y el seno del ángulo opuesto es constante.
""",
        font=("JetBrains Mono Regular", 28),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack()

    imagen = tk.PhotoImage(file="materia3_parte1.png")
    imagen = imagen.subsample(3,3)
    label_imagen = ttk.Label(frame_materia3_parte1, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()

    boton_volver = ttk.Button(
        frame_materia3_parte1,
        text="Volver",
        command=lambda: frame_materia3(frame_materia3_parte1),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)