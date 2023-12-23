import tkinter as tk
from tkinter import ttk

def frame_ejercicio1_solucion(parent_frame):
    from ejercicio1 import frame_ejercicio1

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio1_solucion = tk.Toplevel()
    frame_ejercicio1_solucion.title("Try-Easy")
    frame_ejercicio1_solucion.geometry("1600x900")
    frame_ejercicio1_solucion.configure(bg="#1E1E1E")

    frame_ejercicio1_solucion.geometry(f"+{x}+{y}")

    label_ejercicio1_solucion = ttk.Label(
        frame_ejercicio1_solucion,
        text="Solución",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio1_solucion.pack(pady=30)

    descripcion = ttk.Label(
        frame_ejercicio1_solucion,
        text="Solución: 110°",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1000
    )
    descripcion.pack(pady=10)

    descripcion2 = ttk.Label(
        frame_ejercicio1_solucion,
        text="La respuesta es 110°. Esto se debe a que la manecilla pequeña también avanza, disminuyendo 2.5° por cada cinco minutos del minutero. Dado que han transcurrido 20 minutos, esto implica restarle 10 minutos al ángulo de 120° que se formaría si la manecilla pequeña no se moviera. En resumen, la posición da un ángulo de 110°.",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)


    boton_vovler = ttk.Button(
        frame_ejercicio1_solucion,
        text="Volver",
        command=lambda: frame_ejercicio1(frame_ejercicio1_solucion),
        style="TButton"
    )

    boton_vovler.pack(side="right",anchor="sw",padx=20, pady=20)
    