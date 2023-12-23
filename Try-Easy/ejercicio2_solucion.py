import tkinter as tk
from tkinter import ttk

def frame_ejercicio2_solucion(parent_frame):
    from ejercicio2 import frame_ejercicio2

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio2_solucion = tk.Toplevel()
    frame_ejercicio2_solucion.title("Try-Easy")
    frame_ejercicio2_solucion.geometry("1600x900")
    frame_ejercicio2_solucion.configure(bg="#1E1E1E")

    frame_ejercicio2_solucion.geometry(f"+{x}+{y}")

    label_ejercicio2_solucion = ttk.Label(
        frame_ejercicio2_solucion,
        text="Solución",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio2_solucion.pack(pady=30)

    descripcion2 = ttk.Label(
        frame_ejercicio2_solucion,
        text="""
Solución: El lado mide, aproximadamente, 16.9.
Conocemos la hipotenusa y el ángulo. Como queremos calcular el lado opuesto, utilizamos el seno
        """,
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio2_1.png")
    label_imagen = ttk.Label(frame_ejercicio2_solucion, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack(pady=10)

    descripcion3 = ttk.Label(
        frame_ejercicio2_solucion,
        text="Finalmente despejamos x y sustituimos los valores.",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion3.pack(pady=10)

    boton_volver = ttk.Button(
        frame_ejercicio2_solucion,
        text="Volver",
        command=lambda: frame_ejercicio2(frame_ejercicio2_solucion),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)



