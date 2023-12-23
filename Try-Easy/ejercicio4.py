import tkinter as tk
from tkinter import ttk

def frame_ejercicio4(parent_frame):
    from ejercicios import frame_ejercicios
    from ejercicio4_solución import frame_ejercicio4_solucion

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio4 = tk.Toplevel()
    frame_ejercicio4.title("Try-Easy")
    frame_ejercicio4.geometry("1600x900")
    frame_ejercicio4.configure(bg="#1E1E1E")

    frame_ejercicio4.geometry(f"+{x}+{y}")

    label_ejercicio1 = ttk.Label(
        frame_ejercicio4,
        text="Ejercicio 4",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio1.pack(pady=30)

    descripcion = ttk.Label(
        frame_ejercicio4,
        text="""
Determine el valor del segmento AB.
        """,
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio4.png")
    label_imagen = ttk.Label(frame_ejercicio4, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()


    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    boton_solucion = ttk.Button(
        frame_ejercicio4,
        text="Solución",
        command=lambda: frame_ejercicio4_solucion(frame_ejercicio4),
        style="TButton"
    )
    boton_solucion.pack(side="left", anchor="sw", padx=20, pady=20)

    boton_volver = ttk.Button(
        frame_ejercicio4,
        text="Volver",
        command=lambda: frame_ejercicios(frame_ejercicio4),
        style="TButton"
    )

    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)

    

