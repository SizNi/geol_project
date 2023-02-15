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

    if len(sediments) == 1:
        if sediments[0] == 'пески':
            sands(d, x, y, width, height)
        elif sediments[0] == 'глины':
            clays(d, x, y, width, height)
        elif sediments[0] == 'известняки':
            limestones(d, x, y, width, height)
        elif sediments[0] == 'суглинки':
            loams(d, x, y, width, height)


# пески
def sands(d, x, y, width, height):
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 3*koef
    delta_y = 2*koef
    delta = 0
    indent = 1
    i = 1
    # стартовые значения
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


# глины
def clays(d, x, y, width, height):
    delta_y = 1.5*koef
    indent = 1
    y_start = (y - indent) * koef
    while y_start > (y - height + indent) * koef:
        c = draw.Lines(x*koef, y_start, (x + width) *
                       koef, y_start, stroke='black')
        d.append(c)
        y_start -= delta_y


# известняки
def limestones(d, x, y, width, height):
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_y = 3*koef
    delta_x = 4*delta_y
    delta = 0
    # начальный отступ
    indent = 1
    i = 0
    # стартовые значения
    y_start = y * koef
    x_start = (x + indent) * koef
    while y_start > (y - height) * koef:
        c = draw.Lines(x*koef, y_start, (x + width) *
                       koef, y_start, stroke='black')
        d.append(c)
        while x_start < (width + x - indent) * koef:
            # следующий цикл нужен, чтоб обрезать вертикальные линии,
            # которые могут вылезти за пределы слоя
            if (i + 1) * delta_y <= height * koef:
                c = draw.Lines(x_start, y_start, x_start,
                               y_start - delta_y, stroke='black')
                d.append(c)
                x_start += delta_x
            else:
                # x2 - как раз смещение минус разница, вылезающая за пределы
                c = draw.Lines(x_start, y_start, x_start, y_start - delta_y +
                               ((i + 1) * delta_y - height * koef), stroke='black')
                d.append(c)
                x_start += delta_x
                x_start += delta_x
        i += 1
        # смещение начальной точки
        if i % 2 == 0:
            delta -= delta_x/2
        else:
            delta += delta_x/2
        # обнуление начальной точки + смещение
        x_start = (x + indent) * koef + delta
        y_start -= delta_y


# суглинки, угол наклона - 30 градусов
def loams(d, x, y, width, height):
    delta_y = 5*koef
    # регулировка угла наклона (в нашем случае 30 градусов)
    tg_30 = 0.57735026919
    delta_x = tg_30 * delta_y
    y_start = y * koef
    x_start = x * koef
    # отрисовываем с левого угла
    while y_start >= (y - height) * koef + delta_y and x_start <= (x + width) * koef:
        c = draw.Lines(
            x*koef, y_start - delta_y,
            x_start + delta_x, y*koef,
            stroke='black'
        )
        d.append(c)
        y_start -= delta_y
        x_start += delta_x
    # переназначаем начальные значения
    # обрезанный кусок нижнего левого угла
    x_low_start = ((y-height)*koef - y_start) * tg_30 + delta_x
    while x_start <= (x + width) * koef - delta_x:
        c = draw.Lines(
            x * koef + x_low_start, (y - height) * koef,
            x_start + delta_x, y*koef,
            stroke='black'
        )
        d.append(c)
        x_low_start += delta_x
        x_start += delta_x
    # правый нижний угол
    # переназначаем начальные значения
    # обрезанный кусок нижнего левого угла
    ctg_30 = 1.732050808
    y_right_start = delta_y - (delta_x - (x_start + delta_x - (x+width)*koef))/tg_30
    while y * koef - y_right_start >= (y - height) * koef:
        #print(y_right_start)
        c = draw.Lines(
            x*koef + x_low_start, (y - height) * koef,
            (x + width)*koef, y*koef - y_right_start,
            stroke='black'
        )
        d.append(c)
        y_right_start += delta_y
        x_low_start += delta_x