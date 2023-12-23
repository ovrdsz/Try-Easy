import tkinter as tk
from tkinter import ttk

def frame_ejercicio3(parent_frame):
    from ejercicios import frame_ejercicios
    from ejercicio3_solucion import frame_ejercicio3_solucion

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio3 = tk.Toplevel()
    frame_ejercicio3.title("Try-Easy")
    frame_ejercicio3.geometry("1600x900")
    frame_ejercicio3.configure(bg="#1E1E1E")

    frame_ejercicio3.geometry(f"+{x}+{y}")

    label_ejercicio1 = ttk.Label(
        frame_ejercicio3,
        text="Ejercicio 3",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio1.pack(pady=30)

    descripcion = ttk.Label(
        frame_ejercicio3,
        text="1) Determine el valor del segmento AB:",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack(pady=10)

    descripcion2 = ttk.Label(
        frame_ejercicio3,
        text="2) Determine el valor del segmento AC:",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio3.png")
    label_imagen = ttk.Label(frame_ejercicio3, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack(pady=10)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_solución = ttk.Button(
        frame_ejercicio3,
        text="Solución",
        command=lambda: frame_ejercicio3_solucion(frame_ejercicio3),
        style="TButton"
    )
    boton_solución.pack(side="left",anchor="se",padx=20, pady=20)


    boton_volver = ttk.Button(
        frame_ejercicio3,
        text="Volver",
        command=lambda: frame_ejercicios(frame_ejercicio3),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)

    

