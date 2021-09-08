from random import randint
 
choice = ["roca","papel","tijera"]
def main():
    computer = choice[randint(0,2)]
 
    print("Bienvenido al juego Piedra, papel y tijeras \ n")
    player = input("tu eleccion: ").lower()
    print("Computadora eligio: " + computer)
 
    if player == computer:
        print("dibujar")
    elif player == "roca" and computer == "papel":
        print("Computadora eligio")
    elif player == "roca" and computer == "tijera":
        print("Ganador")
    elif player == "papel" and computer == "roca":
        print("Ganador")
    elif player == "papel" and computer == "tijera":
        print("Ganador")
    elif player == "tijera" and computer  == "roca":
        print("Computadora elegio")
    elif player == "tijera" and computer == "papel":
        print("Ganador")
    elif player == "fin":
        StopIteration
 
    main()
 
main()