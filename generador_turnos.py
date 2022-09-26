
def generador_farmacia():
    for x in range(1,10000):
        yield f"F - {x}"


def generador_cosmetica():
    for x in range(1,10000):
        yield f"C - {x}"


def generador_perfumeria():
    for x in range(1,10000):
        yield f"P - {x}"

f = generador_farmacia()
c = generador_cosmetica()
p = generador_perfumeria()


def decorar_turno(tienda):

        print("Su turno es: ")
        if tienda == "P":
            print(next(p))
        elif tienda == "F":
            print(next(f))
        else:
            print(next(c))
        print("Enseguida sera atendido ")
