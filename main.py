import cairo
import math

def main():
    surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1090)
    context = cairo.Context(surface)
    context.set_source_rgb(0.8, 0.8, 0.8)
    context.paint()

    # context.set_source_rgb(0, 0, 0.4)
    # context.set_line_width(5)


    # House Shape
    context.move_to(100, 500)
    context.line_to(950, 500)
    context.line_to(950, 600)
    context.line_to(850, 600)
    context.line_to(850, 1050)
    context.line_to(200, 1050)
    context.line_to(200, 600)
    context.line_to(100, 600)
    context.line_to(100, 500)
    context.set_line_width(3)
    context.set_source_rgb(0, 0.7, 1)
    context.stroke()

    context.close_path()
    context.stroke()

    surface.write_to_png('test.png')

if __name__ == "__main__":
    main()

