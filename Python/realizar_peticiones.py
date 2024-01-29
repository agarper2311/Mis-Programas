import requests
import time

def realizar_peticiones():
    # Solicitar al usuario el número de peticiones y la URL
    num_peticiones = int(input("Ingrese el número de peticiones a realizar: "))
    url = input("Ingrese la URL de la página: ")

    # Calcular el tiempo de espera entre cada solicitud para lograr 50 peticiones por segundo
    tiempo_entre_peticiones = 1 / 50

    # Realizar las peticiones
    for i in range(num_peticiones):
        try:
            response = requests.get(url)
            # Verificar si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                print(f'Petición {i + 1}: Solicitud exitosa')
            else:
                print(f'Petición {i + 1}: Error en la solicitud. Código de estado: {response.status_code}')
        except requests.RequestException as e:
            print(f'Petición {i + 1}: Error en la solicitud. {e}')

        # Agregar un pequeño retraso entre cada solicitud para lograr 50 peticiones por segundo
        time.sleep(tiempo_entre_peticiones)

if __name__ == "__main__":
    realizar_peticiones()
