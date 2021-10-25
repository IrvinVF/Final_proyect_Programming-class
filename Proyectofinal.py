#Irvin Vásquez Figueroa
#A01541101
#JUEGO DEL AHORCADO
#Objetivo: El usuario jugará al ahorcado, tratando de adivinar todas las letras de la palabra escogida al azar.
import random
#Se importa el módulo random para escoger las palabras al azar.
file = open("textofinal.txt", "r")
#Se abre el archivo de texto en modo de lectura
diccionario = {}
#Se crea un diccionario, el cual tendra las palabras con sus definiciones del archivo de texto
for linea in file:
    prueba = linea.split(":")
    if(prueba):
        diccionario[prueba[0]] = prueba[1][1:-1]
#Se hace un ciclo for para leer línea por línea el archivo de texto
#En donde, el split servirá para separar de una lista cada vez que encuentre dos puntos.
#El if será para que el diccionario agarre el índice 0 de prueba -es decir, la palabra a adivinar- y lo relacione con...
#El índice 1 -es decir, la definición de la palabra a adivinar-.
#Además, la definición solo se tomará en cuenta a partir del primer índice hasta el penúltimo índice, para eliminar los "\n" que haya.


palabra = random.choice(list(diccionario.keys()))
#La palabra a adivinar se escogerá al azar, tomándola del diccionario.
#Se hará ÚNICAMENTE con las key del diccionario, es decir, discriminando las definiciones.

print("¡Bienvenido al juego del ahorcado! <3")
print("Para ganar, deberás adivinar la palabra con respecto a la definición de ésta.")
print("¡Recuerda! Solo tienes 3 intentos ;D")
print("¿Listo? ¡Ahora!    ૮₍˶• . • ⑅₎ა.  ")
print()
#Mensaje de bienvenida

print("La palabra a adivinar tiene: " , len(palabra), " letras ;)")
#Se imprime el número de letras de la palabra a adivinar.
print("_ "*len(palabra), ": ", diccionario[palabra])
#Como el fomato del juego del ahorcado, se imprimen guiones bajo representando el # de letras a adivinar de la palabra
#Posterior a esto, se imprime la definición de la palabra escogida al azar.

letras_correctas = []
#Se hace un array para almacenar las letras correctas que el usuario ingrese a continuación.

intentos = 3
# intentos que tendrá el usuario

while True:
    #Se hace un While que SIEMPRE se ejecutará, a menos que se haga un break en dos escenarios más abajo.
    #Al ser un bucle, se permite que el usuario pueda seguir jugando si es que sigue teniendo intentos.
    letra = input("Escribe una letra c: ")
    #Se le pide al usuario una letra

    if letra.lower() in palabra:
        print ("¡Muy bien! Acertaste <3")
        letras_correctas.append(letra.lower())
        #Si la letra -que siempre es en minúscula- está en alguna de las letras de la palabra, la letra correcta se irá al banco de letras_correctas
    else:
        intentos -=1
        print("Lo siento, esa no es :c")
        print("Número de intentos: " , intentos)
        #De no acertar alguna de las letras de la palabra, se le resta un intento.

    if intentos ==0:
        print("¡Oh no! Perdiste :c")
        print("La palabra correcta fue: " , palabra)
        break
    #Si no le quedan intentos al usuario, se ejecuta el break, el cual hace que se rompa el ciclo while y se pierda el juego.

    mostrar = ""
    guiones = 0
    #Valores que nos servirán para imprimir como va el avance del jugador en la palabra a adivinar
    #Y también revisar si el usuario ya ganó el juego.
    for a in palabra:
        #Se hace un for para escanear letra por letra de la palabra a adivinar
        if a.lower() in letras_correctas:
            #Si a es una de las letras correctas que ingresó el usuario, mostrar será igual a mostrar más la letra correcta, más un espacio en blanco.
            mostrar +=a+ " "
        else:
            mostrar+="_ "
            guiones +=1
            #Si no es así, mostraar será igual a mostrar más un guión bajo
            #Y se le agrega uno al valor de guiones

            #Esto se hace para que, si el usuario acierta una o más letras de la palabra, los guiones bajos de la palabra sean reemplazandos...
            #Por la letra o letras adivinadas en el intento.
            #Y si en ese intento no se adivina ninguna letra, la palabra seguirá igual
    print(mostrar)
    #Se imprime el avance del jugador
    
    if guiones ==0:
        #Si los guiones del avance del jugador es cero -es decir, que ya no hay huecos para adivinar letras porque ya adivinó...
        #Entonces se gana el juego
        print("¡Felicitaciones! Has ganado el juego, ¡Siéntete orgulloso!  ⸜(｡˃ ᵕ ˂ )⸝ ")
        break
    #Se imprime un mensaje de felicitación, con otro break

#Es decir, que para salir del bucle while, solo se podrá romper si el usuario acierta todas las letras (victoria) o pierde sus intentos (derrota)



file.close()
#Se cierra el archivo.

#Se termina el proyecto final. ¡Gracias por su clase maestra! ⸜(｡˃ ᵕ ˂ )⸝
#Gracias. <33
