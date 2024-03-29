import drawSvg as draw
from drawing.format import frmt

# вкрапления

_, _, koef = frmt("a4")


def inclus(d, x, y, width, height, inclusions):
    inclusion_functions = {
        "глыбы": clumps,
        "валуны": boulders,
        "галька": pebbles,
        "щебень": gravels,
        "гравий": grits,
        "фосфориты": phosphorites,
    }

    for elem in inclusions:
        if elem in inclusion_functions:
            inclusion_functions[elem](d, x, y, width, height)


# единичная глыба
def clump(x_start, y_start, size):
    size = size * koef
    coordinates = [
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
    ]
    c = draw.Lines(
        *coordinates, close=True, fill="none", stroke="#ababab", stroke_width=3
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
    c = draw.Ellipse(
        x_start,
        y_start,
        17 * size,
        9 * size,
        fill="none",
        stroke="#ababab",
        stroke_width=3,
    )
    return c


# валуны
def boulders(d, x, y, width, height):
    # размер единичного валуна
    size = 1 / 8
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 80 * size * koef
    delta_y = 50 * size * koef
    delta = 2
    i = 1
    # стартовые значения
    y_start = (y - delta - 9 * size / 2) * koef
    while y_start > (y - height + 9 * size / 2) * koef:
        x_start = (x + delta + 17 * size / 2) * koef
        while x_start < (width + x) * koef:
            d.append(boulder(x_start, y_start, size, i))
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 40 * size
        else:
            delta += 40 * size
        y_start -= delta_y


# единичная галька
def pebble(x_start, y_start, size):
    size = size * koef
    c = draw.Ellipse(
        x_start,
        y_start,
        13 * size,
        8 * size,
        fill="none",
        stroke="#ababab",
        stroke_width=3,
    )
    return c


# галька
def pebbles(d, x, y, width, height):
    # размер
    size = 1 / 10
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 62 * size * koef
    delta_y = 62 * size * koef
    delta = 1
    i = 1
    # стартовые значения
    y_start = (y - delta - 8 * size / 2) * koef
    while y_start > (y - height + 9 * size / 2) * koef:
        x_start = (x + delta + 13 * size / 2) * koef
        while x_start < (width + x) * koef:
            d.append(pebble(x_start, y_start, size))
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 29 * size
        else:
            delta += 29 * size
        y_start -= delta_y


# единичный щебень
def gravel(x_start, y_start, size, i):
    size = size * koef
    dy = -15 * size if i % 2 == 1 else 15 * size
    c = draw.Lines(
        x_start,
        y_start,
        x_start + 15 * size,
        y_start + 0 * size,
        x_start + 7.5 * size,
        y_start + dy,
        x_start,
        y_start,
        close=True,
        fill="none",
        stroke="#ababab",
        stroke_width=3,
    )
    return c


# щебень
def gravels(d, x, y, width, height):
    # размер
    size = 1 / 5
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 48 * size * koef
    delta_y = 30 * size * koef
    delta = 0.3
    i = 1
    # стартовые значения
    y_start = (y - delta) * koef
    while y_start > (y - height + 9 * size) * koef:
        x_start = (x + delta) * koef
        while x_start < (width + x) * koef:
            d.append(gravel(x_start, y_start, size, i))
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= 23 * size
        else:
            delta += 23 * size
        y_start -= delta_y


# единичный гравий
def grit(x_start, y_start, size):
    size = size * koef
    c = draw.Circle(
        x_start,
        y_start,
        4 * size,
        fill="none",
        stroke="#ababab",
        stroke_width=2,
    )
    return c


# гравий
def grits(d, x, y, width, height):
    # размер
    size = 1 / 10
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 69 * size * koef
    delta_y = 18 * size * koef
    delta = 1
    i = 1
    # стартовые значения
    y_start = (y - delta - 4 * size / 2) * koef
    while y_start > (y - height + 4 * size / 2) * koef:
        x_start = (x + delta + 4 * size / 2) * koef
        while x_start < (width + x) * koef:
            d.append(grit(x_start, y_start, size))
            x_start += delta_x
        if i == 1:
            delta += 18 * size
            i += 1
        elif i == 2:
            delta += 18 * size
            i += 1
        else:
            delta -= 36 * size
            i = 1
        y_start -= delta_y


# единичный фосфорит
def phosphorite(x_start, y_start, size):
    size = size * koef
    x_1 = 15
    y_1 = 11 * x_1 / 28.4
    c = draw.Ellipse(
        x_start,
        y_start,
        x_1 * size,
        y_1 * size,
        fill="none",
        stroke="black",
        stroke_width=2,
    )
    b = draw.Ellipse(
        x_start + 5.6 * size,
        y_start,
        (17.2 * x_1 / 28.4) * size,
        (8.4 * y_1 / 11) * size,
        fill="black",
        stroke="black",
        stroke_width=1,
    )
    return c, b


# фосфориты
def phosphorites(d, x, y, width, height):
    # размер
    size = 1 / 10
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = 50 * size * koef
    delta_y = 18 * size * koef
    delta = 0.5
    i = 1
    # стартовые значения
    y_start = (y - height) * koef + 2 * delta_y
    while y_start > (y - height + 11 * size / 2) * koef:
        x_start = (x + delta + 28.4 * size / 2) * koef
        while x_start < (width + x) * koef:
            c, b = phosphorite(x_start, y_start, size)
            d.append(c)
            d.append(b)
            x_start += delta_x
        if i == 1:
            delta += delta_x / (2 * koef)
            i += 1
        else:
            delta -= delta_x / (2 * koef)
            i = 1
        y_start -= delta_y
