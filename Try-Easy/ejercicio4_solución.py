import tkinter as tk
from tkinter import ttk

def frame_ejercicio4_solucion(parent_frame):
    from ejercicio4 import frame_ejercicio4

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicio4_solucion = tk.Toplevel()
    frame_ejercicio4_solucion.title("Try-Easy")
    frame_ejercicio4_solucion.geometry("1600x900")
    frame_ejercicio4_solucion.configure(bg="#1E1E1E")

    frame_ejercicio4_solucion.geometry(f"+{x}+{y}")

    label_ejercicio4_solucion = ttk.Label(
        frame_ejercicio4_solucion,
        text="Solución",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicio4_solucion.pack(pady=30)

    descripcion2 = ttk.Label(
        frame_ejercicio4_solucion,
        text="""
Solución: La medida del segmento AB es 14.
Para resolver este ejercicio, puedes utilizar la ley de los cosenos en trigonometría. La ley de los cosenos establece una relación entre los lados y los ángulos de un triángulo.
        """,
        font=("JetBrains Mono Regular", 30),
        foreground="white",
        background="#1E1E1E",
        wraplength=1300
    )
    descripcion2.pack(pady=10)

    imagen = tk.PhotoImage(file="ejercicio4_1.png")
    label_imagen = ttk.Label(frame_ejercicio4_solucion, image=imagen)
    label_imagen.image = imagen
    label_imagen.pack()

    boton_volver = ttk.Button(
        frame_ejercicio4_solucion,
        text="Volver",
        command=lambda: frame_ejercicio4(frame_ejercicio4_solucion),
        style="TButton"
    )
    boton_volver.pack(side="right",anchor="sw",padx=20, pady=20)
    
