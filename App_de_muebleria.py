class Producto:
    def __init__(self, id, designacion, precio, stock):
        self.id = id
        self.designacion = designacion
        self.precio = precio
        self.stock = stock

class Empleado:
    def __init__(self, numero_legajo, nombre, apellido, comisiones):
        self.numero_legajo = numero_legajo
        self.nombre = nombre
        self.apellido = apellido
        self.comisiones = comisiones

class Muebleria:
    def __init__(self):
        self.productos = []
        self.empleados = []

    def cargar_producto(self, id, designacion, precio, stock):
        if precio < 0 or stock < 0:
            print("El precio y el stock deben ser números positivos.")
            return
        self.productos.append(Producto(id, designacion, precio, stock))
   
    def editar_producto(self, id, designacion=None, precio=None, stock=None):
        for producto in self.productos:
            if producto.id == id:
                if designacion:
                    producto.designacion = designacion
                if precio is not None:
                    if precio < 0:
                        print("El precio debe ser un número positivo.")
                        return
                    producto.precio = precio
                if stock is not None:
                    if stock < 0:
                        print("El stock debe ser un número positivo.")
                        return
                    producto.stock = stock
                return
        print("Producto no encontrado.")
   
    def mostrar_productos(self, orden='nombre'):
        productos_ordenados = sorted(self.productos, key=lambda x: x.designacion if orden == 'nombre' else x.precio)
        for producto in productos_ordenados:
            print(f"{producto.id}: {producto.designacion} - Precio: ${producto.precio} - Stock: {producto.stock}.")
   
    def buscar_producto(self, criterio):
        for producto in self.productos:
            if (criterio.lower() in producto.designacion.lower() or
                str(criterio) == str(producto.id)):
                print(f"{producto.id}: {producto.designacion} - Precio: ${producto.precio} - Stock: {producto.stock}")

    def buscar_por_rango_precio(self, min_precio, max_precio):
        for producto in self.productos:
            if min_precio <= producto.precio <= max_precio:
                print(f"{producto.id}: {producto.designacion} - Precio: ${producto.precio} - Stock: {producto.stock}")
   
    def eliminar_producto(self, id):
        self.productos = [producto for producto in self.productos if producto.id != id]

    def agregar_empleado(self, numero_legajo, nombre, apellido, comisiones):
        self.empleados.append(Empleado(numero_legajo, nombre, apellido, comisiones))
   
    def modificar_empleado(self, numero_legajo, nombre=None, apellido=None, comisiones=None):
        for empleado in self.empleados:
            if empleado.numero_legajo == numero_legajo:
                if nombre:
                    empleado.nombre = nombre
                if apellido:
                    empleado.apellido = apellido
                if comisiones is not None:
                    empleado.comisiones = comisiones
                return
        print("Empleado no encontrado.")

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(f"{empleado.numero_legajo}: {empleado.nombre} {empleado.apellido} - Comisiones: ${empleado.comisiones}")

    def eliminar_empleado(self, numero_legajo):
        self.empleados = [e for e in self.empleados if e.numero_legajo != numero_legajo]

def menu():
    muebleria = Muebleria()

   
    muebleria.cargar_producto(1, "Banquete individual", 110, 50)
    muebleria.cargar_producto(2, "Esquinero", 130, 30)
    muebleria.cargar_producto(3, "Banqueta Doble", 170, 20)
    muebleria.cargar_producto(4, "Mesa ratona grande 1.00x1.00", 200, 20)
    muebleria.cargar_producto(5, "Mesa ratona chica 0.70x0.70", 170, 30)
    muebleria.cargar_producto(6, "Silla cocina-comedor", 110, 10)
    muebleria.cargar_producto(7, "Silla con apoya brazos", 150, 40)
    muebleria.cargar_producto(8, "Mesa de cocina-comedor", 330, 30)
    muebleria.cargar_producto(9, "Mesa de cocina-comedor con detalles", 440, 40)
    muebleria.cargar_producto(10, "Camastro de descanso de 1.30m", 570, 10)
    muebleria.cargar_producto(11, "Camastro de descanso con almohadas", 650, 20)
    muebleria.cargar_producto(12, "Gazebo simple", 1000, 40)
    muebleria.cargar_producto(13, "Gazebo doble", 1700, 30)

    while True:
        print("Menú de Mueblería:")
        print("1. Cargar producto")
        print("2. Editar producto")
        print("3. Mostrar productos")
        print("4. Buscar producto")
        print("5. Buscar por rango de precios")
        print("6. Eliminar producto")
        print("7. Agregar empleado")
        print("8. Modificar empleado")
        print("9. Mostrar empleados")
        print("10. Eliminar empleado")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID del producto: "))
            designacion = input("Designación: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            muebleria.cargar_producto(id, designacion, precio, stock)

        elif opcion == "2":
            id = int(input("ID del producto a editar: "))
            designacion = input("Nuevo nombre (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            stock = input("Nuevo stock (dejar vacío para no cambiar): ")
            muebleria.editar_producto(id, designacion or None, float(precio) if precio else None, int(stock) if stock else None)

        elif opcion == "3":
            orden = input("Ordenar por (nombre/precio): ")
            muebleria.mostrar_productos(orden)

        elif opcion == "4":
            criterio = input("Ingrese nombre o ID del producto a buscar: ")
            muebleria.buscar_producto(criterio)

        elif opcion == "5":
            min_precio = float(input("Precio mínimo: "))
            max_precio = float(input("Precio máximo: "))
            muebleria.buscar_por_rango_precio(min_precio, max_precio)

        elif opcion == "6":
            id = int(input("ID del producto a eliminar: "))
            muebleria.eliminar_producto(id)

        elif opcion == "7":
            numero_legajo = int(input("Número de legajo: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            comisiones = float(input("Comisiones: "))
            muebleria.agregar_empleado(numero_legajo, nombre, apellido, comisiones)

        elif opcion == "8":
            numero_legajo = int(input("Número de legajo del empleado a modificar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            apellido = input("Nuevo apellido (dejar vacío para no cambiar): ")
            comisiones = input("Nuevas comisiones (dejar vacío para no cambiar): ")
            muebleria.modificar_empleado(numero_legajo, nombre or None, apellido or None, float(comisiones) if comisiones else None)

        elif opcion == "9":
            muebleria.mostrar_empleados()

        elif opcion == "10":
            numero_legajo = int(input("Número de legajo del empleado a eliminar: "))
            muebleria.eliminar_empleado(numero_legajo)

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente nuevamente.")
