import tkinter as tk
from tkinter import ttk

def frame_materia2_parte2(parent_frame):
    from materia2 import frame_materia2

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_materia2_parte2 = tk.Toplevel()
    frame_materia2_parte2.title("Try-Easy")
    frame_materia2_parte2.geometry("1600x900")
    frame_materia2_parte2.configure(bg="#1E1E1E")

    frame_materia2_parte2.geometry(f"+{x}+{y}")

    titulo = ttk.Label(
        frame_materia2_parte2,
        text="Teorema de pitágoras",
        font=("JetBrains Mono Medium", 65),
        foreground="white",
        background="#1E1E1E"
    )
    titulo.pack(pady=30)

    descripcion = ttk.Label(
        frame_materia2_parte2,
        text="""
En un triángulo rectángulo, el cuadrado de la longitud de la hipotenusa es igual a la suma de los cuadrados de las longitudes de los otros dos lados.
""",
        font=("JetBrains Mono Regular", 28),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack()

    imagen = tk.PhotoImage(file="materia2_parte2.png")
    imagen = imagen.subsample(2,2)
    label_imagen = ttk.Label(frame_materia2_parte2, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()

    boton_volver = ttk.Button(
        frame_materia2_parte2,
        text="Volver",
        command=lambda: frame_materia2(frame_materia2_parte2),
        style="TButton"
    )
    boton_volver.pack(side="right", anchor="sw", padx=20, pady=20)
