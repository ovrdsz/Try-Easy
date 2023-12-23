import tkinter as tk
from tkinter import ttk

def frame_ejercicios(parent_frame):

    from menu import mostrar_menu
    from ejercicio1 import frame_ejercicio1
    from ejercicio2 import frame_ejercicio2
    from ejercicio3 import frame_ejercicio3
    from ejercicio4 import frame_ejercicio4

    x = parent_frame.winfo_x()
    y = parent_frame.winfo_y()

    parent_frame.withdraw()
    frame_ejercicios = tk.Toplevel()
    frame_ejercicios.title("Try-Easy")
    frame_ejercicios.geometry("1600x900")
    frame_ejercicios.configure(bg="#1E1E1E")

    frame_ejercicios.geometry(f"+{x}+{y}")

    label_ejercicios = ttk.Label(
        frame_ejercicios,
        text="Ejercicios",
        font=("JetBrains Mono Medium", 80),
        foreground="white",
        background="#1E1E1E"
    )
    label_ejercicios.pack(pady=30)

    style = ttk.Style()
    style.configure("TButton", font=("JetBrains Mono Regular", 50))

    ejercicio1 = ttk.Button(
        frame_ejercicios,
        text="Ejercicio 1",
        command=lambda: frame_ejercicio1(frame_ejercicios),
        style="TButton"
    )
    ejercicio1.pack(padx=20, pady=20)

    ejercicio2 = ttk.Button(
        frame_ejercicios,
        text="Ejercicio 2",
        command=lambda: frame_ejercicio2(frame_ejercicios),
        style="TButton"
    )
    ejercicio2.pack(padx=20, pady=20)

    ejercicio3 = ttk.Button(
        frame_ejercicios,
        text="Ejercicio 3",
        command=lambda: frame_ejercicio3(frame_ejercicios),
        style="TButton"
    )
    ejercicio3.pack(padx=20, pady=20)

    ejercicio4 = ttk.Button(
        frame_ejercicios,
        text="Ejercicio 4",
        command=lambda: frame_ejercicio4(frame_ejercicios),
        style="TButton"
    )
    ejercicio4.pack(padx=20, pady=20)

    boton_volver = ttk.Button(
        frame_ejercicios,
        text="Volver",
        command=lambda: mostrar_menu(frame_ejercicios),
        style="TButton"
    )
    boton_volver.pack(pady=20)

