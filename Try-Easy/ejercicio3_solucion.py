import tkinter as tk
from tkinter import ttk

def frame_ejercicio3_solucion(parent_frame):
    from ejercicio3 import frame_ejercicio3

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio3_solucion = tk.Toplevel()
    frame_ejercicio3_solucion.title("Try-Easy")
    frame_ejercicio3_solucion.geometry("1600x900")
    frame_ejercicio3_solucion.configure(bg="#1E1E1E")

    frame_ejercicio3_solucion.geometry(f"+{x}+{y}")

    label_ejercicio3_solucion = ttk.Label(
        frame_ejercicio3_solucion,
        text="Solución",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio3_solucion.pack(pady=30)

    descripcion2 = ttk.Label(
        frame_ejercicio3_solucion,
        text="""
Solución: La medida del segmento AB es 17 y la del segmento AC es 11.06.
La razón por la cual el lado AB mide 17 y el lado AC mide 11.06 está relacionada con la ley de los senos en trigonometría. En un triángulo, la ley de los senos establece que la proporción de la longitud de un lado al seno del ángulo opuesto es constante para todos los lados y ángulos.
Para el lado AB y AC respectivamente:
        """,
        font=("JetBrains Mono Regular", 23),
        foreground="white",
        justify="left",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio3_1.png")
    label_imagen = ttk.Label(frame_ejercicio3_solucion, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()

    imagen2 = tk.PhotoImage(file="ejercicio3_2.png")
    label_imagen2 = ttk.Label(frame_ejercicio3_solucion, image=imagen2)
    label_imagen2.image = imagen2
    label_imagen2.pack()

    boton_volver = ttk.Button(
        frame_ejercicio3_solucion,
        text="Volver",
        command=lambda: frame_ejercicio3(frame_ejercicio3_solucion),
        style="TButton"
    )
    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)