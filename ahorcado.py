from random import choice

palabras = ["carro","patines","motocicleta","bicicleta","ferrocarril","metrobus","triciclo","teleferico","patineta"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    ingreso = ""
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not es_valida:
        print("\n")
        ingreso = input("Por favor ingresa una letra: ").lower()
        print("\n")
        if ingreso in abecedario and len(ingreso) == 1:
            es_valida = True
        else:
            print("No haz elegido la letra correcta")

    return ingreso


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")

    print(" ".join(lista_oculta))


def revisar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias


def perder():
    print("\n")
    print("Te haz quedado sin vidas")
    print("\n")
    print("La palabra correcta era: " + palabra)
    print("\n")

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("\n")
    print("Felicitaciones haz encontrado la palabra!!!")
    print("\n")
    return True
print("------JUEGO DEL AHORCADO------")
palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*" * 30 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print(f"Letras incorrectas: " + "_".join(letras_incorrectas))
    print("\n")
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 30 + "\n")
    letra = pedir_letra()

    intentos, terminado, aciertos = revisar_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado