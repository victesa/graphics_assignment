import cairo
import math

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 500
img_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, CANVAS_WIDTH, CANVAS_HEIGHT)
drawing_ctx = cairo.Context(img_surface)

drawing_ctx.set_source_rgb(1, 1, 1)
drawing_ctx.paint()

drawing_ctx.set_line_width(1)
drawing_ctx.move_to(100, 200)
drawing_ctx.line_to(500, 200)
drawing_ctx.line_to(500, 280)
drawing_ctx.line_to(450, 280)
drawing_ctx.line_to(450, 440)
drawing_ctx.line_to(150, 440)
drawing_ctx.line_to(150, 280)
drawing_ctx.line_to(100, 280)

drawing_ctx.set_source_rgb(0, 0, 1)
drawing_ctx.close_path()
drawing_ctx.stroke()

drawing_ctx.arc(300, 200, 100, math.pi, 2 * math.pi)
drawing_ctx.stroke()

drawing_ctx.set_line_width(1)

drawing_ctx.rectangle(190, 300, 60, 60)
drawing_ctx.set_source_rgb(0, 1, 0)
drawing_ctx.stroke()

drawing_ctx.move_to(220, 300)
drawing_ctx.line_to(220, 360)
drawing_ctx.set_source_rgb(0, 0, 1)
drawing_ctx.stroke()

drawing_ctx.move_to(190, 330)
drawing_ctx.line_to(250, 330)
drawing_ctx.stroke()

drawing_ctx.rectangle(350, 300, 60, 60)
drawing_ctx.set_source_rgb(0, 1, 0)
drawing_ctx.stroke()

drawing_ctx.move_to(380, 300)
drawing_ctx.line_to(380, 360)
drawing_ctx.set_source_rgb(0, 0, 1)
drawing_ctx.stroke()

drawing_ctx.move_to(350, 330)
drawing_ctx.line_to(410, 330)
drawing_ctx.stroke()

drawing_ctx.rectangle(270, 300, 60, 140)
drawing_ctx.set_source_rgb(0, 1, 0)
drawing_ctx.stroke()

drawing_ctx.arc(320, 370, 5, 0, 2 * math.pi)
drawing_ctx.set_source_rgb(0, 0, 1)
drawing_ctx.fill_preserve()
drawing_ctx.set_source_rgb(0, 0, 0.5)
drawing_ctx.set_line_width(3)
drawing_ctx.stroke()

gradient = cairo.LinearGradient(450, 100, 450, 140)
gradient.add_color_stop_rgb(0, 1, 1, 0)
gradient.add_color_stop_rgb(1, 0.9, 0.7, 0)


drawing_ctx.set_source(gradient)
drawing_ctx.set_line_width(1)
drawing_ctx.arc_negative(450, 100, 40, 5 * math.pi / 4, math.pi / 4)
drawing_ctx.curve_to(450, 125, 420, 120, 422, 70)
drawing_ctx.fill_preserve()
drawing_ctx.set_source_rgb(0, 0, 1) 
drawing_ctx.stroke()


    surface.write_to_png('test.png')

if __name__ == "__main__":
    main()

