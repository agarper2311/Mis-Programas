def piramide_normal():
    print("\n Piramide Normal")
    for i in range(5):
        x='* '
        x=x*i
        print(f'{x: ^10}')

def piramide_invertida():
    print("\n Piramide Invertida \n")
    for i in range(5):
        x='* '
        x=x*(5-i)
        print(f'{x: ^10}')
    
def piramide_izquierda():
    print("\n Piramide Orientada a la izquierda")
    for i in range(5):
        x='* '
        x=x*i
        print(f'{x: <10}')

def piramide_derecha():
    print("\n Piramide Orientada a la derecha")
    for i in range(5):
        x='* '
        x=x*i
        print(f'{x: >10}')


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Pirámide Normal")
        print("2. Pirámide Invertida")
        print("3. Pirámide Orientada a la Izquierda")
        print("4. Pirámide Orientada a la Derecha")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            piramide_normal()
        elif opcion == "2":
            piramide_invertida()
        elif opcion == "3":
            piramide_izquierda()
        elif opcion == "4":
            piramide_derecha()
        elif opcion == "5":
            print("Adios....")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción entre 1 y 5.")

menu()