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
    context.arc(320, 370, 5, 0, 2 * math.pi)
    context.set_source_rgb(0, 0, 1)
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0.5)
    context.set_line_width(3)
    context.stroke()
    
    gradient = cairo.LinearGradient(450, 100, 450, 140)
    gradient.add_color_stop_rgb(0, 1, 1, 0)
    gradient.add_color_stop_rgb(1, 0.9, 0.7, 0)
    
    
    context.set_source(gradient)
    context.set_line_width(1)
    context.arc_negative(450, 100, 40, 5 * math.pi / 4, math.pi / 4)
    context.curve_to(450, 125, 420, 120, 422, 70)
    context.fill_preserve()
    context.set_source_rgb(0, 0, 1) 
    context.stroke()



    context.move_to(450,1050)
context.line_to(450,700)
context.line_to(600,700)
context.line_to(600,1050)
context.close_path()
context.set_source_rgb(0.4, 0.8, 0)
context.set_line_width(5)
context.stroke()


context.arc(570, 890, 12.5, 0, 2*math.pi)
context.set_source_rgb(0,0.5,1)
context.fill_preserve()
context.set_line_width(5)
context.set_source_rgb(0,0,0.8)
context.stroke()


    surface.write_to_png('test.png')

if __name__ == "__main__":
    main()

