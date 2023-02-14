import math
import drawSvg as draw
# отрисовка геологических крапов
# ГОСТ 21.302-2013
koef = 2480/210
# d = draw.Drawing(210*koef, 297*koef, origin=(0, 0), displayInline=False)
"""x = 100
y = 100
width = 30
height = 30
sediments = ('пески', 'глины', 'известняки')"""


def speck(d, x, y, width, height, sediments):
    # пески
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 3*koef
    delta_y = 2*koef
    delta = 0
    indent = 1
    i = 1
    # стартовые значения (пока для песков)
    y_start = (y - indent) * koef
    while y_start > (y - height + indent) * koef:
        x_start = (x + delta + indent) * koef
        while x_start < (width + x - indent) * koef:
            c = draw.Circle(x_start, y_start, 0.2*koef, fill='black')
            d.append(c)
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 1
        else:
            delta += 1
        y_start -= delta_y
    # d.savePng('spec.png')


# speck(d, x, y, width, height, sediments)
