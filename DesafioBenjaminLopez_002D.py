import random
# Banco de preguntas precargado: LISTA DE DICCIONARIOS (no lo modifiques)
banco_preguntas = [
    {"pregunta": "Cual es la capital de Chile?", "respuesta": "Santiago"},
    {"pregunta": "Cuanto es 7 por 8?", "respuesta": "56"},
    {"pregunta": "Que palabra clave define una funcion en Python?", "respuesta": "def"},
    {"pregunta": "Cual es el simbolo del resto (modulo) en Python?", "respuesta": "%"},
    {"pregunta": "Que tipo de dato es 3.14?", "respuesta": "float"},
    {"pregunta": "Cuantos colores tiene el arcoiris?", "respuesta": "7"},
    {"pregunta": "Que funcion muestra texto en pantalla en Python?", "respuesta": "print"},
    {"pregunta": "Cual es el oceano que limita con Chile?", "respuesta": "Pacifico"},
]


def mostrar_pregunta(pregunta):
    print(pregunta["pregunta"])


def normalizar(texto):
    return texto.lower().strip()

def es_correcta(respuesta_usuario, respuesta_correcta):
    return normalizar(respuesta_usuario) == normalizar(respuesta_correcta)

def jugar_ronda(jugador, banco, n):
    puntaje = 0
    preguntas = random.sample(banco, n)

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = input("Respuesta: ")

        if es_correcta(respuesta, pregunta["respuesta"]):
            print("Correcto!")
            puntaje += 1
        else:
            print("Incorrecto.")
    
    return puntaje


def mostrar_ranking(jugadores):
    print("\n=== RANKING! ===")

    ordenados = sorted(
        jugadores,
        key=lambda jugador: jugador["puntaje"],
        reverse = True
    )

    posicion = 1
    for jugador in ordenados:
        if jugador["preguntas"] > 0:
            porcentaje = jugador["puntaje"] / jugador["preguntas"] * 100
        else:
            porcentaje = 0

        print(
            f"{posicion}. {jugador["nombre"]}  "
            f"{jugador["puntaje"]} puntos  "
            f"{porcentaje:.2f}%"
        )

        posicion += 1

def main():
    print("=== JUEGO DE TRIVIA POR RONDAS ===")
    preguntas_por_ronda = 5

    # Lectura protegida con try/except (ya resuelto, no lo cambies)
    try:
        cantidad_jugadores = int(input("Cuantos jugadores van a jugar? "))
    except ValueError:
        print("Entrada invalida. Se asume 1 jugador.")
        cantidad_jugadores = 1

    jugadores = []
    numero = 1
    
    while numero <= cantidad_jugadores:
        nombre = input(f"\nNombre del jugador {numero}: ")
        puntaje = jugar_ronda(nombre, banco_preguntas, preguntas_por_ronda)

        jugadores.append({
            "nombre":nombre,
            "puntaje":puntaje,
            "preguntas":preguntas_por_ronda
        })

        numero = numero + 1

    mostrar_ranking(jugadores)
    print("\nGracias por jugar!")


main()