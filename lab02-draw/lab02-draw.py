import arcade

arcade.open_window(600, 600, "drawing example")

arcade.set_background_color(arcade.color.AZURE_MIST)
arcade.start_render()
#arcade.draw_circle_filled(20, 170, 50, arcade.color.BANANA_YELLOW)


def rectanguloRelleno(left,right,top,bottom,color):
    arcade.draw_lrtb_rectangle_filled(left,right,top,bottom,color)

def circuloRelleno(centro_x,centro_y,radio,color):
    arcade.draw_circle_filled(centro_x,centro_y,radio,color)

def arcoVacio(centro_x,centro_y,ancho,alto,color,angulo1,angulo2,ancho_borde,tilt_angle,num_segmentos):
    arcade.draw_arc_outline(centro_x,centro_y,ancho,alto,color,angulo1,angulo2,ancho_borde,tilt_angle,num_segmentos)


#suelo
rectanguloRelleno(0,600,150,0,arcade.color.AO)
rectanguloRelleno(0,600,160,150,arcade.color.BROWN_NOSE)

#carroceria
rectanguloRelleno(120,380,240,200,arcade.color.FERRARI_RED)
arcoVacio(240,240,70,60,arcade.color.FERRARI_RED,0,180,12,0,128)

#aleron
rectanguloRelleno(360,366,260,240,arcade.color.SMOKY_BLACK)
arcoVacio(363,260,30,3,arcade.color.SMOKY_BLACK,30,180,20,0,128)

#ruedas
circuloRelleno(160,180,20,arcade.color.JET)
circuloRelleno(340,180,20,arcade.color.JET)

#luces
rectanguloRelleno(125,140,250,240,arcade.color.FERRARI_RED)
rectanguloRelleno(120,125,250,240,arcade.color.YELLOW)


arcade.finish_render()
arcade.run()
