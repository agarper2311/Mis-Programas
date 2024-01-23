# Importamos la biblioteca Random para poder mostrar las respuestas de forma aleatoria.

import random

# Estas son las listas donde se almacenarán las preguntas con sus respuestas, nombres de usuarios y puntuaciones.

preguntas = []
nombres = []
puntuaciones = []


# Función para las preguntas por defecto.

def preguntas_por_defecto():

  # Diccionarios que almacenan las preguntas y respuestas por defecto {}.

  pregunta1 = {"pregunta": "¿Cuál es el planeta más grande del sistema solar?",
               "opciones": ["Júpiter", "Venus", "Marte", "Tierra"],
               "respuesta_correcta": "Júpiter"}
  pregunta2 = {"pregunta": "¿Cuál es la capital de Francia?",
               "opciones": ["París", "Londres", "Berlín", "Roma"],
               "respuesta_correcta": "París"}
  pregunta3 = {"pregunta": "¿Cuántos continentes hay en el mundo?",
               "opciones": ["6", "7", "8", "9"],
               "respuesta_correcta": "7"}
  pregunta4 = {"pregunta": "¿Cuál es la moneda oficial de Italia?",
               "opciones": ["Euro", "Dólar", "Yen", "Libra"],
               "respuesta_correcta": "Euro"}
  # Si quieres añadir alguna pregunta, deberás incluirla en la linea de abajo también.
  preguntas = [pregunta1, pregunta2, pregunta3, pregunta4]
  

  # Contador de aciertos en la función Preguntas_Por_Defecto, se inicia en 0 para ir sumando puntos.
  aciertos = 0
  # La variable "p" representa cada pregunta en la lista preguntas.
  
  for p in preguntas:
    opciones = p["opciones"]
    random.shuffle(opciones)
    p["opciones"] = opciones
    print(f"{p['pregunta']}")
    # La variable "i" representa el índice de cada opción dentro de la lista de opciones de una pregunta específica.
    for i, opcion in enumerate(p["opciones"]):
    # La variable "i" es un contador que itera sobre las opciones de la pregunta actual en el bucle for. Al agregar 1 a "i", 
    # se garantiza que las opciones se numeran desde 1 en lugar de 0.
      print(f"{i + 1}. {opcion}")
    respuesta_usuario = input("Elige una opción (1, 2, 3, 4): ")
    # Respuesta_Usuario es -= 1 porque los indices de lista en Python comienzan en 0, entonces se le resta 1 
    # para que la respuesta del usuario corresponda con la que se le mostró.

    # if p["opciones"][int(respuesta_usuario) - 1] == p["respuesta_correcta"]: 
    # comprueba si la respuesta elegida por el usuario es igual a la respuesta correcta de la pregunta actual.
    if p["opciones"][int(respuesta_usuario) - 1] == p["respuesta_correcta"]:
      print("¡Correcto!")
      aciertos += 1
    else:
      print("Incorrecto.")

  print(f"Has acertado {aciertos} preguntas de {len(preguntas)}.")
    # muestra el número de respuestas correctas del usuario en comparación con el total de preguntas.
    # La variable aciertos almacena el número de respuestas correctas y la función len(preguntas) devuelve el número total de preguntas.
    # La sintaxis f"..." es una forma de crear una cadena.
  
  return preguntas
  # Return preguntas devuelve la lista "preguntas" como resultado de la función "preguntas_por_defecto()".
  



# Función para agregar preguntas.
def agregar_pregunta():
  pregunta = input("Ingrese la pregunta: ")

# El ciclo continúa hasta que el usuario ingrese una pregunta vacía.
  while pregunta != "":
    respuesta_correcta = input("Ingrese la respuesta correcta: ")
    respuesta_incorrecta1 = input("Ingrese la respuesta incorrecta 1: ")
    respuesta_incorrecta2 = input("Ingrese la respuesta incorrecta 2: ")

    # Crea una lista con las opciones.
    opciones = [respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2]
    # Agrega un diccionario con la pregunta y las opciones a la lista de preguntas.
    preguntas.append({"pregunta": pregunta, "opciones": opciones, "respuesta_correcta": respuesta_correcta})
    print("Pregunta agregada!")
    pregunta = input("Ingrese la pregunta (o presione enter para salir): ")




# Función para ver el listado de las preguntas que introdujo el usuario al hacer uso de la función agregar_preguntas
def ver_listado_de_preguntas():
  print("Listado de preguntas:")
# Nos muesta las preguntas que agregamos antes haciendo uso de la variable "i" que es el índice/número de cada pregunta
  for i, pregunta in enumerate(preguntas):
    print("---------------------------------------")
    print(f"{i + 1}. {pregunta['pregunta']}")
    print("---------------------------------------")




# Función para eliminar cualquier pregunta de las que el usuario ha introducido.
# La función muestra una lista de preguntas, pide al usuario que seleccione una de ellas,
# y luego la elimina de la lista.
#  Si el usuario no selecciona una pregunta o la selección es inválida, la función
#  informa al usuario y retorna la lista de preguntas sin cambios.
# Las preguntas por defecto solo se pueden modificar dentro del código.
def eliminar_pregunta(preguntas):

  # Nos imprime la lista de preguntas en el orden que la añadimos anteriormente
    print("Lista de preguntas:")
    for i, pregunta in enumerate(preguntas):
        print(f"{i + 1}. {pregunta}")
    
    seleccion = input("Selecciona el número de la pregunta que deseas eliminar: ")
    
  # Si no seleccionamos ninguna pregunta, el programa nos devolverá al menú principal
    if seleccion == "":
        print("-------------------------------------------------")
        print("No se ha seleccionado ninguna pregunta.")
        print("-------------------------------------------------")
        return preguntas

    # Control de excepciones.
    # Try permite ejecutar un bloque de código y controlar las excepciones que puedan ocurrir en él.
    try:
        index = int(seleccion) - 1
        if index < 0 or index >= len(preguntas):
    # ValueError es una excepción que se lanza cuando una operación o función recibe un argumento o valor que no es válido o no se puede utilizar. 
            raise ValueError
        preguntas.pop(index)
        print("-------------------------------------------------")
        print("La pregunta se ha eliminado correctamente.")
        print("-------------------------------------------------")
        return preguntas
    except ValueError:
        print("-------------------------------------------------")
        print("La pregunta seleccionada no existe.")
        print("-------------------------------------------------")
        return preguntas





# Función para jugar al Trivial.
def jugar_juego():

  # Puntuación inicial del jugador.
  puntuacion = 0
  # Repite la secuencia a través de las preguntas en la lista.
  for p in preguntas:
    print("-------------------------------------------------")
    print(p["pregunta"])
    random.shuffle(p["opciones"])
    print("-------------------------------------------------")
    for i, opcion in enumerate(p["opciones"]):
      print(f"{i + 1}. {opcion}")
    respuesta_usuario = int(input("Ingrese su respuesta (1, 2, o 3): "))
    # Respuesta_Usuario es -= 1 porque los indices de lista en Python comienzan en 0, entonces se le resta 1 
    # para que la respuesta del usuario corresponda con la que se le mostró.
    respuesta_usuario -= 1
     # Verifica si la respuesta del usuario es correcta sobre la variable "P" que hace referencia a cada pregunta con su respuesta correcta
     # en la lista de preguntas.
    if p["opciones"][respuesta_usuario] == p["respuesta_correcta"]:
      # Suma 1 punto si la respuesta es correcta.
      puntuacion += 1
    
      print("-------------------------------------------------")
      print("No se acierta por casualidad!")
      print("-------------------------------------------------")
    else:
      print("-------------------------------------------------")
      print("Tampoco se falla por casualidad")
      print("-------------------------------------------------")
      return
    # Imprimimos el resultado final X puntuación de X preguntas jugando con las preguntas que ha introducido el usuario.
    print("")
    if puntuacion == 0:
      print("Has hecho lo más dificil")
    print("-------------------------------------------------")
    print(f"Obtuviste {puntuacion} de {len(preguntas)}.")
    print("-------------------------------------------------")




# Funcion para agregar usuarios y puntuacion a la lista de nombres = [] y puntuaciones = [].
def agregar_jugador(nombres, puntuaciones):
  while True:
    nombre = input("Ingrese el nombre del jugador: ")
  # Si en el nombre del jugador no introducimos nada, el programa nos dirá que no se introdujo ningún jugador y nos devolverá al menú principal.
    if nombre == "":
      print("")
      print("----------------------------------------------")
      print("No se introdujo ningún jugador")
      print("----------------------------------------------")
      print("")
      return
  # Comprueba de que el nombre de usuario no está ya registrado, si está registrado nos dirá que ya existe 
    if nombre in nombres:
      print("")
      print("----------------------------------------------")
      print(f"El jugador con nombre {nombre} ya existe")
      print("----------------------------------------------")
      print("")
      continue
    break

  # Si previamente hemos introducido el nombre del jugador/a nos pedirá que introduzcamos la puntuación obtenida.
  puntuacion = int(input("Ingrese la puntuación del jugador: "))
  nombres.append(nombre)
  puntuaciones.append(puntuacion)
  # Aquí nos mostrará que el Jugador (con su nombre) a sido agregado.
  print("")
  print("----------------------------------------------")
  print(f"Jugador {nombre} Agregado")
  print("----------------------------------------------")
  print("")




# Función para ver los 10 mejores resultados
def ver_top_10():
# Crea una lista de tuplas con los nombres y puntuaciones de los jugadores
  jugadores = list(zip(nombres, puntuaciones))
# Ordena la lista anterior de jugadores en orden descendente según la puntuación obtenida 
  jugadores.sort(key=lambda x: x[1], reverse=True)
# Obtiene la cantidad de jugadores en la lista
  cantidad_jugadores = len(jugadores)
# Si no hay ningún jugador registrado, nos dirá que no hay nadie y nos devolverá al menú principal
  if cantidad_jugadores == 0:
    print("")
    print("----------------------------------------------")
    print("No hay jugadores agregados.")
    print("----------------------------------------------")
    print("")
    return
# Obtiene los 10 mejores jugadores si hay al menos 10 jugadores, de lo contrario, se obtiene la lista completa de jugadores
  top_10 = jugadores[:10] if cantidad_jugadores >= 10 else jugadores
# Nos imprime el título 
  print("Top 10 Jugadores:")
# Imprime los 10 mejores jugadores
  for i, jugador in enumerate(top_10):
    print("----------------------------------------------")
    print(f"{i + 1}. {jugador[0]} - {jugador[1]}")
    print("----------------------------------------------")
    print("\n")




# Función para mostrar el menú y que el usuario escoja la opción que desee.
def mostrar_menu():
  print("1. Probar programa con preguntas por defecto")
  print("Es la lectura buen compañero de viaje")
  print("2. Agregar pregunta ")
  print("3. Eliminar pregunta")
  print("4. Ver listado de preguntas")
  print("5. Jugar juego")
  print("6. Agregar Jugador Actual")
  print("7. Ver Top 10")
  print("8. Salir")
  eleccion = input("Ingrese su elección: ")
# Verificamos que la entrada sea válida
  if eleccion == "":
    print("-------------------------------------------------------------")
    print("No se ha seleccionado ninguna opción")
    print("-------------------------------------------------------------")
    return
  # elif not eleccion.isdigit(): en este caso sirve para que cuando el usuario introduzca un caracter que no sea numerico por error, 
  # se le volverá a mostrar el menú del programa.
  # Es decir, verifica que la entrada es un número
  elif not eleccion.isdigit():
    print("-------------------------------------------------------------")
    print("Elección inválida. Por favor, ingrese un número del 1 al 7.")
    print("-------------------------------------------------------------")
    return
  eleccion = int(eleccion)
# Ejecuta la función que ha seleccionado el usuario
  if eleccion == 1:
    preguntas_por_defecto()
  elif eleccion == 2:
     agregar_pregunta()
  elif eleccion == 3:
    eliminar_pregunta(preguntas) 
  elif eleccion == 4:
    ver_listado_de_preguntas()
  elif eleccion == 5:
    jugar_juego()
  elif eleccion == 6:
    agregar_jugador(nombres, puntuaciones)
  elif eleccion == 7:
    ver_top_10()
  elif eleccion == 8:
    print("Gracias Por Usar Este Programa \U0001f600")
    # \U0001f600 es un unicode que básicamente lo que hace es imprimir una cara sonriente. Para usar este código no es necesario importar ninguna 
    # biblioteca, pero si queremos usar otros si haría falta.
    exit()

  else:
    print("-------------------------------------------------------------")
    print("Elección inválida. Intente de nuevo.")
    print("-------------------------------------------------------------")

# Muestra el menú en un bucle infinito.
while True:
  mostrar_menu()