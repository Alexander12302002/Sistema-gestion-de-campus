import os
from .variables import save, getAll, camper

def create():
    os.system("cls")
    print("""
        *************************
        * Formulario del camper *
        *************************
    """)
    save({
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Edad": int(input("Ingrese la edad del camper: ")),
        "Genero": input("Ingrese genero del camper: ")
            })
    os.system("pause")

def read(codigo=None):
    os.system("cls")
    print("""
        ********************
        * Tabla del camper *
        ********************
    """)
    if(codigo==None):
        for i,val in enumerate(getAll()):
            print(f"""
            _______________________
            Codigo: {i+1}
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Edad: {val.get("Edad")}
            Genero: {val.get("Genero")}
            _________________________
            """)
    else:
        val = getAll()[codigo-1]
        print(f"""
        _______________________
        Codigo: {codigo}
        Nombre: {val.get("Nombre")}
        Apellido: {val.get("Apellido")}
        Edad: {val.get("Edad")}
        Genero: {val.get("Genero")}
        _________________________
        """)
    os.system("pause")
    

def update():
    os.system("cls")
    read()
    print("""
        *************************
        * Actualizar del camper *
        *************************
    """)
    codigo = int(input("Cual es el codigo del camper que desea actualizar?: "))
    read(codigo)
    while(True):
        print("""
        Esta seguro que desea actualizar el camper?
        1. si
        2. no
        3. cancelar
        """)
        opc = int(input(": "))
        match(opc):
            case 1:
                val = {
                    "Nombre": input("Ingrese el nombre del camper: "),
                    "Apellido": input("Ingrese el apellido del camper: "),
                    "Edad": int(input("Ingrese la edad del camper: ")),
                    "Genero": input("Ingrese genero del camper: ")
            }
                camper[codigo-1] = val
                print(f"""
                    El camper fue Actualizado
                    _________________________
                    Codigo: {codigo}
                    Nombre: {val.get("Nombre")}
                    Apellido: {val.get("Apellido")}
                    Edad: {val.get("Edad")}
                    Genero: {val.get("Genero")}
                    _________________________
                    """)
                os.system("pause")
                break

def delete():
    os.system("cls")
    read()
    print("""
        ***********************
        * Eliminar del camper *
        ***********************
    """)
    codigo = int(input("Cual es el codigo del camper que desea eliminar?: "))
    read(codigo)
    while(True):
        print("""
        Esta seguro que desea eliminar el camper?
        1. si
        2. no
        3. cancelar
        """)
        opc = int(input(": "))
        match(opc):
            case 1: 
                val = camper.pop(codigo-1)
                os.system("cls")
                print(f"""
                El camper fue eliminado
                _______________________
                Codigo: {codigo}
                Nombre: {val.get("Nombre")}
                Apellido: {val.get("Apellido")}
                Edad: {val.get("Edad")}
                Genero: {val.get("Genero")}
                _________________________
                """)
                os.system("pause")
                break
            case 3:
                break

def menu():
    menu = ["Guardar", "Buscar","Actualizar","Eliminar","Salir"]
    while(True):
        os.system("cls")
        print("""
            **********************
            *  Menu del camper   *
            **********************
          """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc<=len(menu) and opc>0):
                match (opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5: break
        except ValueError:
            print(f"La opcion no es valida")
