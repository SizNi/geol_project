import cairo

def main():
    
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 210, 297)
    cr = cairo.Context(ims)
    
    cr.set_source_rgb(0, 0, 0)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(12)
    
    cr.move_to(0, 20)
    cr.show_text("Disziplin ist Macht.")
 
    ims.write_to_png("image.png")

 
        
        
