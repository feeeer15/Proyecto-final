import tkinter as tk
import customtkinter as ctk
from backend import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import os
import sys
import tkinter.font as tkFont

def ruta_recurso(rel_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, rel_path)

def cargar_fuente(nombre, ruta):
    if os.path.exists(ruta):
        try:
            # Carga la fuente .ttf usando font.createfont
            root.tk.call("font", "create", nombre, "-family", nombre)
        except Exception as e:
            print(f"Error al registrar la fuente {nombre}: {e}")

def ventana_de_inico():
    global root
    root = ctk.CTk()
    root.title("Inicio de sesión")
    root.geometry("695x695")
    root.config(bg="#EADED0")

    cargar_fuente("Calligraphy (OpenType)", ruta_recurso("Fuentes/Calligraphy.ttf"))
    cargar_fuente("vendya (OpenType)", ruta_recurso("Fuentes/vendya.ttf"))
    cargar_fuente("DreamOrphans-Regular (OpenType)", ruta_recurso("Fuentes/Dream_orphans.ttf"))

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root.resizable(width=False, height=False)
    
    titulo = tk.Label(root, text=f"Bienvenido!", font=("Calligraphy", 100 ), fg="#8C916C", bg="#EADED0", padx=20, pady=100)
    titulo.pack()

    global entrada1, entrada2
    etiqueta1 = tk.Label(root, text="Usuario:", fg="#8C916C", bg="#EADED0", font=("Vendya", 30))
    entrada1 = ctk.CTkEntry(root, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 20), text_color="#EADED0", width=200,)
    etiqueta2 = tk.Label(root, text="Contraseña:", fg="#8C916C", bg="#EADED0", font=("Vendya", 30))
    entrada2 = ctk.CTkEntry(root, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 20), text_color="#EADED0", show="★", width=200)  

    etiqueta1.pack()
    entrada1.pack()
    etiqueta2.pack()
    entrada2.pack()

    boton_login = ctk.CTkButton(master=root, text="Iniciar Sesión", fg_color="#2c3424", bg_color="#EADED0", font=("Vendya", 18, "bold"), hover_color="#8C916C", command=inicio)
    boton_login.pack(pady=40)
    root.protocol("WM_DELETE_WINDOW", al_cerrar)

    etiqueta_texto = ctk.CTkLabel(master=root, text="¿No tienes una cuenta?", text_color="#8C916C", bg_color="#EADED0", font=("Vendya", 20, "bold"))
    etiqueta_texto.place(x=20, y=630)

    etiqueta_link = ctk.CTkLabel(master=root, text="Registrate aquí", text_color="#8C916C", bg_color="#EADED0", font=("Vendya", 20, "underline", "bold"), cursor="hand2")
    etiqueta_link.place(x=245, y=630)

    etiqueta_link.bind("<Button-1>", lambda event: [root.destroy(), ventana_registro()])


    root.mainloop()

def al_cerrar():
    root.destroy()

def ventana_registro():
    global root3

    root3 = ctk.CTk()
    root3.title("Registrate")
    root3.geometry("695x695")
    root3.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root3.winfo_screenwidth()
    alto_pantalla = root3.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root3.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root3.resizable(width=False, height=False)

    registro = tk.Label(root3, text=f"¿No eres parte de bancofer?", font=("Vendya", 20 ), fg="#8C916C", bg="#EADED0", padx=20, pady=80)
    registro.pack()

    registrate = tk.Label(root3, text=f"Registrate!", font=("Calligraphy", 80 ), fg="#8C916C", bg="#EADED0")
    registrate.place(x=200, y=120)

    global entrada3
    global entrada4
    global entrada5
    global entrada6

    etiqueta3 = tk.Label(root3, text="Nombre completo :", fg="#8C916C", bg="#EADED0", font=("Vendya", 25, "bold"))
    entrada3 = ctk.CTkEntry(root3, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 18), text_color="#EADED0", width=240)

    etiqueta4 = tk.Label(root3, text="Número de telefono :", fg="#8C916C", bg="#EADED0", font=("Vendya", 25, "bold"))
    entrada4 = ctk.CTkEntry(root3, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 18), text_color="#EADED0", width=240)

    etiqueta5 = tk.Label(root3, text="Usuario :", fg="#8C916C", bg="#EADED0", font=("Vendya", 25, "bold"))
    entrada5 = ctk.CTkEntry(root3, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 18,), text_color="#EADED0", width=240)  

    etiqueta6 = tk.Label(root3, text="Contraseña :", fg="#8C916C", bg="#EADED0", font=("Vendya", 25, "bold"))
    entrada6 = ctk.CTkEntry(root3, fg_color="#8C916C", bg_color="#EADED0", font=("Dream Orphans", 18,), text_color="#EADED0", show="★", width=240) 

    etiqueta3.place(x=280, y=300)
    entrada3.place(x=225, y=288)

    etiqueta4.place(x=280, y=415)
    entrada4.place(x=225, y=380)

    etiqueta5.place(x=280, y=530)
    entrada5.place(x=225, y=472)

    etiqueta6.place(x=280, y=645)
    entrada6.place(x=225, y=564)

    boton_registrar = ctk.CTkButton(master=root3, text="Registrar", fg_color="#2c3424", bg_color="#EADED0", font=("Vendya", 15, "bold"), hover_color="#8C916C", command=registar)
    boton_registrar.place(x=500, y=635)

    root3.mainloop()


def inicio():
    usuario_input = entrada1.get()
    password_input = entrada2.get()

    if not usuario_input or not password_input:
        messagebox.showwarning("Campos vacíos", "Por favor completa ambos campos.")
        return

    usuario_registrado = Usuario.iniciar_sesion(usuario_input, password_input)

    if usuario_registrado:
        messagebox.showinfo("Éxito", f"¡Bienvenid@ {usuario_registrado.nombre}!")
        root.destroy()  
        ventana_menú()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def ventana_menú():
    global root2
    root2 = ctk.CTk()
    root2.title("Menú principal")
    root2.geometry("695x695") 
    root2.configure(fg_color="#B3B792")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root2.winfo_screenwidth()
    alto_pantalla = root2.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root2.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root2.resizable(width=False, height=False)

    menú = ctk.CTkLabel(master=root2, text=" Menú principal ", font=("Calligraphy", 72 ), text_color="#2c3424", fg_color="#B3B792", anchor="center", width=675)
    menú.place(x=0, y=30)

    ruta_imagen = ruta_recurso("Imagenes_app/Ingresos.jpeg")
    imagen1 = Image.open(ruta_imagen)
    imagen1 = imagen1.resize((150, 180)) 
    imagen1_tk = ImageTk.PhotoImage(imagen1)
    boton_imagen_ingresos = ctk.CTkButton(master=root2, image=imagen1_tk, text="", fg_color="#B3B792", hover_color="#8C916C", width=150, height=180, command=ventana_ingresos)
    boton_imagen_ingresos.image = imagen1_tk 
    boton_imagen_ingresos.place(x=30, y=220)

    ruta_imagen = ruta_recurso("Imagenes_app/gastoos.jpeg")
    imagen2 = Image.open(ruta_imagen)
    imagen2 = imagen2.resize((150, 180))
    imagen2_tk = ImageTk.PhotoImage(imagen2)
    boton_imagen_gastos = ctk.CTkButton(master=root2, image=imagen2_tk, text="", fg_color="#B3B792", hover_color="#8C916C", width=150, height=180, command=ventana_gastos)
    boton_imagen_gastos.image = imagen2_tk  
    boton_imagen_gastos.place(x=195, y=220)

    ruta_imagen = ruta_recurso("Imagenes_app/Controol.jpeg")
    imagen3 = Image.open(ruta_imagen)
    imagen3 = imagen3.resize((150, 180))
    imagen3_tk = ImageTk.PhotoImage(imagen3)
    boton_imagen_control = ctk.CTkButton(master=root2, image=imagen3_tk, text="", fg_color="#B3B792", hover_color="#8C916C", width=150, height=180, command=ventana_control)
    boton_imagen_control.image = imagen3_tk
    boton_imagen_control.place(x=360, y=220)

    ruta_imagen = ruta_recurso("Imagenes_app/Ahorros.jpeg")
    imagen4 = Image.open(ruta_imagen)
    imagen4 = imagen4.resize((150, 180))
    imagen4_tk = ImageTk.PhotoImage(imagen4)
    boton_imagen_ahorros = ctk.CTkButton(master=root2, image=imagen4_tk, text="", fg_color="#B3B792", hover_color="#8C916C", width=150, height=180, command=ventana_ahorros)
    boton_imagen_ahorros.image = imagen4_tk  
    boton_imagen_ahorros.place(x=525, y=220)

    boton_ingresos = ctk.CTkButton(master=root2, text="Ingresos", fg_color="#2c3424", bg_color="#B3B792", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#8C916C", width=130, height=35, command=ventana_ingresos)
    boton_ingresos.place(x=30, y=220 + 180 + 20)

    boton_gastos = ctk.CTkButton(master=root2, text="Gastos", fg_color="#2c3424", bg_color="#B3B792", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#8C916C", width=130, height=35, command=ventana_gastos)
    boton_gastos.place(x=205, y=220 + 180 + 20)

    boton_control_de_gastos = ctk.CTkButton(master=root2, text="Control de\nGastos", fg_color="#2c3424", bg_color="#B3B792", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#8C916C", width=130, height=35, command=ventana_control)
    boton_control_de_gastos.place(x=370, y=220 + 180 + 20)

    boton_ahorro = ctk.CTkButton(master=root2, text="Ahorro", fg_color="#2c3424", bg_color="#B3B792", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#8C916C", width=130, height=35, command=ventana_ahorros)
    boton_ahorro.place(x=535, y=220 + 180 + 20)

    boton_cerrar_sesión = ctk.CTkButton(master=root2, text="Salir", fg_color="#2c3424", bg_color="#B3B792", text_color="#B3B792", font=("Century Gothic", 20), hover_color="#8C916C", width=195, height=35, command=lambda:cerrar_sesion(root2))
    boton_cerrar_sesión.place(x=250, y=300 + 180 + 80)

    root2.mainloop()

def ventana_ingresos():
    global root4
    root2.destroy()
    root4 = ctk.CTk()
    root4.title("Ingresos")
    root4.geometry("695x695")
    root4.config(bg="#BFC4B0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root4.winfo_screenwidth()
    alto_pantalla = root4.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root4.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root4.resizable(width=False, height=False)

    etiqueta_ingesos = tk.Label(root4, text=" Ingresos", font=("Calligraphy", 72), fg="#2c3424", bg="#BFC4B0")
    etiqueta_ingesos.place(x=270, y=45)

    boton_agregar_ingreso = ctk.CTkButton(master=root4, text="Agregar nuevo ingreso", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", width=260, height=32, command=ventana_agregar_ingreso)
    boton_agregar_ingreso.place(x=350, y=180)

    boton_modificar_ingreso = ctk.CTkButton(master=root4, text="Modificar ingreso", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", width=260, height=32, command=ventana_modificar_ingreso)
    boton_modificar_ingreso.place(x=350, y=290)

    boton_consultar_ingreso_individual = ctk.CTkButton(master=root4, text="Consultar ingreso (individual)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", width=260, height=32, command=ventana_consultar_ingreso_individual)
    boton_consultar_ingreso_individual.place(x=350, y=410)

    boton_consultar_ingreso_grupal = ctk.CTkButton(master=root4, text="Consultar ingreso (grupal)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", width=260, height=32, command=ventana_consultar_ingreso_grupal)
    boton_consultar_ingreso_grupal.place(x=350, y=540)

    boton_regresar = ctk.CTkButton(master=root4, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root4))
    boton_regresar.place(x=280, y=640)

    ruta_imagen = ruta_recurso("Imagenes_app/credito.jpeg")
    imagen5 = Image.open(ruta_imagen)
    imagen5 = imagen5.resize((210, 130))
    imagen5_tk = ImageTk.PhotoImage(imagen5)
    label_imagen = tk.Label(root4, image=imagen5_tk, bg="#BFC4B0")
    label_imagen.image = imagen5_tk
    label_imagen.place(x=130, y=165)

    ruta_imagen = ruta_recurso("Imagenes_app/modificaar.jpeg")
    imagen6 = Image.open(ruta_imagen)
    imagen6 = imagen6.resize((210, 120))
    imagen6_tk = ImageTk.PhotoImage(imagen6)
    label_imagen = tk.Label(root4, image=imagen6_tk, bg="#BFC4B0")
    label_imagen.image = imagen6_tk
    label_imagen.place(x=130, y=320)
    
    ruta_imagen = ruta_recurso("Imagenes_app/individual.jpeg")
    imagen7 = Image.open(ruta_imagen)
    imagen7 = imagen7.resize((210, 150))
    imagen7_tk = ImageTk.PhotoImage(imagen7)
    label_imagen = tk.Label(root4, image=imagen7_tk, bg="#BFC4B0")
    label_imagen.image = imagen7_tk
    label_imagen.place(x=130, y=470)

    ruta_imagen = ruta_recurso("Imagenes_app/grupal.png")
    imagen8 = Image.open(ruta_imagen)
    imagen8 = Image.open("C://Users//maxim//OneDrive//Escritorio//mafer´s folder//Imagenes_app//grupal.png")
    imagen8 = imagen8.resize((210, 150))
    imagen8_tk = ImageTk.PhotoImage(imagen8)
    label_imagen = tk.Label(root4, image=imagen8_tk, bg="#BFC4B0")
    label_imagen.image = imagen8_tk
    label_imagen.place(x=130, y=630)

    root4.mainloop()

def ventana_agregar_ingreso():
    global root9
    root4.destroy()
    root9 = ctk.CTk()
    root9.title("Agregar nuevo ingreso")
    root9.geometry("695x695")
    root9.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root9.winfo_screenwidth()
    alto_pantalla = root9.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root9.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root9.resizable(width=False, height=False)

    etiqueta_agregar = ctk.CTkLabel(master=root9, text="Agregar ingreso", font=("Vendya", 50, "bold"), bg_color="#EADED0", text_color="#8C916C", anchor="center", width=675)
    etiqueta_agregar.place(x=15, y=100)

    marco = tk.Frame(root9, bg="#EADED0")
    marco.place(relx=0.5, rely=0.5, anchor="center") 

    etiqueta_tipo_de_ingreso = tk.Label(marco, text="Tipo de ingreso:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_tipo_de_ingreso.pack(pady=(0, 5))
    boton_de_opciones = ctk.CTkComboBox(marco, fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 22), width=180, 
                                        values=["Salario", "Beca", "Pensión", "Bonificación", "Prestamos", "Otros"], 
                                        dropdown_font=("Century Gothic", 18), dropdown_text_color="#0D2207", dropdown_hover_color="#8C916C",
                                        dropdown_fg_color="#EADED0", button_color="#93948F")
    boton_de_opciones.pack(pady=(0, 20))


    etiqueta_ingresa_cantidad = tk.Label(marco, text="Cantidad:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_ingresa_cantidad.pack(pady=(0, 5))
    entrada_cant = ctk.CTkEntry(marco, fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), width=180)
    entrada_cant.pack(pady=(0, 20))

    def registrar_ingreso():
        tipo = boton_de_opciones.get()
        cantidad_str = entrada_cant.get()

        if not tipo or not cantidad_str:
            messagebox.showerror("Error", "Debes completar todos los campos.")
            return

        try:
            cantidad = float(cantidad_str)
            exito = guardar_ingreso(tipo, cantidad, fecha_actual)
            if exito:
                messagebox.showinfo("Éxito", "Ingreso guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el ingreso.")
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")

    fecha_actual = datetime.today().strftime('%Y-%m-%d')  # Formato YYYY-MM-DD
    etiqueta_fecha = tk.Label(marco, text=f"Fecha: {fecha_actual}", font=("Century Gothic", 20), fg="#8C916C", bg="#EADED0")
    etiqueta_fecha.pack(pady=(0, 20))

    boton_guardar_ingresos = ctk.CTkButton(master=root9, text="Registrar ingreso", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=registrar_ingreso)
    boton_guardar_ingresos.place(x=260, y=550)

    boton_regresaar = ctk.CTkButton(master=root9, text="Regresar", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=lambda:regresar(root9))
    boton_regresaar.place(x=280, y=600)

    root9.mainloop()

def ventana_modificar_ingreso():
    root4.destroy()
    root10 = ctk.CTk()
    root10.title("Modificar ingreso")
    root10.geometry("695x695")
    root10.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root10.winfo_screenwidth()
    alto_pantalla = root10.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root10.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root10.resizable(width=False, height=False)

    
    etiqueta = ctk.CTkLabel(root10, text="Modificar ingreso", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root10, bg="#EADED0")
    marco.pack()

    style = ttk.Style()
    style.configure("Custom.Treeview",
                background="#EADED0",        
                foreground="#0D2207",       
                rowheight=30,
                fieldbackground="#EADED0") 

    style.map("Custom.Treeview", background=[("selected", "#8C916C")])

    tree = ttk.Treeview(marco, columns=("tipo", "cantidad", "fecha"), show="headings", height=8, style="Custom.Treeview" )
    tree.heading("tipo", text="Tipo")
    tree.heading("cantidad", text="Cantidad")
    tree.heading("fecha", text="Fecha")

    tree.column("tipo", width=150, anchor="center")
    tree.column("cantidad", width=100, anchor="center")
    tree.column("fecha", width=120, anchor="center")

    tree.pack(pady=20)

    tipo_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    fecha_var = tk.StringVar()

    tipo_label = ctk.CTkLabel(marco, text="Nuevo tipo:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    tipo_label.pack()
    tipo_entry = ctk.CTkEntry(marco, textvariable=tipo_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    tipo_entry.pack(pady=5)

    cantidad_label = ctk.CTkLabel(marco, text="Nueva cantidad:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_label.pack()
    cantidad_entry = ctk.CTkEntry(marco, textvariable=cantidad_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_entry.pack(pady=5)

    fecha_label = ctk.CTkLabel(marco, text="Fecha (YYYY-MM-DD):", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    fecha_label.pack()
    fecha_entry = ctk.CTkEntry(marco, textvariable=fecha_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    fecha_entry.pack(pady=5)

    # Cargar ingresos del usuario
    ingresos = cargar_ingresos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista_actual = ingresos.get(usuario_id, [])

    for i, ingreso in enumerate(lista_actual):
        tipo = ingreso["tipo"]
        cantidad = ingreso["cantidad"]
        fecha = ingreso.get("fecha", "Sin fecha")
        tree.insert("", "end", iid=i, values=(tipo, cantidad, fecha))

    def seleccionar_ingreso(event):
        seleccionado = tree.focus()  # obtiene el item seleccionado
        if not seleccionado:
            return
        index = int(seleccionado)
        ingreso = lista_actual[index]
        tipo_var.set(ingreso["tipo"])
        cantidad_var.set(str(ingreso["cantidad"]))
        fecha_var.set(ingreso.get("fecha", ""))

    tree.bind("<<TreeviewSelect>>", seleccionar_ingreso)

    def guardar_cambios():
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showerror("Error", "Selecciona un ingreso para modificar.")
            return

        try:
            index = int(seleccionado)
        except ValueError:
            messagebox.showerror("Error", "Selección inválida.")
            return

        nuevo_tipo = tipo_var.get().strip()
        nueva_cantidad_str = cantidad_var.get().strip()
        nueva_fecha = fecha_var.get().strip()

        if not nuevo_tipo or not nueva_cantidad_str or not nueva_fecha:
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        try:
            nueva_cantidad = float(nueva_cantidad_str)
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")
            return
        
        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Usa el formato YYYY-MM-DD.")
            return

        lista_actual[index] = {"tipo": nuevo_tipo, "cantidad": nueva_cantidad, "fecha": nueva_fecha}
        ingresos = cargar_ingresos()
        usuario_id = Usuario.usuario_actual.usuario_id
        ingresos[usuario_id] = lista_actual

        with open(ruta_ingresos, "w", encoding="utf-8") as archivo:
            json.dump(ingresos, archivo, indent=4, ensure_ascii=False)

        tree.item(index, values=(nuevo_tipo, nueva_cantidad, nueva_fecha))

        messagebox.showinfo("Éxito", "Ingreso modificado correctamente.")
        ventana_modificar_ingreso()  # Recargar la ventana

    boton_guardar = ctk.CTkButton(root10, text="Guardar cambios", command=guardar_cambios,
                                  fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289")
    boton_guardar.pack(pady=20)

    boton_regresar = ctk.CTkButton(root10, text="Regresar", command=lambda: regresar(root10),
                                   fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289")
    boton_regresar.pack()

    root10.mainloop()

def ventana_consultar_ingreso_individual():
    root4.destroy()
    root11 = ctk.CTk()
    root11.title("Consultar ingreso individual")
    root11.geometry("695x695")
    root11.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root11.winfo_screenwidth()
    alto_pantalla = root11.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root11.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root11.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root11, text="Consultar ingresos", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root11, bg="#EADED0")
    marco.pack()

    total = calcular_total_ingresos()
    etiqueta_total = tk.Label(marco, text=f"Total ingresos: ${total:.2f}", font=("Century Gothic", 20),
                            fg="#0D2207", bg="#EADED0")
    etiqueta_total.pack(pady=(10, 5))

    total = calcular_total_ingresos()
    etiqueta_total.config(text=f"Total ingresos: ${total:.2f}")

    agrupados = agrupar_ingresos_por_tipo_con_fecha()

    etiqueta_titulo_detalle = tk.Label(marco, text="Detalle por tipo:",
                                    font=("Century Gothic", 18, "bold"), fg="#8C916C", bg="#EADED0")
    etiqueta_titulo_detalle.pack(pady=(15, 5))

    for tipo, ingresos in agrupados.items():
        etiqueta_tipo = tk.Label(marco, text=f"{tipo}:", font=("Century Gothic", 17, "bold"),
                                fg="#103107", bg="#EADED0", anchor="w", justify="left")
        etiqueta_tipo.pack(anchor="w", padx=20)

        for ingreso in ingresos:
            cantidad, fecha = ingreso
            etiqueta_detalle = tk.Label(marco, text=f"    ★ ${cantidad:.2f} el {fecha}",
                                        font=("Century Gothic", 15), fg="#0D2207", bg="#EADED0",
                                        anchor="w", justify="left")
            etiqueta_detalle.pack(anchor="w", padx=40)

    boton_regresaar = ctk.CTkButton(master=root11, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root11))
    boton_regresaar.place(x=280, y=640)

    root11.mainloop()

def ventana_consultar_ingreso_grupal():
    root4.destroy()
    root12 = ctk.CTk()
    root12.title("Consultar ingreso grupal")
    root12.geometry("695x695")
    root12.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root12.winfo_screenwidth()
    alto_pantalla = root12.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root12.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root12.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root12, text="Consultar ingresos (grupales)", font=("Vendya", 40, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    lo_sentimos = ctk.CTkLabel(root12, text="Las funciones grupales serán habilitadas pronto!\nLamentamos las molestias que esto pueda ocasionar,\npor lo mientras disfruta de nuestras increibles funciones individuales",
                            font=("Century Gothic", 18), text_color="#897F73", bg_color="#EADED0")
    lo_sentimos.pack(pady=180)

    boton_regresaar = ctk.CTkButton(master=root12, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root12))
    boton_regresaar.place(x=280, y=640)

    root12.mainloop()

def ventana_gastos():
    global root5
    root2.destroy()
    root5 = ctk.CTk()
    root5.title("Gastos")
    root5.geometry("695x695")
    root5.config(bg="#BFC4B0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root5.winfo_screenwidth()
    alto_pantalla = root5.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root5.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root5.resizable(width=False, height=False)

    ruta_imagen = ruta_recurso("Imagenes_app/gastosgrup.png")
    imagen11 = Image.open(ruta_imagen)
    imagen11 = imagen11.resize((130, 170))
    imagen11_tk = ImageTk.PhotoImage(imagen11)
    label_imagen = tk.Label(root5, image=imagen11_tk, bg="#BFC4B0")
    label_imagen.image = imagen11_tk
    label_imagen.place(x=160, y=630)

    ruta_imagen = ruta_recurso("Imagenes_app/gastosind.png")
    imagen12 = Image.open(ruta_imagen)
    imagen12 = imagen12.resize((180, 130))
    imagen12_tk = ImageTk.PhotoImage(imagen12)
    label_imagen = tk.Label(root5, image=imagen12_tk, bg="#BFC4B0")
    label_imagen.image = imagen12_tk
    label_imagen.place(x=130, y=470)

    ruta_imagen = ruta_recurso("Imagenes_app/mod.png")
    imagen13 = Image.open(ruta_imagen)
    imagen13 = imagen13.resize((180, 130))
    imagen13_tk = ImageTk.PhotoImage(imagen13)
    label_imagen = tk.Label(root5, image=imagen13_tk, bg="#BFC4B0")
    label_imagen.image = imagen13_tk
    label_imagen.place(x=130, y=320)

    ruta_imagen = ruta_recurso("Imagenes_app/agrg.png")
    imagen14 = Image.open(ruta_imagen)
    imagen14 = imagen14.resize((180, 130))
    imagen14_tk = ImageTk.PhotoImage(imagen14)
    label_imagen = tk.Label(root5, image=imagen14_tk, bg="#BFC4B0")
    label_imagen.image = imagen14_tk
    label_imagen.place(x=130, y=165)

    etiqueta_gastos = tk.Label(root5, text=" Gastos", font=("Calligraphy", 72), fg="#2c3424", bg="#BFC4B0")
    etiqueta_gastos.place(x=270, y=35)

    boton_agregar_gasto = ctk.CTkButton(master=root5, text="Agregar gasto", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_agregar_gastos)
    boton_agregar_gasto.place(x=350, y=180)

    boton_modificar_gasto = ctk.CTkButton(master=root5, text="Modificar gasto", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_modificar_gastos)
    boton_modificar_gasto.place(x=350, y=290)

    boton_consultar_gasto_individual = ctk.CTkButton(master=root5, text="Consultar gastos (individuales)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command= ventana_consultar_gasto_individual)
    boton_consultar_gasto_individual.place(x=350, y=410)

    boton_consultar_gasto_grupal = ctk.CTkButton(master=root5, text="Consultar gastos (grupales)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_consultar_gasto_grupal)
    boton_consultar_gasto_grupal.place(x=350, y=540)

    boton_regresar = ctk.CTkButton(master=root5, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root5))
    boton_regresar.place(x=280, y=640)

    root5.mainloop()

def ventana_agregar_gastos():
    root5.destroy()
    root13 = ctk.CTk()
    root13.title("Agregar gasto")
    root13.geometry("695x695")
    root13.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root13.winfo_screenwidth()
    alto_pantalla = root13.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root13.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root13.resizable(width=False, height=False)

    etiquetaa = ctk.CTkLabel(root13, text="Agregar gasto", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiquetaa.place(x=185, y=100)

    marco = tk.Frame(root13, bg="#EADED0")
    marco.place(relx=0.5, rely=0.5, anchor="center") 

    etiqueta_tipo_de_gasto = tk.Label(marco, text="Tipo de gasto:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_tipo_de_gasto.pack(pady=(0, 5))
    boton_de_opcionees = ctk.CTkComboBox(marco, fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 22), width=180, 
                                        values=["Academico", "Social", "Ropa", "Comida", "Pagos", "Gastos de la casa", "Otros"], 
                                        dropdown_font=("Century Gothic", 18), dropdown_text_color="#0D2207", dropdown_hover_color="#8C916C",
                                        dropdown_fg_color="#EADED0", button_color="#93948F")
    boton_de_opcionees.pack(pady=(0, 20))


    etiqueta_ingresa_cantidaad = tk.Label(marco, text="Cantidad:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_ingresa_cantidaad.pack(pady=(0, 5))
    entrada_canti = ctk.CTkEntry(marco, fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), width=180)
    entrada_canti.pack(pady=(0, 20))

    def registrar_gasto():
        tipo = boton_de_opcionees.get()
        cantidad_str = entrada_canti.get()

        if not tipo or not cantidad_str:
            messagebox.showerror("Error", "Debes completar todos los campos.")
            return

        try:
            cantidad = float(cantidad_str)
            exito = guardar_gasto(tipo, cantidad, fecha_actual)
            if exito:
                messagebox.showinfo("Éxito", "Gasto guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el gasto.")
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")

    fecha_actual = datetime.today().strftime('%Y-%m-%d') 
    etiqueta_fecha = tk.Label(marco, text=f"Fecha: {fecha_actual}", font=("Century Gothic", 20), fg="#8C916C", bg="#EADED0")
    etiqueta_fecha.pack(pady=(0, 20))

    boton_guardar_gastos = ctk.CTkButton(master=root13, text="Registrar gasto", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=registrar_gasto)
    boton_guardar_gastos.place(x=268, y=550)

    boton_regresaar = ctk.CTkButton(master=root13, text="Regresar", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=lambda:regresar(root13))
    boton_regresaar.place(x=280, y=600)

    root13.mainloop()

def ventana_modificar_gastos():
    root5.destroy()
    root14 = ctk.CTk()
    root14.title("Modificar gasto")
    root14.geometry("695x695")
    root14.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root14.winfo_screenwidth()
    alto_pantalla = root14.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root14.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root14.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root14, text="Modificar gastos", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root14, bg="#EADED0")
    marco.pack()

    style = ttk.Style()
    style.configure("Custom.Treeview",
                background="#EADED0",        
                foreground="#0D2207",       
                rowheight=30,
                fieldbackground="#EADED0") 

    style.map("Custom.Treeview", background=[("selected", "#8C916C")])

    tree_gastos = ttk.Treeview(marco, columns=("tipo", "cantidad", "fecha"), show="headings", height=8, style="Custom.Treeview" )
    tree_gastos.heading("tipo", text="Tipo")
    tree_gastos.heading("cantidad", text="Cantidad")
    tree_gastos.heading("fecha", text="Fecha")

    tree_gastos.column("tipo", width=150, anchor="center")
    tree_gastos.column("cantidad", width=100, anchor="center")
    tree_gastos.column("fecha", width=120, anchor="center")

    tree_gastos.pack(pady=20)

    tipo_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    fecha_var = tk.StringVar()

    tipo_label = ctk.CTkLabel(marco, text="Nuevo tipo:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    tipo_label.pack()
    tipo_entry = ctk.CTkEntry(marco, textvariable=tipo_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    tipo_entry.pack(pady=5)

    cantidad_label = ctk.CTkLabel(marco, text="Nueva cantidad:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_label.pack()
    cantidad_entry = ctk.CTkEntry(marco, textvariable=cantidad_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_entry.pack(pady=5)

    fecha_label = ctk.CTkLabel(marco, text="Fecha (YYYY-MM-DD):", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    fecha_label.pack()
    fecha_entry = ctk.CTkEntry(marco, textvariable=fecha_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    fecha_entry.pack(pady=5)

    # Cargar gastos del usuario
    gastos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista_actual = gastos.get(usuario_id, [])

    for i, gastos in enumerate(lista_actual):
        tipo = gastos["tipo"]
        cantidad = gastos["cantidad"]
        fecha = gastos.get("fecha", "Sin fecha")
        tree_gastos.insert("", "end", iid=i, values=(tipo, cantidad, fecha))

    def seleccionar_gasto(event):
        seleccionado = tree_gastos.focus() 
        if not seleccionado:
            return
        index = int(seleccionado)
        gasto = lista_actual[index]
        tipo_var.set(gasto["tipo"])
        cantidad_var.set(str(gasto["cantidad"]))
        fecha_var.set(gasto.get("fecha", ""))

    tree_gastos.bind("<<TreeviewSelect>>", seleccionar_gasto)

    def guardar_cambioos():
        seleccionadoo = tree_gastos.focus()
        if not seleccionadoo:
            messagebox.showerror("Error", "Selecciona un ingreso para modificar.")
            return

        try:
            index = int(seleccionadoo)
        except ValueError:
            messagebox.showerror("Error", "Selección inválida.")
            return

        nuevo_tipo = tipo_var.get().strip()
        nueva_cantidad_str = cantidad_var.get().strip()
        nueva_fecha = fecha_var.get().strip()

        if not nuevo_tipo or not nueva_cantidad_str or not nueva_fecha:
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        try:
            nueva_cantidad = float(nueva_cantidad_str)
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")
            return
        
        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Usa el formato YYYY-MM-DD.")
            return

        lista_actual[index] = {"tipo": nuevo_tipo, "cantidad": nueva_cantidad, "fecha": nueva_fecha}
        gastos = cargar_gastos()
        usuario_id = Usuario.usuario_actual.usuario_id
        gastos[usuario_id] = lista_actual

        with open(ruta_gastos, "w", encoding="utf-8") as archivo:
            json.dump(gastos, archivo, indent=4, ensure_ascii=False)

        tree_gastos.item(index, values=(nuevo_tipo, nueva_cantidad, nueva_fecha))

        messagebox.showinfo("Éxito", "Gasto modificado correctamente.")
        ventana_modificar_ingreso()  

    boton_guardar = ctk.CTkButton(root14, text="Guardar cambios", command=guardar_cambioos,
                                  fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289")
    boton_guardar.pack(pady=20)

    boton_regresar = ctk.CTkButton(root14, text="Regresar", command=lambda: regresar(root14),
                                   fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289")
    boton_regresar.pack()

    root14.mainloop()

def ventana_consultar_gasto_individual():
    root5.destroy()
    root15 = ctk.CTk()
    root15.title("Modificar gasto individual")
    root15.geometry("695x695")
    root15.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root15.winfo_screenwidth()
    alto_pantalla = root15.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root15.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root15.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root15, text="Consultar gastos", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root15, bg="#EADED0")
    marco.pack()

    total = calcular_total_gastos()
    etiqueta_total = tk.Label(marco, text=f"Total de gastos: ${total:.2f}", font=("Century Gothic", 20),
                            fg="#0D2207", bg="#EADED0")
    etiqueta_total.pack(pady=(10, 5))

    total = calcular_total_gastos()
    etiqueta_total.config(text=f"Total de gastos: ${total:.2f}")

    agrupados = agrupar_gastos_por_tipo_con_fecha()

    etiqueta_titulo_detalle = tk.Label(marco, text="Detalle por tipo:",
                                    font=("Century Gothic", 18, "bold"), fg="#8C916C", bg="#EADED0")
    etiqueta_titulo_detalle.pack(pady=(15, 5))

    for tipo, gastos in agrupados.items():
        etiqueta_tipo = tk.Label(marco, text=f"{tipo}:", font=("Century Gothic", 17, "bold"),
                                fg="#103107", bg="#EADED0", anchor="w", justify="left")
        etiqueta_tipo.pack(anchor="w", padx=20)

        for gasto in gastos:
            cantidad, fecha = gasto
            etiqueta_detalle = tk.Label(marco, text=f"    ★ ${cantidad:.2f} el {fecha}",
                                        font=("Century Gothic", 15), fg="#0D2207", bg="#EADED0",
                                        anchor="w", justify="left")
            etiqueta_detalle.pack(anchor="w", padx=40)

    boton_regresaar = ctk.CTkButton(master=root15, text="Regresar", fg_color="#2c3424", bg_color="#EADED0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root15))
    boton_regresaar.place(x=280, y=640)

    root15.mainloop()

def ventana_consultar_gasto_grupal():
    root5.destroy()
    root16 = ctk.CTk()
    root16.title("Modificar gasto individual")
    root16.geometry("695x695")
    root16.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root16.winfo_screenwidth()
    alto_pantalla = root16.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root16.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root16.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root16, text="Consultar gastos (grupales)", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    lo_sentimos = ctk.CTkLabel(root16, text="Las funciones grupales serán habilitadas pronto!\nLamentamos las molestias que esto pueda ocasionar,\npor lo mientras disfruta de nuestras increibles funciones individuales",
                            font=("Century Gothic", 18), text_color="#897F73", bg_color="#EADED0")
    lo_sentimos.pack(pady=180)

    boton_regresaar = ctk.CTkButton(master=root16, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root16))
    boton_regresaar.place(x=280, y=640)

    root16.mainloop()
    

def ventana_control():
    global root6
    global root6
    root2.destroy()
    root6 = ctk.CTk()
    root6.title("Control de gastos")
    root6.geometry("695x695")
    root6.config(bg="#BFC4B0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root6.winfo_screenwidth()
    alto_pantalla = root6.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root6.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root6.resizable(width=False, height=False)

    etiqueta_control = tk.Label(root6, text=" Control de Gastos", font=("Calligraphy", 72), fg="#2c3424", bg="#BFC4B0")
    etiqueta_control.place(x=75, y=45)

    ruta_imagen = ruta_recurso("Imagenes_app/alertas.png")
    imagen9 = Image.open(ruta_imagen)
    imagen9 = imagen9.resize((180, 180))
    imagen9_tk = ImageTk.PhotoImage(imagen9)
    label_imagen = tk.Label(root6, image=imagen9_tk, bg="#BFC4B0")
    label_imagen.image = imagen9_tk
    label_imagen.place(x=345, y=500)

    ruta_imagen = ruta_recurso("Imagenes_app/analisis.png")
    imagen10 = Image.open(ruta_imagen)
    imagen10 = imagen10.resize((180, 180))
    imagen10_tk = ImageTk.PhotoImage(imagen10)
    label_imagen = tk.Label(root6, image=imagen10_tk, bg="#BFC4B0")
    label_imagen.image = imagen10_tk
    label_imagen.place(x=345, y=220)

    boton_analisis_gasto = ctk.CTkButton(master=root6, text="Análisis ingresos vs gastos", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_de_analisis)
    boton_analisis_gasto.place(x=230, y=335)

    boton_alertas_gasto = ctk.CTkButton(master=root6, text="Consultar alertas!!!", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", width=230, height=32, command=ventana_de_alertas)
    boton_alertas_gasto.place(x=235, y=560)

    boton_regresar = ctk.CTkButton(master=root6, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=lambda:regresar(root6))
    boton_regresar.place(x=280, y=640)

    root6.mainloop()

def ventana_de_analisis():
    global root6, root17
    root6.destroy()
    root17 = ctk.CTk()
    root17.title("Ventana de analisis")
    root17.geometry("695x695")
    root17.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root17.winfo_screenwidth()
    alto_pantalla = root17.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root17.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root17.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root17, text="Analisis ingresos vs gastos", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    usuario_id = Usuario.usuario_actual.usuario_id
    total_ingresos, total_gastos = calcular_totales_ingresos_vs_gastos(usuario_id)
    resumen_ingresos, resumen_gastos = resumen_por_tipo(usuario_id)

    ctk.CTkLabel(root17, text=f"Total Ingresos: ${total_ingresos:.2f}", font=("Century Gothic", 20),
                 text_color="#0D2207", bg_color="#EADED0").pack(pady=10)
    ctk.CTkLabel(root17, text=f"Total Gastos: ${total_gastos:.2f}", font=("Century Gothic", 20),
                 text_color="#0D2207", bg_color="#EADED0").pack(pady=10)

    ctk.CTkLabel(root17, text="Detalle por tipo de ingreso:", font=("Century Gothic", 18, "bold"),
                 text_color="#8C916C", bg_color="#EADED0").pack(pady=5)
    for tipo, total in resumen_ingresos.items():
        ctk.CTkLabel(root17, text=f"- {tipo}: ${total:.2f}", font=("Century Gothic", 16),
                     text_color="#0D2207", bg_color="#EADED0").pack()

    ctk.CTkLabel(root17, text="Detalle por tipo de gasto:", font=("Century Gothic", 18, "bold"),
                 text_color="#8C916C", bg_color="#EADED0").pack(pady=10)
    for tipo, total in resumen_gastos.items():
        ctk.CTkLabel(root17, text=f"- {tipo}: ${total:.2f}", font=("Century Gothic", 16),
                     text_color="#0D2207", bg_color="#EADED0").pack()

    ctk.CTkButton(root17, text="Regresar", command=lambda: regresar(root17),
                  fg_color="#8C916C", text_color="#0D2207", hover_color="#646954", font=("Century Gothic", 18)).pack(pady=20)

    root17.mainloop()


def ventana_de_alertas():
    root6.destroy()
    root18 = ctk.CTk()
    root18.title("Alertas")
    root18.geometry("695x695")
    root18.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root18.winfo_screenwidth()
    alto_pantalla = root18.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root18.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root18.resizable(width=False, height=False)

    usuario_id = Usuario.usuario_actual.usuario_id
    ingresos, gastos = calcular_totales_ingresos_vs_gastos(usuario_id)
    estado_alerta = gastos > ingresos

    if estado_alerta:
        mensaje = "⚠️ Estás gastando más de lo que ingresas"
        color = "#700707"
    else:
        mensaje = "✅ Todo en orden, sigue así"
        color = "#061801"

    ctk.CTkLabel(root18, text=mensaje, font=("Century Gothic", 22, "bold"),
                 text_color=color, bg_color="#EADED0").pack(pady=300)

    ctk.CTkButton(root18, text="Regresar", command=lambda: regresar(root18),
                  fg_color="#8C916C", text_color="#0D2207", hover_color="#646954",
                  font=("Century Gothic", 18)).place(x=275, y=360)

    root18.mainloop()

def ventana_ahorros():
    global root7
    root2.destroy()
    root7 = ctk.CTk()
    root7.title("Ahorros")
    root7.geometry("695x695")
    root7.config(bg="#BFC4B0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root7.winfo_screenwidth()
    alto_pantalla = root7.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root7.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root7.resizable(width=False, height=False)

    etiqueta_ahorro = tk.Label(root7, text=" Ahorro", font=("Calligraphy", 72), fg="#2c3424", bg="#BFC4B0")
    etiqueta_ahorro.place(x=270, y=35)

    ruta_imagen = ruta_recurso("Imagenes_app/ahorroind.png")
    imagen15 = Image.open(ruta_imagen)
    imagen15 = imagen15.resize((180, 130))
    imagen15_tk = ImageTk.PhotoImage(imagen15)
    label_imagen = tk.Label(root7, image=imagen15_tk, bg="#BFC4B0")
    label_imagen.image = imagen15_tk
    label_imagen.place(x=130, y=470)

    ruta_imagen = ruta_recurso("Imagenes_app/ahorrogrup.png")
    imagen16 = Image.open(ruta_imagen)
    imagen16 = imagen16.resize((180, 130))
    imagen16_tk = ImageTk.PhotoImage(imagen16)
    label_imagen = tk.Label(root7, image=imagen16_tk, bg="#BFC4B0")
    label_imagen.image = imagen16_tk
    label_imagen.place(x=130, y=630)

    ruta_imagen = ruta_recurso("Imagenes_app/agregar.png")
    imagen17 = Image.open(ruta_imagen)
    imagen17 = imagen17.resize((180, 130))
    imagen17_tk = ImageTk.PhotoImage(imagen17)
    label_imagen = tk.Label(root7, image=imagen17_tk, bg="#BFC4B0")
    label_imagen.image = imagen17_tk
    label_imagen.place(x=130, y=165)

    ruta_imagen = ruta_recurso("Imagenes_app/modificar.png")
    imagen18 = Image.open(ruta_imagen)
    imagen18 = imagen18.resize((190, 140))
    imagen18_tk = ImageTk.PhotoImage(imagen18)
    label_imagen = tk.Label(root7, image=imagen18_tk, bg="#BFC4B0")
    label_imagen.image = imagen18_tk
    label_imagen.place(x=130, y=320)

    boton_agregar_ahorro = ctk.CTkButton(master=root7, text="Agregar ahorro", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_agregrar_ahorro)
    boton_agregar_ahorro.place(x=350, y=180)

    boton_modificar_ahorro = ctk.CTkButton(master=root7, text="Modificar ahorro", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_modificar_ahorro)
    boton_modificar_ahorro.place(x=350, y=290)

    boton_consultar_ahorro_individual = ctk.CTkButton(master=root7, text="Consultar ahorro (individual)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_consultar_ahorro)
    boton_consultar_ahorro_individual.place(x=350, y=410)

    boton_consultar_ahorro_grupal = ctk.CTkButton(master=root7, text="Consultar ahorro (grupal)", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", height=32, command=ventana_consultar_ahorro_grupal)
    boton_consultar_ahorro_grupal.place(x=350, y=540)

    boton_regresar = ctk.CTkButton(master=root7, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root7))
    boton_regresar.place(x=280, y=640)

    root7.mainloop()

def ventana_agregrar_ahorro():
    root7.destroy()
    root19 = ctk.CTk()
    root19.title("Agregar ahorro")
    root19.geometry("695x695")
    root19.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root19.winfo_screenwidth()
    alto_pantalla = root19.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root19.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root19.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root19, text="Agregar ahorro", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.place(x=185, y=100)

    marco = tk.Frame(root19, bg="#EADED0")
    marco.place(relx=0.5, rely=0.5, anchor="center") 

    etiqueta_tipo_de_ahorro = tk.Label(marco, text="Ingreso del que proviene el ahorro:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_tipo_de_ahorro.pack(pady=(0, 5))
    boton_de_opcionees = ctk.CTkComboBox(marco, fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 22), width=180, 
                                        values=["Salario", "Beca", "Pensión", "Bonificación", "Prestamos", "Otros"], 
                                        dropdown_font=("Century Gothic", 18), dropdown_text_color="#0D2207", dropdown_hover_color="#8C916C",
                                        dropdown_fg_color="#EADED0", button_color="#93948F")
    boton_de_opcionees.pack(pady=(0, 20))


    etiqueta_ingresa_cantidaad = tk.Label(marco, text="Cantidad:", font=("Century Gothic", 25), fg="#8C916C", bg="#EADED0")
    etiqueta_ingresa_cantidaad.pack(pady=(0, 5))
    entrada_canti = ctk.CTkEntry(marco, fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), width=180)
    entrada_canti.pack(pady=(0, 20))

    def registrar_ahorro():
        tipo = boton_de_opcionees.get()
        cantidad_str = entrada_canti.get()

        if not tipo or not cantidad_str:
            messagebox.showerror("Error", "Debes completar todos los campos.")
            return

        try:
            cantidad = float(cantidad_str)
            exito = guardar_ahorro(tipo, cantidad, fecha_actual)
            if exito:
                messagebox.showinfo("Éxito", "Ahorro registrado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo registrar el ahorro.")
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")

    fecha_actual = datetime.today().strftime('%Y-%m-%d') 
    etiqueta_fecha = tk.Label(marco, text=f"Fecha: {fecha_actual}", font=("Century Gothic", 20), fg="#8C916C", bg="#EADED0")
    etiqueta_fecha.pack(pady=(0, 20))

    boton_guardar_ahorro = ctk.CTkButton(master=root19, text="Registrar ahorro", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=registrar_ahorro)
    boton_guardar_ahorro.place(x=268, y=550)

    boton_regresaar = ctk.CTkButton(master=root19, text="Regresar", fg_color="#8C916C", bg_color="#EADED0", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289", height=35, command=lambda:regresar(root19))
    boton_regresaar.place(x=280, y=600)

    root19.mainloop()

    boton_regresaar = ctk.CTkButton(master=root19, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root19))
    boton_regresaar.place(x=280, y=640)

    root19.mainloop()

def ventana_modificar_ahorro():
    root7.destroy()
    root20 = ctk.CTk()
    root20.title("Modificar ahorro")
    root20.geometry("695x695")
    root20.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root20.winfo_screenwidth()
    alto_pantalla = root20.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root20.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root20.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root20, text="Modificar ahorro", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root20, bg="#EADED0")
    marco.pack()

    style = ttk.Style()
    style.configure("Custom.Treeview",
                background="#EADED0",        
                foreground="#0D2207",       
                rowheight=30,
                fieldbackground="#EADED0") 

    style.map("Custom.Treeview", background=[("selected", "#8C916C")])

    tree_ahorro = ttk.Treeview(marco, columns=("tipo", "cantidad", "fecha"), show="headings", height=8, style="Custom.Treeview" )
    tree_ahorro.heading("tipo", text="Tipo")
    tree_ahorro.heading("cantidad", text="Cantidad")
    tree_ahorro.heading("fecha", text="Fecha")

    tree_ahorro.column("tipo", width=150, anchor="center")
    tree_ahorro.column("cantidad", width=100, anchor="center")
    tree_ahorro.column("fecha", width=120, anchor="center")

    tree_ahorro.pack(pady=20)

    tipo_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    fecha_var = tk.StringVar()

    tipo_label = ctk.CTkLabel(marco, text="Proviene de:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    tipo_label.pack()
    tipo_entry = ctk.CTkEntry(marco, textvariable=tipo_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    tipo_entry.pack(pady=5)

    cantidad_label = ctk.CTkLabel(marco, text="Nueva cantidad:", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_label.pack()
    cantidad_entry = ctk.CTkEntry(marco, textvariable=cantidad_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    cantidad_entry.pack(pady=5)

    fecha_label = ctk.CTkLabel(marco, text="Fecha (YYYY-MM-DD):", font=("Century Gothic", 18), text_color="#8C916C", bg_color="#EADED0", fg_color="#EADED0")
    fecha_label.pack()
    fecha_entry = ctk.CTkEntry(marco, textvariable=fecha_var, font=("Century Gothic", 16), text_color="#0D2207", bg_color="#EADED0", fg_color="#EADED0")
    fecha_entry.pack(pady=5)

    # Cargar ahorro del usuario
    ahorro = cargar_ahorros()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista_actual = ahorro.get(usuario_id, [])

    for i, ahorro in enumerate(lista_actual):
        tipo = ahorro.get("tipo")
        cantidad = ahorro.get("cantidad")
        fecha = ahorro.get("fecha", "Sin fecha")
        tree_ahorro.insert("", "end", iid=i, values=(tipo, cantidad, fecha))

    def seleccionar_ahorro(event):
        seleccionado = tree_ahorro.focus() 
        if not seleccionado:
            return
        index = int(seleccionado)
        ahorro = lista_actual[index]
        tipo_var.set(ahorro["tipo"])
        cantidad_var.set(str(ahorro["cantidad"]))
        fecha_var.set(ahorro.get("fecha", ""))

    tree_ahorro.bind("<<TreeviewSelect>>", seleccionar_ahorro)

    def guardar_cambioos():
        seleccionadoo = tree_ahorro.focus()
        if not seleccionadoo:
            messagebox.showerror("Error", "Selecciona un ahorro para modificar.")
            return

        try:
            index = int(seleccionadoo)
        except ValueError:
            messagebox.showerror("Error", "Selección inválida.")
            return

        nuevo_tipo = tipo_var.get().strip()
        nueva_cantidad_str = cantidad_var.get().strip()
        nueva_fecha = fecha_var.get().strip()

        if not nuevo_tipo or not nueva_cantidad_str or not nueva_fecha:
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        try:
            nueva_cantidad = float(nueva_cantidad_str)
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")
            return
        
        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Usa el formato YYYY-MM-DD.")
            return

        lista_actual[index] = {"tipo": nuevo_tipo, "cantidad": nueva_cantidad, "fecha": nueva_fecha}
        ahorro = cargar_ahorros()
        usuario_id = Usuario.usuario_actual.usuario_id
        ahorro[usuario_id] = lista_actual

        with open(ruta_ahorro, "w", encoding="utf-8") as archivo:
            json.dump(ahorro, archivo, indent=4, ensure_ascii=False)

        tree_ahorro.item(index, values=(nuevo_tipo, nueva_cantidad, nueva_fecha))

        messagebox.showinfo("Éxito", "Ahorro modificado correctamente.")
        ventana_modificar_gastos()  

    boton_guardar = ctk.CTkButton(root20, text="Guardar cambios", command=guardar_cambioos,
                                  fg_color="#8C916C", text_color="#0D2207", font=("Century Gothic", 20), hover_color="#8E9289")
    boton_guardar.pack(pady=20)

    boton_regresaar = ctk.CTkButton(master=root20, text="Regresar", fg_color="#2c3424", bg_color="#EADED0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root20))
    boton_regresaar.place(x=280, y=640)

    root20.mainloop()

def ventana_consultar_ahorro():
    root7.destroy()
    root21 = ctk.CTk()
    root21.title("Consultar ahorro")
    root21.geometry("695x695")
    root21.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root21.winfo_screenwidth()
    alto_pantalla = root21.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root21.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root21.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root21, text="Consultar ahorro", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    marco = tk.Frame(root21, bg="#EADED0")
    marco.pack()

    total = calcular_total_ahorro()
    etiqueta_total = tk.Label(marco, text=f"Total de ahorro: ${total:.2f}", font=("Century Gothic", 20),
                            fg="#0D2207", bg="#EADED0")
    etiqueta_total.pack(pady=(10, 5))

    total = calcular_total_ahorro()
    etiqueta_total.config(text=f"Total de ahorro: ${total:.2f}")

    agrupados = agrupar_ahorros_por_tipo_con_fecha()

    etiqueta_titulo_detalle = tk.Label(marco, text="Detalle por tipo:",
                                    font=("Century Gothic", 18, "bold"), fg="#8C916C", bg="#EADED0")
    etiqueta_titulo_detalle.pack(pady=(15, 5))

    for tipo, ahorros in agrupados.items():
        etiqueta_tipo = tk.Label(marco, text=f"{tipo}:", font=("Century Gothic", 17, "bold"),
                                fg="#103107", bg="#EADED0", anchor="w", justify="left")
        etiqueta_tipo.pack(anchor="w", padx=20)

        for ahorro in ahorros:
            cantidad, fecha = ahorro
            etiqueta_detalle = tk.Label(marco, text=f"    ★ Ahorraste ${cantidad:.2f} el {fecha}",
                                        font=("Century Gothic", 15), fg="#0D2207", bg="#EADED0",
                                        anchor="w", justify="left")
            etiqueta_detalle.pack(anchor="w", padx=40)

    boton_regresaar = ctk.CTkButton(master=root21, text="Regresar", fg_color="#2c3424", bg_color="#EADED0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root21))
    boton_regresaar.place(x=280, y=640)

    root21.mainloop()

def ventana_consultar_ahorro_grupal():
    root7.destroy()
    root22 = ctk.CTk()
    root22.title("Ahorro grupal")
    root22.geometry("695x695")
    root22.config(bg="#EADED0")

    ancho_ventana = 695
    alto_ventana = 695

    ancho_pantalla = root22.winfo_screenwidth()
    alto_pantalla = root22.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho_ventana // 3)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    root22.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    root22.resizable(width=False, height=False)

    etiqueta = ctk.CTkLabel(root22, text="Consultar ahorro (grupal)", font=("Vendya", 50, "bold"), text_color="#8C916C", bg_color="#EADED0")
    etiqueta.pack(pady=30)

    lo_sentimos = ctk.CTkLabel(root22, text="Las funciones grupales serán habilitadas pronto!\nLamentamos las molestias que esto pueda ocasionar,\npor lo mientras disfruta de nuestras increibles funciones individuales",
                            font=("Century Gothic", 18), text_color="#897F73", bg_color="#EADED0")
    lo_sentimos.pack(pady=180)

    boton_regresaar = ctk.CTkButton(master=root22, text="Regresar", fg_color="#2c3424", bg_color="#BFC4B0", text_color="#B3B792", font=("Century Gothic", 18), hover_color="#646954", command=lambda:regresar(root22))
    boton_regresaar.place(x=280, y=640)

    root22.mainloop()

def registar():
    nombre = entrada3.get()
    telefono = entrada4.get()
    usuario = entrada5.get()
    contraseña = entrada6.get()

    if not nombre or not telefono or not usuario or not contraseña:
        messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")
        return

    exito = registrar_usuario(nombre, telefono, usuario, contraseña)

    if exito:
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        root3.destroy()  
        ventana_de_inico()
    else:
        messagebox.showerror("Error", "Ese nombre de usuario ya existe.")
     

def regresar(ventana_actual):
    ventana_actual.destroy()
    ventana_menú()

def cerrar_sesion(ventana_actual):
    ventana_actual.destroy() 
    ventana_de_inico()

    
ventana_de_inico()
