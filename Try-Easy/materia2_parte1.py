import tkinter as tk
from tkinter import ttk

def frame_materia2_parte1(parent_frame):
    from materia2 import frame_materia2

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_materia2_parte1 = tk.Toplevel()
    frame_materia2_parte1.title("Try-Easy")
    frame_materia2_parte1.geometry("1600x900")
    frame_materia2_parte1.configure(bg="#1E1E1E")

    frame_materia2_parte1.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia2_parte1,
        text="Razones trigonométricas",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E"
    )
    titulo.pack(pady=30)

    descripcion = ttk.Label(
        frame_materia2_parte1,
        text="""
Las Razones Trigonométricas son las relaciones entre los lados de un triángulo y sus ángulos. Incluyen seno, coseno y tangente.
""",
        font=("JetBrains Mono Regular", 26),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack()

    imagen = tk.PhotoImage(file="materia2_parte1.png")
    label_imagen = ttk.Label(frame_materia2_parte1, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()

    boton_volver = ttk.Button(
        frame_materia2_parte1,
        text="Volver",
        command=lambda: frame_materia2(frame_materia2_parte1),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)
