import json
import os
from collections import defaultdict

class Usuario:
    lista_usuario = []
    usuario_actual = None  # Usuario que ha iniciado sesión

    def __init__(self, Nombre, Rol, Password, Usuario_ID=None):
        self.nombre = Nombre
        self.rol = Rol
        self.__pass = Password
        self.usuario_id = Usuario_ID  # ID único (nombre de usuario)
        Usuario.lista_usuario.append(self)

    @classmethod
    def iniciar_sesion(cls, usuario_input, password_input):
        archivo = "usuarios.json"

        if not os.path.exists(archivo):
            print("Archivo de usuarios no encontrado.")
            return None

        with open(archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                print("Error leyendo archivo JSON.")
                return None

        for u in datos:
            if u["usuario"] == usuario_input and u["contraseña"] == password_input:
                print(f"Inicio de sesión exitoso. Bienvenido {u['nombre']}")
                usuario = Usuario(
                u["nombre"], "Usuario", u["contraseña"], Usuario_ID=u["usuario"])
                cls.usuario_actual = usuario
                return usuario
        
        print("Usuario o contraseña incorrectos.")
        return None



# Función para registrar usuarios en JSON
def registrar_usuario(nombre, telefono, usuario, contraseña):
    nuevo_usuario = {
        "nombre": nombre,
        "telefono": telefono,
        "usuario": usuario,
        "contraseña": contraseña
    }

    archivo = "usuarios.json"

    # Carga usuarios existentes
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = []
    else:
        datos = []

    # Verifica si el usuario ya existe
    for u in datos:
        if u["usuario"] == usuario:
            print("El nombre de usuario ya está registrado.")
            return False

    # Agrega el nuevo usuario y guarda
    datos.append(nuevo_usuario)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print("Usuario registrado correctamente.")
    return True


ruta_ingresos = "ingresos.json"

# Cargar ingresos desde archivo
def cargar_ingresos():
    if os.path.exists(ruta_ingresos):
        with open(ruta_ingresos, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {}
    return {}

# Guardar nuevo ingreso
def guardar_ingreso(tipo, cantidad, fecha):
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return False

    datos = cargar_ingresos()
    usuario_id = Usuario.usuario_actual.usuario_id

    if usuario_id not in datos:
        datos[usuario_id] = []

    datos[usuario_id].append({
        "tipo": tipo,
        "cantidad": cantidad,
        "fecha": fecha
    })

    with open(ruta_ingresos, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Ingreso guardado para {usuario_id}")
    return True

def calcular_total_ingresos():
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return 0.0

    datos = cargar_ingresos()
    usuario_id = Usuario.usuario_actual.usuario_id

    ingresos = datos.get(usuario_id, [])
    total = sum(ingreso.get("cantidad", 0) for ingreso in ingresos)
    return total

def calcular_totales_por_tipo():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_ingresos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    resumen = {}
    for ingreso in lista:
        tipo = ingreso.get("tipo", "Desconocido")
        cantidad = ingreso.get("cantidad", 0)
        resumen[tipo] = resumen.get(tipo, 0) + cantidad

    return resumen

def agrupar_ingresos_por_tipo_con_fecha():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_ingresos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    agrupado = {}
    for ingreso in lista:
        tipo = ingreso.get("tipo", "Desconocido")
        cantidad = ingreso.get("cantidad", 0)
        fecha = ingreso.get("fecha", "Sin fecha")
        agrupado.setdefault(tipo, []).append((cantidad, fecha))

    return agrupado

ruta_gastos = "gastos.json"

# Cargar ingresos desde archivo
def cargar_gastos():
    if os.path.exists(ruta_gastos):
        with open(ruta_gastos, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {}
    return {}

# Guardar nuevo gasto
def guardar_gasto(tipo, cantidad, fecha):
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return False

    datos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id

    if usuario_id not in datos:
        datos[usuario_id] = []

    datos[usuario_id].append({
        "tipo": tipo,
        "cantidad": cantidad,
        "fecha": fecha
    })

    with open(ruta_gastos, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Nuevo gasto registrado para {usuario_id}")
    return True

ruta_gastos = "gastos.json"

# Cargar gastos desde archivo
def cargar_gastos():
    if os.path.exists(ruta_gastos):
        with open(ruta_gastos, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {}
    return {}

# Guardar nuevo gasto
def guardar_gasto(tipo, cantidad, fecha):
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return False

    datos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id

    if usuario_id not in datos:
        datos[usuario_id] = []

    datos[usuario_id].append({
        "tipo": tipo,
        "cantidad": cantidad,
        "fecha": fecha
    })

    with open(ruta_gastos, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Gasto modificado correctamente para {usuario_id}")
    return True

def calcular_total_gastos():
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return 0.0

    datos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id

    gastos = datos.get(usuario_id, [])
    total = sum(gasto.get("cantidad", 0) for gasto in gastos)
    return total

def calcular_totales_por_tipo():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    resumen = {}
    for gasto in lista:
        tipo = gasto.get("tipo", "Desconocido")
        cantidad = gasto.get("cantidad", 0)
        resumen[tipo] = resumen.get(tipo, 0) + cantidad

    return resumen

def agrupar_gastos_por_tipo_con_fecha():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_gastos()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    agrupado = {}
    for gasto in lista:
        tipo = gasto.get("tipo", "Desconocido")
        cantidad = gasto.get("cantidad", 0)
        fecha = gasto.get("fecha", "Sin fecha")
        agrupado.setdefault(tipo, []).append((cantidad, fecha))

    return agrupado

ruta_ahorro = "ahorro.json"

# Cargar ahorros desde archivo
def cargar_ahorros():
    if os.path.exists(ruta_ahorro):
        with open(ruta_ahorro, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {}
    return {}

# Guardar nuevo ahorro
def guardar_ahorro(tipo, cantidad, fecha):
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return False

    datos = cargar_ahorros()
    usuario_id = Usuario.usuario_actual.usuario_id

    if usuario_id not in datos:
        datos[usuario_id] = []

    datos[usuario_id].append({
        "tipo": tipo,
        "cantidad": cantidad,
        "fecha": fecha
    })

    with open(ruta_ahorro, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Ahorro modificado correctamente para {usuario_id}")
    return True

def calcular_total_ahorro():
    if Usuario.usuario_actual is None:
        print("Error: No hay usuario autenticado.")
        return 0.0

    datos = cargar_ahorros()
    usuario_id = Usuario.usuario_actual.usuario_id

    ahorros = datos.get(usuario_id, [])
    total = sum(ahorro.get("cantidad", 0) for ahorro in ahorros)
    return total

def calcular_totales_por_tipo():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_ahorros()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    resumen = {}
    for ahorro in lista:
        tipo = ahorro.get("tipo", "Desconocido")
        cantidad = ahorro.get("cantidad", 0)
        resumen[tipo] = resumen.get(tipo, 0) + cantidad

    return resumen

def agrupar_ahorros_por_tipo_con_fecha():
    if Usuario.usuario_actual is None:
        return {}

    datos = cargar_ahorros()
    usuario_id = Usuario.usuario_actual.usuario_id
    lista = datos.get(usuario_id, [])

    agrupado = {}
    for ahorro in lista:
        tipo = ahorro.get("tipo", "Desconocido")
        cantidad = ahorro.get("cantidad", 0)
        fecha = ahorro.get("fecha", "Sin fecha")
        agrupado.setdefault(tipo, []).append((cantidad, fecha))

    return agrupado

ruta_ingresos = "ingresos.json"
ruta_gastos = "gastos.json"

def cargar_json(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {}
    return {}

def calcular_totales_ingresos_vs_gastos(usuario_id):
    ingresos = cargar_json(ruta_ingresos).get(usuario_id, [])
    gastos = cargar_json(ruta_gastos).get(usuario_id, [])

    total_ingresos = sum(item.get("cantidad", 0) for item in ingresos)
    total_gastos = sum(item.get("cantidad", 0) for item in gastos)

    return total_ingresos, total_gastos

def resumen_por_tipo(usuario_id):
    ingresos_data = cargar_json(ruta_ingresos).get(usuario_id, [])
    gastos_data = cargar_json(ruta_gastos).get(usuario_id, [])

    resumen_ingresos = defaultdict(float)
    resumen_gastos = defaultdict(float)

    for ingreso in ingresos_data:
        resumen_ingresos[ingreso.get("tipo", "Desconocido")] += ingreso.get("cantidad", 0)

    for gasto in gastos_data:
        resumen_gastos[gasto.get("tipo", "Desconocido")] += gasto.get("cantidad", 0)

    return resumen_ingresos, resumen_gastos