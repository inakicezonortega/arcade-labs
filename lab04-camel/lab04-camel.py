import arcade
import random

def menu():
    print("0. Beber de la botella (agua+70, gasta 1 turno y 1 sorbo).\n"       
          "1. Caminar (distancia+(6-12), gasta 1 turno y 15 de energia).\n"
          "2. Correr (distancia+(15-21), gasta 1 turno y 25 de energia).\n"
          "3. Descansar (energia+75, gasta 1 turno).\n"
          "4. Mirar estado actual(GRATIS).\n"
          "5. Salir.")

def leerAccion():
    num_accion = int(input("Introduce la accion deseada: "))

    return num_accion

def accion0(sorbos,sed):
    sorbos -= 1
    sed += 70
    print("Ahora tienes ", sed, " de agua y te quedan ", sorbos, " sorbos")
    return sorbos, sed

def accion1(energia,distancia_recorrida,distancia_personaje,distancia_avanzada):
    energia -= 15
    distancia_recorrida = 0
    distancia_recorrida = random.randint(6, 12)
    distancia_personaje = distancia_personaje - distancia_recorrida
    distancia_avanzada = distancia_avanzada + distancia_recorrida
    print("Has avanzado ", distancia_recorrida, "metros")
    return energia,distancia_recorrida,distancia_personaje,distancia_avanzada

def accion2(energia,distancia_recorrida, distancia_personaje,distancia_avanzada):
    energia -= 25
    distancia_recorrida = 0
    distancia_recorrida = random.randint(15, 21)
    distancia_personaje = distancia_personaje - distancia_recorrida
    distancia_avanzada = distancia_avanzada + distancia_recorrida
    print("Has avanzado ", distancia_recorrida, " metros")
    return energia,distancia_recorrida, distancia_personaje,distancia_avanzada

def imprimirVariablesEstado(sorbos,distancia_personaje,distancia_a_nativos,energia,sed):

    print("Tienes ",sorbos," sorbos y ",sed," de agua")
    print("Te falta por recorrer ",distancia_personaje,"metros")
    print("Los nativos estan a ",distancia_a_nativos," metros")
    print("Tienes ",energia," energia")

def finTurno (distancia_nativos_recorrida,sed,energia,distancia_avanzada):
    distancia_nativos_recorrida += 10
    distancia_a_nativos = distancia_avanzada-distancia_nativos_recorrida
    sed -= 20
    energia -= 10
    return distancia_nativos_recorrida,sed,energia,distancia_a_nativos

def comprobarEstado (sed,energia,aux,sorbos):
    aux_secundaria = True
    if (sed <= 0 and sorbos > 0):
        print("Estas sin agua, tienes que beber (pulsa '0')")
        while aux_secundaria:
            num_accion = leerAccion()
            if num_accion == 1 or num_accion == 2:
                print("Estas demasiado sediento para esa accion")
            else:
                aux_secundaria = False
    elif (sed <= 0 and sorbos == 0):
        print("Te has deshidratado y te queda agua, HAS PERDIDO")
        aux = False
    if (energia <= 0):
        print("Estas sin energia, tienes que descansar (pulsa '3')")
        while aux_secundaria:
            num_accion = leerAccion()
            if num_accion == 1 or num_accion == 2:
                print("Estas demasiado cansado para esa accion")
            aux_secundaria = False
    if (sed > 0 and energia > 0):
        menu()
        num_accion = leerAccion()
        aux_sorbos = True
        while aux_sorbos:
            if num_accion == 0 and sorbos == 0:
                print("No te quedan sorbos, elige otra accion")
                num_accion = leerAccion()
            else:
                aux_sorbos = False
    return aux,num_accion


def main():
    sorbos = 3
    distancia_personaje = 200
    distancia_nativos_recorrida = -30
    energia = 250
    sed = 140
    distancia_recorrida = 0
    distancia_avanzada = 0
    distancia_a_nativos = distancia_avanzada-distancia_nativos_recorrida
    aux = True
    num_accion = ''
    while (aux):
        aux,num_accion = comprobarEstado(sed,energia,aux,sorbos)
        if distancia_a_nativos <= 0:
            print("Los nativos te han alcanzado, HAS PERDIDO")
            aux = False

        if num_accion == 0:
            sorbos, sed = accion0(sorbos, sed)
            distancia_nativos_recorrida, sed, energia, distancia_a_nativos = finTurno(distancia_nativos_recorrida, sed, energia,distancia_avanzada)

        elif num_accion == 1:
            energia, distancia_recorrida, distancia_personaje, distancia_avanzada = \
                accion1(energia, distancia_recorrida, distancia_personaje, distancia_avanzada)
            distancia_nativos_recorrida, sed, energia, distancia_a_nativos = finTurno(distancia_nativos_recorrida, sed, energia, distancia_avanzada)

        elif num_accion == 2:
            energia, distancia_recorrida, distancia_personaje, distancia_avanzada = \
                accion2(energia, distancia_recorrida, distancia_personaje, distancia_avanzada)
            distancia_nativos_recorrida, sed, energia,distancia_a_nativos = finTurno(distancia_nativos_recorrida, sed, energia, distancia_avanzada)

        elif num_accion == 3:
            energia += 75
            print("Tu energia actual es ", energia)
            distancia_nativos_recorrida, sed, energia,distancia_a_nativos = finTurno(distancia_nativos_recorrida, sed, energia, distancia_avanzada)

        elif num_accion == 4:
            imprimirVariablesEstado(sorbos,distancia_personaje,distancia_a_nativos, energia, sed)

        elif num_accion == 5:
            aux = False

        if distancia_a_nativos <= 10:
            print("Cuidado, los nativos te van a alcanzar")

        if distancia_personaje <= 0:
            print("Has llegado a salvo al destino, HAS GANADO")
            aux = False

main()

