import arcade
import random

def menu():
    print("0. Drink from your canteen.\n"       
          "1. Ahead moderate speed.\n"
          "2. Ahead full speed.\n"
          "3. Stop for the night.\n"
          "4. Status check.\n"
          "5. Quit.")

def leerAccion():
    num_accion = int(input("Introduce la accion deseada: "))

    return num_accion




def accion0(sorbos,sed):
    sorbos -= 1
    sed += 70
    print("Ahora tienes ", sed, " de agua y te quedan ", sorbos, " sorbos")
    return sorbos, sed

def accion1(energia,distancia_recorrida,distancia,personaje,distancia_avanzada):
    energia -= 15
    distancia_recorrida = random.randint(6, 12)
    distancia_personaje = distancia_personaje - distancia_recorrida
    distancia_avanzada = distancia_avanzada + distancia_recorrida
    print("Has avanzado ", distancia_avanzada, "metros")
    return energia,distancia_recorrida,distancia,personaje,distancia_avanzada

def accion2(energia,distancia_recorrida, distancia_personaje,distancia_avanzada):
    energia -= 25
    distancia_recorrida = random.randint(15, 21)
    distancia_personaje = distancia_personaje - distancia_recorrida
    distancia_avanzada = distancia_avanzada + distancia_recorrida
    print("Has avanzado ", distancia_avanzada, " metros")
    return energia,distancia_recorrida, distancia_personaje,distancia_avanzada

def imprimirVariablesEstado(sorbos,distancia_personaje,distancia_avanzada,distancia_nativos,energia,sed):

    print("Tienes ",sorbos," sorbos y ",sed," de agua")
    print("Te falta por recorrer ",distancia_personaje,"metros")
    print("Los nativos estan a ",distancia_avanzada - distancia_nativos," metros")
    print("Tienes ",energia," energia")


def main():
    sorbos = 3
    distancia_personaje = 200
    distancia_nativos = -20
    energia = 250
    sed = 100
    distancia_avanzada = 0
    aux = True
    while aux and distancia_personaje > 0 and sed > 0:
        menu()
        num_accion = leerAccion()
        #ejecutarAccion(sorbos,distancia_personaje,distancia_avanzada,distancia_nativos,energia,sed,leerAccion())
        if num_accion == 0:
            sorbos, sed = accion0(sorbos, sed)
            return sorbos, sed

        elif num_accion == 1:
            energia, distancia_recorrida, distancia, personaje, distancia_avanzada = \
                accion1(energia, distancia_recorrida, distancia, personaje, distancia_avanzada)
            return energia, distancia_recorrida, distancia_personaje, distancia_avanzada

        elif num_accion == 2:
            energia, distancia_recorrida, distancia_personaje, distancia_avanzada = \
                accion2(energia, distancia_recorrida, distancia_personaje, distancia_avanzada)
            return energia, distancia_recorrida, distancia_personaje, distancia_avanzada

        elif num_accion == 3:
            energia += 75
            print("Tu energia actual es ", energia)
            return energia

        elif num_accion == 4:
            imprimirVariablesEstado(sorbos, distancia_personaje, distancia_avanzada, distancia_nativos, energia, sed)

        elif num_accion == 5:
            aux = False


main()

