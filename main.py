import cairo
import math

def main():
    surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 750)
    context = cairo.Context(surface)
    context.set_source_rgb(0.8, 0.8, 0.8)
    context.paint()

    context.set_source_rgb(0, 0, 1)
    context.set_line_width(5)



    context.move_to(100, 350)
    context.line_to(600, 350)
    context.line_to(600, 450)
    context.line_to(550, 450)
    context.line_to(550, 700)
    context.line_to(150, 700)
    context.line_to(150, 450)
    context.line_to(100, 450)

    context.close_path()
    context.stroke()

    surface.write_to_png('test.png')

if __name__ == "__main__":
    main()

