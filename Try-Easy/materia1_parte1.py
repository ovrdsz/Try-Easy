import tkinter as tk
from tkinter import ttk

def frame_materia1_parte1(parent_frame):
    from materia1 import frame_materia1

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_materia1_parte1 = tk.Toplevel()
    frame_materia1_parte1.title("Try-Easy")
    frame_materia1_parte1.geometry("1600x900")
    frame_materia1_parte1.configure(bg="#1E1E1E")


    frame_materia1_parte1.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia1_parte1,
        text="Ángulos y tipos de ángulos",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E",
        justify="center"
    )
    titulo.pack(pady=30)

    descripcion = ttk.Label(
        frame_materia1_parte1,
        text="""
Ángulo: Es la abertura formada por dos rayos que comparten un punto común, llamado vértice.

Tipos de ángulos:

Ángulo agudo: < 90°.
Ángulo recto: 90°.
Ángulo obtuso: > 90° y < 180°.
Ángulo llano: 180°.
Ángulo completo: 360°.
""",
        font=("JetBrains Mono Regular", 28),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack()

    boton_volver = ttk.Button(
        frame_materia1_parte1,
        text="Volver",
        command=lambda: frame_materia1(frame_materia1_parte1),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)

