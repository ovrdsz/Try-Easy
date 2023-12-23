import tkinter as tk
from tkinter import ttk

def frame_materia2(parent_frame):
    from materias import frame_materias
    from materia2_parte1 import frame_materia2_parte1
    from materia2_parte2 import frame_materia2_parte2

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()  
    frame_materia2 = tk.Toplevel()
    frame_materia2.title("Try-Easy")
    frame_materia2.geometry("1600x900")
    frame_materia2.configure(bg="#1E1E1E")

    frame_materia2.geometry(f"+{x}+{y}")

    label_materia1 = ttk.Label(
        frame_materia2,
        text="Fundamentos Trigonométricos",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E"
    )
    label_materia1.pack(pady=30)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton1 = ttk.Button(
        frame_materia2,
        text="Razones trigonométricas",
        command=lambda: frame_materia2_parte1(frame_materia2),
        style="TButton"
    )
    boton1.pack(pady=20)

    boton2 = ttk.Button(
        frame_materia2,
        text="Teorema de Pitágoras",
        command=lambda: frame_materia2_parte2(frame_materia2),
        style="TButton"
    )
    boton2.pack(pady=20)

    boton_volver = ttk.Button(
        frame_materia2,
        text="Volver",
        command=lambda: frame_materias(frame_materia2),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)