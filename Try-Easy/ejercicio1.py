import tkinter as tk
from tkinter import ttk

def frame_ejercicio1(parent_frame):
    from ejercicios import frame_ejercicios
    from ejercicio1_solución import frame_ejercicio1_solucion

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio1 = tk.Toplevel()
    frame_ejercicio1.title("Try-Easy")
    frame_ejercicio1.geometry("1600x900")
    frame_ejercicio1.configure(bg="#1E1E1E")

    frame_ejercicio1.geometry(f"+{x}+{y}")

    label_ejercicio1 = ttk.Label(
        frame_ejercicio1,
        text="Ejercicio 1",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio1.pack(pady=30)

    descripcion = ttk.Label(
        frame_ejercicio1,
        text="Considere la imagen de referencia que corresponde a un reloj analógico.",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio1.png")
    label_imagen = ttk.Label(frame_ejercicio1, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack(pady=10)

    descripcion2 = ttk.Label(
        frame_ejercicio1,
        text="Cuando son las 12:20, ¿cuánto mide el ángulo que se forma entre las manecillas del reloj?",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)

    boton_solución = ttk.Button(
        frame_ejercicio1,
        text="Solución",
        command=lambda: frame_ejercicio1_solucion(frame_ejercicio1),
        style="TButton"
    )

    boton_solución.pack(side="left",anchor="se",padx=20, pady=20)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_volver = ttk.Button(
        frame_ejercicio1,
        text="Volver",
        command=lambda: frame_ejercicios(frame_ejercicio1),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)

    

