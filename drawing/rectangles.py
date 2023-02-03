import cairo
from IPython.display import Image, display
from math import pi
from io import BytesIO

def save(draw_func):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 210, 297)
    ctx = cairo.Context(surface)
    draw_func(ctx, 210, 297)
    with BytesIO() as fileobj:
        surface.write_to_png("image.png")


#@save
def make_rectangle(cr, width, height):
    
    cr.scale(width, height)
    cr.set_line_width(0.04)

    cr.rectangle(0.1, 0.1, 0.9, 0.6)
    cr.set_line_width(0.005)
    cr.set_source_rgb(0, 0, 0)
    cr.stroke()

    cr.push_group()
    cr.rectangle(0.3, 0.3, 0.6, 0.6)
    cr.set_source(cairo.SolidPattern(1, 0, 0))
    cr.fill_preserve()
    cr.set_source(cairo.SolidPattern(0, 0, 0))
    cr.stroke()
    cr.pop_group_to_source()
    cr.paint_with_alpha(0.5)

@save
def header(cr, width, height):
    
    cr.scale(width, height)
    cr.set_line_width(0.005)
    
    cr.rectangle(0.05, 0.1, 0., 0.6)
    cr.set_line_width(0.005)
    cr.set_source_rgb(0, 0, 0)
    cr.stroke()
  