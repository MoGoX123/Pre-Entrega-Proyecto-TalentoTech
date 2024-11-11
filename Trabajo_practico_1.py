# Lista para almacenar el inventario de productos
inventario = []


while True:
    
    print("\n--- Menu ---")
    print("1. Agregar producto al inventario")
    print("2. Mostrar inventario")
    print("3. Salir")
    
    # Solicitar la opción del usuario
    opcion = input("Selecciona una opción (1, 2 o 3): ")
    
    # Condicional para manejar la opción seleccionada
    if opcion == "1":
        # Agregar un producto al inventario
        nombre_producto = input("Ingresa el nombre del producto: ")
        cantidad_producto = input("Ingresa la cantidad del producto: ")
        
        # Validación 
        if cantidad_producto.isdigit():
            inventario.append([nombre_producto, int(cantidad_producto)])
            print("Producto agregado al inventario.")
        else:
            print("La cantidad debe ser un número entero.")
    
    elif opcion == "2":
        # Mostrar el inventario 
        if inventario:
            print("\n--- Inventario Actual ---")
            indice = 0  
            while indice < len(inventario):
                producto = inventario[indice]
                print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")
                indice += 1
        else:
            print("El inventario está vacío.")
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")