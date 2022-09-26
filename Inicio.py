import generador_turnos
print()

def preguntar():

    print("Bienvenido a la Farmacia")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_tienda = input("Elija su tienda: ").upper()
            ["P", "F", "C"].index(mi_tienda)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break

    generador_turnos.decorar_turno(mi_tienda)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro turno?  [S] o [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()