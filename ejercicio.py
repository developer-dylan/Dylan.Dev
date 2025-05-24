# Funcion para validar que solo haya letras y espacios
def solo_letras_y_espacios(texto):
    return all(caracter.isalpha() or caracter.isspace() for caracter in texto)

# Bienvenida al usuario
print("BIENVENIDO AL SISTEMA DE FACTURACIÓN")
print ("\n") # Espacio en blanco

# Solicitar el nombre del usuario
while True:
    username = input("Introduce del nombre de usuario: ").upper()
    # Validar que solo contenga letras y espacios y no este vacío
    if solo_letras_y_espacios(username) and username.strip() != "":
        # Convertir el nombre de usuario a mayúsculas
        username = username.upper()
        print(f"¡Hola {username}!")
        break
    else:
        print("El nombre de usuario solo debe contener letras.")
print ("\n") # Espacio en blanco

# Solicitar nombre del producto
nom_producto= input("Introduce el nombre del producto: ").upper()

# Solicitar el precio del producto
while True:
    try:
        precio_producto = float(input("Introduce el precio del producto: "))
        if precio_producto >0:
            break
        else :
            print("El precio no puede ser menor o igual a cero.") 
    except ValueError:
        print("Por favor, ingresa el precio del producto.")

cantidad_producto = 0
while True:
    try:
        cantidad_producto = int(input("Introduce la cantidad del producto: "))
        if cantidad_producto >0:
            break
        else :
            print("La cantidad no puede ser menor o igual a cero.")
    except ValueError:
        print("Por favor, ingresa la cantidad del producto.")

# Solicitar el descuento
while True:
    try:
        descuento = int(input("Introduce el descuento: "))
        if descuento >=0 and descuento <= 100:
            break
        elif descuento > 100:
            print("El descuento no puede ser mayor a 100.")
        else:
            print("El descuento no puede ser menor a 0.")
    except ValueError:
        print("Por favor, introduce un número válido para el descuento.")
        break
print () # Espacio en blanco

# Calcular el total
print("Calculando el total de tu compra")
print () # Espacio en blanco

# Simular un proceso de carga
import time
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1)  # Espera 1 segundo entre puntos
print ("\n") # Espacio en blanco

# Calcular subtotal, descuento, valor del descuento y total a pagar
subtotal = precio_producto * cantidad_producto
porcentaje_descuento = descuento
valor_descuento = (subtotal * porcentaje_descuento) / 100
total = subtotal - valor_descuento
print () # Espacio en blanco

# Obtener fecha y hora actual
from datetime import datetime
fecha_hora_actual = datetime.now()
fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Mostrar factura de compra
print("="*40)
print(" "*12 + "FACTURA DE COMPRA")
print("="*40)
print(f"Fecha y hora: {fecha_hora}")
print(f"Usuario: {username}")
print(f"Producto: {nom_producto}")
print("="*40)
print(f"{'Precio unitario:':20} ${precio_producto:>10,.0f}")
print(f"{'Cantidad:':20} {cantidad_producto:>10}")
print(f"{'Subtotal:':20} ${subtotal:>10,.0f}")
if descuento > 0:
    print(f"{'Descuento ('+str(porcentaje_descuento)+'%):':20} -${valor_descuento:>9,.0f}")
else:
    print(f"{'Descuento:':20} -${0.00:>10,.0f}")
print("="*40)
print(f"{'TOTAL A PAGAR:':20} ${total:>10,.0f} ({nom_producto})")
print("="*40)
print () # Espacio en blanco

# Mostrar mensaje de despedida
print(f"¡GRACIAS {username} POR TU COMPRA!")
# Fin del programa
