# Lista global para almacenar las calificaciones
calificaciones = []

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print ("\n")
    print("1. Verificar si una calificación es aprobatoria")
    print("2. Ingresar lista de calificaciones")
    print("3. Agrega una nota mas a la lista")
    print("4. Calcular el promedio de la lista")
    print("5. Contar cuántas calificaciones son mayores que un valor")
    print("6. Verificar y contar una calificación específica")
    print("7. Mostrar calificaciones")
    print("8. Salir")
    print ("\n")

# Función para verificar si una calificación es aprobatoria
def verificar_aprobacion():
    while True:
        entrada = input("Introduce la calificación (0-100): ").strip()
        
        if entrada == "-0":
            print("La calificación no puede ser negativa.\n")
            continue

        try:
            calificacion = float(entrada)

            if 0 <= calificacion <= 100:
                if calificacion >= 60:
                    print("El estudiante ha aprobado.")
                else:
                    print("El estudiante ha reprobado.")
                break
            else:
                print("La calificación debe estar entre 0 y 100.\n")
        except ValueError:
            print("Error, Por favor, introduce la calificacion.\n")

# Función para ingresar una lista de calificaciones válidas
def ingresar_calificaciones():
    global calificaciones
    entrada = input("Ingresa calificaciones separadas por comas (ej: 70,85,90): ")

    lista = []
    for item in entrada.split(","):
        item = item.strip()
        if item == "-0":
            print("Valor '-0' no permitido. Se omitirá.")
            continue

        if item.lstrip('-').replace('.', '', 1).isdigit():
            nota = float(item)
            if 0 <= nota <= 100:
                lista.append(nota)
            else:
                print(f"Calificación fuera de rango: {nota:.0f}. Se omitirá.")
        else:
            print(f"Entrada inválida: {item:.0f}. Se omitirá.")

    if lista:
        calificaciones = lista
        print("Lista guardada correctamente.")
    else:
        print("No se ingresaron calificaciones válidas.")

# Función para agregar una calificación a la lista
def agregar_calificacion():
    global calificaciones
    entrada = input("Ingresa una o más calificaciones separadas por comas (0-100): ").strip()

    nuevas = []
    for nota in entrada.split(","):
        nota = nota.strip()
        if nota == "-0":
            print("La calificación no puede ser negativa.")
            continue
        try:
            nota = float(nota)
            if 0 <= nota <= 100:
                nuevas.append(nota)
            else:
                print(f"La calificación {nota:.0f} está fuera del rango permitido (0-100).")
        except ValueError:
            print(f"'{nota}' no es una calificación válida.")

    if nuevas:
        calificaciones.extend(nuevas)
        print(f"Se agregaron {len(nuevas)} calificaciones correctamente.")
    else:
        print("No se agregaron calificaciones válidas.")

# Función para calcular el promedio de la lista
def calcular_promedio():
    if not calificaciones:
        print("No hay calificaciones cargadas.")
        return
    suma = 0
    for nota in calificaciones:
        suma += nota
    promedio = suma / len(calificaciones)
    print(f"El promedio es: {promedio:.0f}")

# Función para contar cuántas calificaciones son mayores que un valor
def contar_mayores():
    if not calificaciones:
        print("No hay calificaciones cargadas.")
        return
    try:
        valor = float(input("Ingresa un valor para comparar: "))
        i = 0
        contador = 0
        for i in calificaciones:
            if i > valor:
                contador += 1
        print(f"Hay {contador:.0f} calificaciones mayores que {valor:.0f}.")
    except ValueError:
        print("Valor inválido. Debe ser numérico.")

# Función para verificar y contar una calificación específica
def verificar_y_contar():
    if not calificaciones:
        print("No hay calificaciones cargadas.")
        return
    try:
        valor_objetivo = float(input("Ingresa la calificación a buscar: "))
        contador = 0
        for nota in calificaciones:
            if nota < 0 or nota > 100:
                continue  # se omite cualquier valor fuera de rango
            if nota == valor_objetivo:
                contador += 1
                # No usamos break aquí porque queremos contar todas
        if contador > 0:
            print(f"La calificación {valor_objetivo:.0f} aparece {contador:.0f} veces.")
        else:
            print(f"La calificación {valor_objetivo:.0f} no se encontró.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def mostrar_calificaciones():
    if not calificaciones:
        print("No hay calificaciones cargadas.")
    else:
        print("Calificaciones actuales:")
        for i, nota in enumerate(calificaciones, 1):
            print(f"{i}. {nota:.0f}")

# Programa principal con menú
def menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")
        print ("\n")
        # Validar la opción del menú
        if opcion == "1":
            verificar_aprobacion()
        elif opcion == "2":
            ingresar_calificaciones()
        elif opcion == "3":
            agregar_calificacion()
        elif opcion == "4":
            calcular_promedio()
        elif opcion == "5":
            contar_mayores()
        elif opcion == "6":
            verificar_y_contar()
        elif opcion == "7":
            mostrar_calificaciones()
        elif opcion == "8":
            print("Gracias por usar el programa. ¡Hasta luego!")
            print ("\n")
            break
        # Opción no válida
        else:
            print("Opción no válida. Elige del 1 al 6.")
# Llamar a la función del menú
if __name__ == "__main__":
    menu()
# Fin del programa