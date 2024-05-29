import random
import colorama

def leer_preguntas(nombreArchivo):
    matriz_preguntas = []

    with open(nombreArchivo, 'r', encoding='utf-8') as file:
        pregunta = []
        for line in file:
            line = line.strip()
            if not line:
                # Ignorar líneas vacías
                continue
            elif line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                # Agregar a las filas correspondientes y eliminar la cadena inicial
                pregunta.append(line[3:].strip())
            elif line.startswith("ANSWER:"):
                # Agregar a la sexta fila y eliminar la cadena inicial
                pregunta.append(line[7:].strip())
                matriz_preguntas.append(pregunta)
                pregunta = []
            else:
                # Agregar a la pregunta
                pregunta = [line]

    return matriz_preguntas


def mostrar_pregunta(pregunta):
    print(f"{pregunta[0]}")
    if len(pregunta) > 1:
        print(f"A. {pregunta[1]}")
    if len(pregunta) > 2:
        print(f"B. {pregunta[2]}")
    if len(pregunta) > 3:
        print(f"C. {pregunta[3]}")
    if len(pregunta) > 4:
        print(f"D. {pregunta[4]}")
    respuesta = input("Ingrese la respuesta: ")
    return respuesta

def validar_respuesta(pregunta, respuesta):
    return pregunta.upper() == respuesta.upper()

def generar_pregunta(preguntas):
    len_preguntas = len(preguntas)
    indice = random.randint(0, len_preguntas-1)
    pregunta = preguntas.pop(indice)  # Elimina la pregunta de la lista
    respuesta = mostrar_pregunta(pregunta)
    if (validar_respuesta(pregunta[5], respuesta)):
        print(colorama.Fore.GREEN + "Respuesta correcta")
        print(colorama.Style.RESET_ALL)  # Restablece el color a su valor predeterminado
        return True
    else:
        print(colorama.Fore.RED + "Respuesta incorrecta. La respuesta correcta era:", pregunta[5])
        print(colorama.Style.RESET_ALL)  # Restablece el color a su valor predeterminado
        return False

# Llamada a la función y muestra de la matriz resultante
preguntas = leer_preguntas("preguntas.txt")
correctas = 0
incorrectas = 0
while preguntas:
    if generar_pregunta(preguntas):
        correctas += 1
    else:
        incorrectas += 1
    print(f"Respuestas correctas: {correctas}, Respuestas incorrectas: {incorrectas}")
