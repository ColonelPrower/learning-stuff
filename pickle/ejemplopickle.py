import pickle
import os

# Nombre del archivo donde guardaremos los datos
ARCHIVO_PRODUCTOS = 'productos.pkl'

def cargar_productos():
    """Carga los productos desde el archivo pickle."""
    if os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, 'rb') as f:
            try:
                productos = pickle.load(f)
            except EOFError:  # Manejar el caso de archivo vacío
                productos = []
            except Exception as e:
                print(f"Error al cargar productos: {e}")
                productos = []
    else:
        productos = []
    return productos

def guardar_productos(productos):
    """Guarda los productos en el archivo pickle."""
    with open(ARCHIVO_PRODUCTOS, 'wb') as f:
        pickle.dump(productos, f)
    print("Productos guardados exitosamente.")

def generar_nuevo_id(productos):
    """Genera un nuevo ID para un producto."""
    if not productos:
        return 1
    return max(p['id'] for p in productos) + 1

def crear_producto():
    """Permite al usuario crear un nuevo producto."""
    productos = cargar_productos()
    nuevo_id = generar_nuevo_id(productos)
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número.")

    nuevo_producto = {'id': nuevo_id, 'nombre': nombre, 'precio': precio}
    productos.append(nuevo_producto)
    guardar_productos(productos)
    print(f"Producto '{nombre}' (ID: {nuevo_id}) creado exitosamente.")

def leer_productos():
    """Muestra todos los productos existentes."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- Lista de Productos ---")
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")
    print("--------------------------")

def actualizar_producto():
    """Permite al usuario actualizar un producto existente."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos para actualizar.")
        return

    leer_productos()
    while True:
        try:
            producto_id = int(input("Ingrese el ID del producto a actualizar: "))
            break
        except ValueError:
            print("ID inválido. Por favor, ingrese un número.")

    producto_encontrado = False
    for producto in productos:
        if producto['id'] == producto_id:
            print(f"Producto actual: Nombre='{producto['nombre']}', Precio='{producto['precio']}'")
            nuevo_nombre = input(f"Ingrese el nuevo nombre para '{producto['nombre']}' (dejar en blanco para no cambiar): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre

            while True:
                nuevo_precio_str = input(f"Ingrese el nuevo precio para '{producto['nombre']}' (dejar en blanco para no cambiar): ")
                if not nuevo_precio_str:
                    break
                try:
                    nuevo_precio = float(nuevo_precio_str)
                    producto['precio'] = nuevo_precio
                    break
                except ValueError:
                    print("Precio inválido. Por favor, ingrese un número.")

            producto_encontrado = True
            break

    if producto_encontrado:
        guardar_productos(productos)
        print(f"Producto con ID {producto_id} actualizado exitosamente.")
    else:
        print(f"Producto con ID {producto_id} no encontrado.")

def eliminar_producto():
    """Permite al usuario eliminar un producto existente."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos para eliminar.")
        return

    leer_productos()
    while True:
        try:
            producto_id = int(input("Ingrese el ID del producto a eliminar: "))
            break
        except ValueError:
            print("ID inválido. Por favor, ingrese un número.")

    productos_actualizados = [p for p in productos if p['id'] != producto_id]

    if len(productos_actualizados) < len(productos):
        guardar_productos(productos_actualizados)
        print(f"Producto con ID {producto_id} eliminado exitosamente.")
    else:
        print(f"Producto con ID {producto_id} no encontrado.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú CRUD de Productos ---")
    print("1. Crear Producto")
    print("2. Leer Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    print("----------------------------")

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_producto()
        elif opcion == '2':
            leer_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()