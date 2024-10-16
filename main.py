import cairo
import math

def main():
    surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
    context = cairo.Context(surface)
    context.set_source_rgb(0.8, 0.8, 0.8)
    context.paint()

    context.set_source_rgb(0, 0, 0.4)
    context.set_line_width(5)



    context.move_to(100, 350)
    context.line_to(600, 350)#900, 350
    context.arc(350, 350, 150, math.pi, 0)
    context.line_to(900, 350)
    context.line_to(900, 500)
    context.line_to(800, 500)
    context.line_to(800, 950)
    context.line_to(200, 950)
    context.line_to(200, 500)
    context.line_to(100, 500)

    # context.line_to(600, 350)  # 900, 350
    # context.line_to(600, 450)  # 900, 500
    # context.line_to(550, 450)  # 800, 500
    # context.line_to(550, 700)  # 800, 950
    # context.line_to(150, 700)  # 200, 950
    # context.line_to(150, 450)  # 200, 500
    # context.line_to(100, 450)  # 100, 500






    context.close_path()
    context.stroke()

    surface.write_to_png('test.png')

if __name__ == "__main__":
    main()

