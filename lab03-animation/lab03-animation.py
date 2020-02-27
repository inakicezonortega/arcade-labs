import arcade


def suelo():
    # imprime el suelo
    arcade.draw_lrtb_rectangle_filled(0, 600, 150, 0, arcade.color.AO)  # cesped
    arcade.draw_lrtb_rectangle_filled(0, 600, 160, 150, arcade.color.BROWN_NOSE)  # tierra


def coche(x):
    # imprimir el coche
    # carroceria

    arcade.draw_point(x,150, arcade.color.RED, 20)

    arcade.draw_lrtb_rectangle_filled(120 + x, 380 + x, 240, 200, arcade.color.FERRARI_RED)
    arcade.draw_arc_outline(240 + x, 240, 70, 60, arcade.color.FERRARI_RED, 0, 180, 12, 0, 128)
    # aleron
    arcade.draw_lrtb_rectangle_filled(360 + x, 366 + x, 260, 240, arcade.color.SMOKY_BLACK)
    arcade.draw_arc_outline(363 + x, 260, 30, 3, arcade.color.SMOKY_BLACK, 30, 180, 20, 0, 128)
    # ruedas
    arcade.draw_circle_filled(160 + x, 180, 20, arcade.color.JET)
    arcade.draw_circle_filled(340 + x, 180, 20, arcade.color.JET)
    # luces
    arcade.draw_lrtb_rectangle_filled(125 + x, 140 + x, 250, 240, arcade.color.FERRARI_RED)
    arcade.draw_lrtb_rectangle_filled(120 + x, 125 + x, 250, 240, arcade.color.YELLOW)


def on_draw(delta_time):
    arcade.start_render()

    suelo()
    coche(on_draw.coche_x)
    if on_draw.coche_x == 300 or on_draw.coche_x == 0:

        on_draw.coche_x *= -1
    on_draw.coche_x += 2

on_draw.coche_x = -100


def main():
    arcade.open_window(600, 600, "drawing example")

    arcade.set_background_color(arcade.color.AZURE_MIST)
    arcade.schedule(on_draw, 1 / 60)

    arcade.finish_render()
    arcade.run()

main()