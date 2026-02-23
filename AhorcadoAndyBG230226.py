import random

juega = True
vidas = 6

palabras = [
    "tenge", "tis", "plinplanta", "moltres", "piplup",
    "invitamemarito", "balatrito", "supercalifragilisticoespialidoso"
]

palabra_juego = random.choice(palabras)
letras = list(palabra_juego)

# lista de letras adivinadas (inicialmente todo oculto)
progreso = ["_" for _ in letras]

letras_usadas = []
print(" ".join(progreso))

while juega and vidas > 0:

    intento = input("Escribe una letra: ").lower()

 
    if len(intento) != 1 or not intento.isalpha():
        print("Ingresa UNA letra.")
        continue

    letras_usadas.append(intento)

    if intento in letras:
        print("¡Correcto!")

        for i in range(len(letras)):
            if letras[i] == intento:
                progreso[i] = intento
    else:
        vidas -= 1
        print("La letra es... incorrecta.")
        print(f"Te quedan {vidas} vidas.")

    print(" ".join(progreso))

    if "_" not in progreso:
        print("¡Ganaste!")
        juega = False

if vidas == 0:
    print("Perdiste. La palabra era:", palabra_juego)
