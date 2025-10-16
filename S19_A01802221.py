import random

eleccionComputadora = random.choice(["Piedra", "Papel", "Tijera"])
print("La computadora eligió:", eleccionComputadora)

eleccionJugador = input("¿Quieres Piedra, Papel o Tijera?: ")

if eleccionComputadora == eleccionJugador:
    print("¡Empate!")

if eleccionComputadora == "Tijera" and eleccionJugador == "Piedra":
    print("¡El jugador gana!")

if eleccionComputadora == "Papel" and eleccionJugador == "Tijera":
    print("¡El jugador gana!")

if eleccionComputadora == "Tijera" and eleccionJugador == "Papel":
    print("¡La computadora gana!")

if eleccionComputadora == "Piedra" and eleccionJugador == "Tijera":
    print("¡La computadora gana!")

if eleccionComputadora == "Piedra" and eleccionJugador == "Papel":
    print("¡El jugador gana!")

if eleccionComputadora == "Papel" and eleccionJugador == "Piedra":
    print("¡La computadora gana!")
