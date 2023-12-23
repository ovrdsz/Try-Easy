import tkinter as tk
from tkinter import ttk

def frame_materia3(parent_frame):
    from materias import frame_materias
    from materia3_parte1 import frame_materia3_parte1
    from materia3_parte2 import frame_materia3_parte2


    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()  
    frame_materia3 = tk.Toplevel()
    frame_materia3.title("Try-Easy")
    frame_materia3.geometry("1600x900")
    frame_materia3.configure(bg="#1E1E1E")

    frame_materia3.geometry(f"+{x}+{y}")

    label_materia1 = ttk.Label(
        frame_materia3,
        text="Teoremas",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_materia1.pack(pady=30)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton1 = ttk.Button(
        frame_materia3,
        text="Teorema del seno",
        command=lambda: frame_materia3_parte1(frame_materia3),
        style="TButton"
    )
    boton1.pack(pady=20)

    boton2 = ttk.Button(
        frame_materia3,
        text="Teorema del coseno",
        command=lambda: frame_materia3_parte2(frame_materia3),
        style="TButton"
    )
    boton2.pack(pady=20)

    boton_volver = ttk.Button(
        frame_materia3,
        text="Volver",
        command=lambda: frame_materias(frame_materia3),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)