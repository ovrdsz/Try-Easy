import tkinter as tk
from tkinter import ttk
from menu import mostrar_menu

def centrar_ventana(ventana):
    
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"+{x}+{y}")

main = tk.Tk()
main.title("Try-Easy")
main.geometry("1600x900")  
main.configure(bg="#1E1E1E")  

titulo = ttk.Label(
    main,
    text="Try-Easy",
    font=("JetBrains Mono Medium", 80),
    foreground="white",
    background="#1E1E1E"
    )
titulo.pack(pady=30)

descripcion = ttk.Label(
    main,
    text="El programa que necesitas para aprobar la unidad de Trigonometría en Inacap.",
    font=("JetBrains Mono Regular", 50),
    foreground="white",
    background="#1E1E1E",
    justify="center",
    wraplength=1000
)
descripcion.pack(pady=90)

style = ttk.Style()
style.configure("TButton", font=("JetBrains Mono Regular", 50))

boton_continuar = ttk.Button(
    main,
    text="Continuar",
    command=lambda: mostrar_menu(main),  
    style="TButton"
)
boton_continuar.pack(side="right", anchor="sw", padx=20, pady=20)

main.mainloop()

