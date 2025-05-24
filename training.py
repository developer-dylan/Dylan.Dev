# Sección de datos y contador de IDs
inventario = {}        # Diccionario que almacenará los productos
id_actual = 1          # ID que se incrementa con cada nuevo producto
# -------------------------------

# Buscar ID por nombre
def obtener_id_por_nombre(nombre):
    for id, datos in inventario.items():
        if datos["nombre"] == nombre:
            return id
    return None

# Añadir producto con ID único
def añadir_producto(nombre, precio, cantidad):
    global id_actual
    if any(producto["nombre"] == nombre for producto in inventario.values()):
        print(" El producto ya existe.")
    else:
        inventario[id_actual] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        print(f" Producto '{nombre}' añadido con ID {id_actual}.")
        id_actual += 1

# Consultar producto por nombre
def consultar_producto(nombre):
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        datos = inventario[id_producto]
        print(f"ID: {id_producto} | {datos['nombre']} → Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
    else:
        print(" Producto no encontrado.")

# Actualizar precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        inventario[id_producto]["precio"] = nuevo_precio
        print(" Precio actualizado.")
    else:
        print(" Producto no encontrado.")

# Eliminar producto por nombre
def eliminar_producto(nombre):
    global id_actual
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        # Eliminar el producto
        del inventario[id_producto]
        print(f" Producto '{nombre}' eliminado.")

        # Reacomodar los IDs
        # Creamos una lista con los IDs ordenados de menor a mayor
        ids_a_reacomodar = sorted(inventario.keys())

        # Reasignar nuevos IDs de forma consecutiva
        for idx, nuevo_id in enumerate(ids_a_reacomodar, start=1):
            # Actualizamos el ID de cada producto con el nuevo ID
            inventario[idx] = inventario.pop(nuevo_id)
            print(f"Producto con ID {nuevo_id} ahora tiene el nuevo ID {idx}.")
            
        id_actual = max(inventario.keys()) + 1  # Actualizar el próximo ID disponible
    else:
        print(" Producto no encontrado.")

# Calcular valor total usando lambda
def calcular_valor_total():
    total = sum(map(lambda p: p["precio"] * p["cantidad"], inventario.values()))
    print(f" Valor total del inventario: ${total:>10,.0f}")

# Validar número ingresado
def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor < 0:
                print("Ingresa un número positivo.")
            else:
                return valor
        except ValueError:
            print("Ingresa un número válido.")

# Menú principal del programa
def mostrar_menu():
    while True:
        print("\n------ MENÚ DE INVENTARIO ------")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Mostrar todos los productos")
        print("7. Salir")
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip().lower()
            precio = pedir_numero("Precio del producto: ")
            cantidad = pedir_numero("Cantidad disponible: ")
            añadir_producto(nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ").strip().lower()
            consultar_producto(nombre)

        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip().lower()
            nuevo_precio = pedir_numero("Nuevo precio: ")
            actualizar_precio(nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip().lower()
            eliminar_producto(nombre)

        elif opcion == "5":
            calcular_valor_total()

        elif opcion == "6":
            if inventario:
                print("\nInventario completo:")
                for id, datos in inventario.items():
                    print(f"ID: {id} | {datos['nombre'].title()} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
            else:
                print("El inventario está vacío.")

        elif opcion == "7":
            print("Programa finalizado. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

mostrar_menu()
