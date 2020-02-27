import arcade


# funciones de figuras
def rectanguloRelleno(left, right, top, bottom, color):
    arcade.draw_lrtb_rectangle_filled(left, right, top, bottom, color)


def circuloRelleno(centro_x, centro_y, radio, color):
    arcade.draw_circle_filled(centro_x, centro_y, radio, color)


def arcoVacio(centro_x, centro_y, ancho, alto, color, angulo1, angulo2, ancho_borde, tilt_angle, num_segmentos):
    arcade.draw_arc_outline(centro_x, centro_y, ancho, alto, color, angulo1, angulo2, ancho_borde, tilt_angle,
                            num_segmentos)


def suelo():
    # imprime el suelo
    rectanguloRelleno(0, 600, 150, 0, arcade.color.AO)  # cesped
    rectanguloRelleno(0, 600, 160, 150, arcade.color.BROWN_NOSE)  # tierra


def coche(x, y):
    # imprime el coche
    # carroceria

    arcade.draw_point(x, y, arcade.color.RED, 20)

    rectanguloRelleno(120 + x, 380 + x, 240 + y, 200 + y, arcade.color.FERRARI_RED)
    arcoVacio(240 + x, 240 + x, 70 + y, 60 + y, arcade.color.FERRARI_RED, 0, 180, 12, 0, 128)
    # aleron
    rectanguloRelleno(360 + x, 366 + x, 260 + y, 240 + y, arcade.color.SMOKY_BLACK)
    arcoVacio(363 + x, 260 + y, 30, 3, arcade.color.SMOKY_BLACK, 30, 180, 20, 0, 128)
    # ruedas
    circuloRelleno(160 + x, 180 + y, 20, arcade.color.JET)
    circuloRelleno(340 + x, 180 + y, 20, arcade.color.JET)
    # luces
    rectanguloRelleno(125 + x, 140 + x, 250 + y, 240 + y, arcade.color.FERRARI_RED)
    rectanguloRelleno(120 + x, 125 + x, 250 + y, 240 + y, arcade.color.YELLOW)

    on_draw.coche_x += 1


def on_draw(delta_time):
    arcade.start_render()

    suelo()
    coche(on_draw.coche_x, 0)


on_draw.coche_x = 160


def main():
    arcade.open_window(600, 600, "drawing example")

    arcade.set_background_color(arcade.color.AZURE_MIST)
    arcade.schedule(on_draw(), 1 / 60)
    arcade.finish_render()
    arcade.run()
