from random import randint

respuesta = "s"
puntajedeljugador = 0
puntajedelacompu = 0
while respuesta == "s":
    print("*" * 55)
    print("            Piedra , Papel o Tijera")
    print("*" * 55)
    jugador = input("Escribe tu jugada: piedra, papel o tijera: ")

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("La computadora elige: ", computadora)

    if computadora == jugador:
        print("Es un empate.")
    elif computadora == "piedra" and jugador == "tijera":
        print("Gana la computadora.")
        puntajedelacompu += 1
    elif computadora == "papel" and jugador == "tijera":
        print("Tu ganaste.")
        puntajedeljugador += 1
    elif computadora == "tijera" and jugador == "piedra":
        print("Tu ganaste.")
        puntajedeljugador += 1
    elif computadora == "papel" and jugador == "piedra":
        print("Gana la computadora.")
        puntajedelacompu += 1
    elif computadora == "piedra" and jugador == "papel":
        print("Tu ganaste.")
        puntajedeljugador += 1
    elif computadora == "tijera" and jugador == "papel":
        print("Gana la computadora.")
        puntajedelacompu += 1
    print("///////////////////////////////////////")
    print("El puntaje del jugador es: ", puntajedeljugador)
    print("El puntaje de la computadora: ", puntajedelacompu)
    print("///////////////////////////////////////")
    print("-----------------------------------------------------------")
    respuesta = input("Desea seguir jugando: Responda Si(s) o No(n): ")
    print("-----------------------------------------------------------")
