import tkinter as tk
from tkinter import ttk

def frame_ejercicio2(parent_frame):
    from ejercicios import frame_ejercicios
    from ejercicio2_solucion import frame_ejercicio2_solucion

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio2 = tk.Toplevel()
    frame_ejercicio2.title("Try-Easy")
    frame_ejercicio2.geometry("1600x900")
    frame_ejercicio2.configure(bg="#1E1E1E")

    frame_ejercicio2.geometry(f"+{x}+{y}")

    label_ejercicio1 = ttk.Label(
        frame_ejercicio2,
        text="Ejercicio 2",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio1.pack(pady=30)

    descripcion = ttk.Label(
        frame_ejercicio2,
        text="Calcular el valor de x de la siguiente figura:",
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )

    descripcion.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio2.png")
    label_imagen = ttk.Label(frame_ejercicio2, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack(pady=10)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_solución = ttk.Button(
        frame_ejercicio2,
        text="Solución",
        command=lambda: frame_ejercicio2_solucion(frame_ejercicio2),
        style="TButton"
    )

    boton_solución.pack(side="left",anchor="se",padx=20, pady=20)


    boton_volver = ttk.Button(
        frame_ejercicio2,
        text="Volver",
        command=lambda: frame_ejercicios(frame_ejercicio2),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)

    

