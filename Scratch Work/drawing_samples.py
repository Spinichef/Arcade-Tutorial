# this is a single-line comment
import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 330, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(200, 330, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 380, 60, 80, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(300, 330, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 350, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
arcade.draw_rectangle_filled(400, 330, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 410, 370, 330, 430, 330, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(500, 330, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 410),
                            (480, 370),
                            (470, 330),
                            (530, 330),
                            (520, 370)
                            ),
                           arcade.csscolor.DARK_GREEN)
arcade.finish_render()
arcade.run()
