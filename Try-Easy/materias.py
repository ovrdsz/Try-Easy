import tkinter as tk
from tkinter import ttk

def frame_materias(parent_frame):
    from menu import mostrar_menu
    from materia1 import frame_materia1
    from materia2 import frame_materia2
    from materia3 import frame_materia3
    
    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()  
    frame_materia = tk.Toplevel()
    frame_materia.title("Try-Easy")
    frame_materia.geometry("1600x900")
    frame_materia.configure(bg="#1E1E1E")

    frame_materia.geometry(f"+{x}+{y}")

    label_materia = ttk.Label(
        frame_materia,
        text="Materia",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_materia.pack(pady=30)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    materia1 = ttk.Button(
        frame_materia,
        text="Introducción",
        command=lambda: frame_materia1(frame_materia),
        style="TButton"
    )
    materia1.pack(padx=20, pady=20)

    materia2 = ttk.Button(
        frame_materia,
        text="Fundamentos Trigonométricos",
        command=lambda: frame_materia2(frame_materia),
        style="TButton"
    )
    materia2.pack(padx=20, pady=20)

    materia3 = ttk.Button(
        frame_materia,
        text="Teoremas",
        command=lambda: frame_materia3(frame_materia),
        style="TButton"
    )
    materia3.pack(padx=20, pady=20)

    boton_volver = ttk.Button(
        frame_materia,
        text="Volver",
        command=lambda: mostrar_menu(frame_materia),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)

