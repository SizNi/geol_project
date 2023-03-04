import drawSvg as draw
from format import frmt

# вкрапления

_, _, koef = frmt("a4")


def inclus(d, x, y, width, height, inclusions):
    for elem in inclusions:
        if elem == "глыбы":
            clumps(d, x, y, width, height)
        if elem == "валуны":
            boulders(d, x, y, width, height)


# единичная глыба
def clump(x_start, y_start, size):
    size = size * koef
    c = draw.Lines(
        x_start,
        y_start,
        x_start + 2.5 * size,
        y_start + 5.5 * size,
        x_start + 10.0 * size,
        y_start + 5.5 * size,
        x_start + 13.3 * size,
        y_start + 0.0 * size,
        x_start + 10.6 * size,
        y_start - 5.6 * size,
        x_start + 4.6 * size,
        y_start - 4.1 * size,
        x_start,
        y_start,
        close=True,
        fill="none",
        stroke="#ababab",
        stroke_width=3,
    )
    return c


# глыбы
def clumps(d, x, y, width, height):
    # размер единичной глыбы
    size = 1 / 5
    indent = 1 + 5 * size
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 30 * size * koef
    delta_y = 40 * size * koef
    delta = 1
    i = 1
    # стартовые значения
    y_start = (y - indent) * koef
    while y_start > (y - height + indent) * koef:
        x_start = (x + delta) * koef
        while x_start < (width + x) * koef:
            d.append(clump(x_start, y_start, size))
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 11 * size
        else:
            delta += 11 * size

        y_start -= delta_y


# единичный валун
def boulder(x_start, y_start, size, i):
    size = size * koef
    # угол наклона эллипса !! поправить
    if i % 2 == 1:
        angle = f"rotate(10, {x_start}, {y_start})"
    else:
        angle = f"rotate(0, {x_start}, {y_start})"
    c_1 = draw.Circle(
        x_start,
        y_start,
        0.4 * koef,
        fill="black",
    )
    c = draw.Ellipse(
        x_start,
        y_start,
        17 * size,
        9 * size,
        fill="none",
        stroke="#ababab",
        stroke_width=3,
        transform=angle,
    )
    return c, c_1


# валуны
def boulders(d, x, y, width, height):
    # размер единичного валуна
    size = 1 / 8
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 60 * size * koef
    delta_y = 30 * size * koef
    delta = 1
    i = 1
    # стартовые значения
    y_start = (y - delta - 9 * size / 2) * koef
    while y_start > (y - height + 9 * size / 2) * koef:
        x_start = (x + delta + 17 * size / 2) * koef
        while x_start < (width + x) * koef:
            c, c_1 = boulder(x_start, y_start, size, i)
            d.append(c)
            d.append(c_1)
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 11 * size
        else:
            delta += 11 * size
        y_start -= delta_y
