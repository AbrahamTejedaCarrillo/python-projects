print("*"*50)
print("              CONTROL DE INVENTARIO")
print("*"*50)
productos = {}

while True:
    print("\nOpciones")
    print("-"*50)
    print("1. Mostrar inventario")
    print("2. Agregar un producto")
    print("3. Buscar producto")
    print("4. Salir")
    print("-"*50)
    while True:
        opcion = input("\nSeleccione una opción: ")
        try:
            opcion = int(opcion)
            if opcion > 0 and opcion < 5:
                break
        except ValueError:
            print ("Entrada no valida")
    print("\n")
    contador = 0
    
    if opcion == 2:        
        producto_nuevo = input("Ingresa el nombre del producto: ").lower()
        if producto_nuevo in productos.keys():
            print(f"El producto {producto_nuevo.capitalize()} ya se encuentra en el inventario")
            while True:
                seleccion1 = input("Presione A si desea modificar la cantidad\nPresione E si desea eliminar el producto\nPresione S si desea salir\nSeleccion: ").upper()
                if seleccion1 == "A":
                    nueva_cantidad1 = input("Ingrese la nueva cantidad: ")
                    while True:
                        try:
                            nueva_cantidad1 = int(nueva_cantidad1)
                            break
                        except ValueError:
                            print("Entrada no valida")
                    productos[producto_nuevo] = nueva_cantidad1
                    print(f"La cantidad de {producto_nuevo} ha cambiado a {productos[producto_nuevo]}")
                elif seleccion1 == "E":
                    del productos[producto_nuevo]
                    print(f"\n")
                    print("*"*50)
                    print(f"Se ha eliminado el producto {producto_nuevo}")
                    print("*"*50)
                    break
                elif seleccion1 == "S":
                    break
                else:
                    print("Entrada no valida")
        else:
            while True:
                cantidad_producto = (input("Ingresa la cantidad del producto: "))
                try:
                    cantidad_producto = int(cantidad_producto)
                    break
                except ValueError:
                    print("Entrada no valida")
            productos[producto_nuevo] = cantidad_producto
            print("\n")
            print("*"*50)
            print(f"Se añadiieron {cantidad_producto} unidades de {producto_nuevo.capitalize()} ")
            print("*"*50)
            
    elif opcion == 1:
        if not productos:
            print("¡¡¡El inventario está vacio!!!\n")
        else:
            print("Inventario actual\n")
        for item,cantidad in productos.items():
            contador += 1
            print(f"{contador}. {item.capitalize()} {cantidad} unidades")

    elif opcion == 3:
        producto_a_buscar = input("Ingresa el producto a buscar: ").lower()
        if producto_a_buscar in productos:
            print(f"\nCuentas con {productos[producto_a_buscar]} unidades de {producto_a_buscar.capitalize()}\n")
            while True:
                seleccion = input("Presione A si desea modificar la cantidad\nPresione E si desea eliminar el producto\nPresione S si desea salir\nSeleccion: ").upper()
                if seleccion == "A":
                    nueva_cantidad = input("Ingrese la nueva cantidad: ")
                    while True:
                        try:
                            nueva_cantidad = int(nueva_cantidad)
                            break
                        except ValueError:
                            print("Entrada no valida")
                    productos[producto_a_buscar] = nueva_cantidad
                    print(f"La cantidad de {producto_a_buscar} ha cambiado a {productos[producto_a_buscar]}")
                    break
                elif seleccion == "E":
                    del productos[producto_a_buscar]
                    print(f"\n")
                    print("*"*50)
                    print(f"Se ha eliminado el producto {producto_a_buscar}")
                    print("*"*50)
                    break
                elif seleccion == "S":
                    break
                else:
                    print("Entrada no valida")
        elif producto_a_buscar not in productos.keys():
            print("El producto no existe dentro del inventario, ¿desea agregarlo?")
            while True:
                eleccion = input("1) Si\n2) No\nSeleccione una opcion: ")
                try:
                    eleccion = int(eleccion)
                    if eleccion == 1 or eleccion == 2:
                        break
                except ValueError:
                    ("Entrada no valida")
            if eleccion == 2:
                break
            elif eleccion == 1:
                producto_nuevo2 = producto_a_buscar
                while True:
                    cantidad_producto2 = (input("Ingresa la cantidad del producto: "))
                    try:
                        cantidad_producto2 = int(cantidad_producto2)
                        break
                    except ValueError:
                        print("Entrada no valida")
            productos[producto_nuevo2] = cantidad_producto2
            print("\n")
            print("*"*50)
            print(f"Se añadiieron {cantidad_producto2} unidades de {producto_nuevo2.capitalize()} ")
            print("*"*50)
    elif opcion == 4:
        print("...Saliendo...")
        break
            