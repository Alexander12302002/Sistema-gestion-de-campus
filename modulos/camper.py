def create():
    print("El camper se guardo")

def read():
    print("Datos del camper encontrados")

def update():
    print("El camper se actualizo")

def delete():
    print("El camper se borro")

def menu():
    print("""
**********************
*  Menu del camper   *
**********************
          """)
    
    print("1. Guardar \n2. Buscar \n3. Actualizar \n4. Eliminar")
    while(True):
        try:
            opc = int(input)
            break
        except ValueError:
            print("Valor invalido, ingrese un numero de las opciones ")
