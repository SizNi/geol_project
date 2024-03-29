import math
import drawSvg as draw
from drawing.format import frmt

# отрисовка геологических крапов
# ГОСТ Р 21.302-2021
_, _, koef = frmt("a4")


# типы отложений в possible_settings.txt
def speck(d, x, y, width, height, sediments, interlayers):
    height = height / len(sediments)
    # если есть прослои:
    if interlayers:
        # толщина прослоя в %
        one_interlayer = 0.15
        # какую часть слоя (в %) отдадим на прослои
        interlayers_part = one_interlayer * len(interlayers)
        for elem in sediments:
            choose_speck(d, x, y, width, height * (1 - interlayers_part), elem)
            interlayer_step = height * (1 - interlayers_part)
            for elem in interlayers:
                choose_speck(
                    d, x, y - interlayer_step, width, height * one_interlayer, elem
                )
                interlayer_step += one_interlayer * height
            y -= height
    else:
        for elem in sediments:
            choose_speck(d, x, y, width, height, elem)
            y -= height


# отдельно вынес выбор крапа
def choose_speck(d, x, y, width, height, elem):
    speck_functions = {
        "пески": sands,
        "глины": clays,
        "известняки": limestones,
        "суглинки": loams,
        "мергели": marls,
        "супеси": sandy_loams,
        "песчаники": sandstones,
        "доломиты": dolomites,
        "мел": chalk,
        "гнейсы": gneisses,
        "граниты": granites,
    }
    if elem.startswith("пески"):
        speck_type = elem.split(" ")[-1] if len(elem) > 6 else "средние"
        speck_functions["пески"](d, x, y, width, height, speck_type)
    elif elem in speck_functions:
        speck_functions[elem](d, x, y, width, height)
    else:
        raise ValueError("Что-то пошло не так. Возможно таких отложений нет")


# задание параметров масштаба для блочных крапов
def scaling(type):
    if type == "stones":
        # смещение по y
        delta_y = 2 * koef
        # смещение по x
        delta_x = 4 * delta_y
        # смещение от строки к строке
        delta = 0
        # начальный отступ
        indent = 0.3
        return delta_x, delta_y, delta, indent
    elif type == "sands":
        delta_x = 3 * koef
        delta_y = 2 * koef
        delta = 0
        indent = 0.6
        return delta_x, delta_y, delta, indent
    # граниты, гнейсы
    elif type == "rocks":
        size = 1.2
        indent = 0.6
        delta = 0
        return size, indent, delta
    # мел
    elif type == "chalk":
        delta = 3 / 2 * koef
        return delta


# пески
def sands(d, x, y, width, height, type):
    # выбор типа песков
    if type == "крупные":
        size = 0.2
    if type == "средние":
        size = 0.15
    if type == "мелкие":
        size = 0.1
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x, delta_y, delta, indent = scaling("sands")
    delta_x = delta_x * (size * 5)
    delta_y = delta_y * (size * 5)
    i = 1
    # стартовые значения
    y_start = (y - indent) * koef
    while y_start > (y - height) * koef:
        x_start = (x + delta + indent) * koef
        while x_start < (width + x) * koef:
            c = draw.Circle(x_start, y_start, size * koef, fill="black")
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
    delta_y = 1 * koef
    indent = 0.1
    y_start = (y - indent) * koef
    while y_start > (y - height + indent) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        y_start -= delta_y


# известняки
def limestones(d, x, y, width, height):
    # начальные значения
    delta_x, delta_y, delta, indent = scaling("stones")
    i = 0
    # стартовые значения
    y_start = y * koef
    x_start = (x + indent) * koef
    while y_start > (y - height) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        while x_start < (width + x - indent) * koef:
            # следующий цикл нужен, чтоб обрезать вертикальные линии,
            # которые могут вылезти за пределы слоя
            if (i + 1) * delta_y <= height * koef:
                c = draw.Lines(
                    x_start, y_start, x_start, y_start - delta_y, stroke="black"
                )
                d.append(c)
                x_start += delta_x
            else:
                # x2 - как раз смещение минус разница, вылезающая за пределы
                c = draw.Lines(
                    x_start,
                    y_start,
                    x_start,
                    y_start - delta_y + ((i + 1) * delta_y - height * koef),
                    stroke="black",
                )
                d.append(c)
                x_start += delta_x
        i += 1
        # смещение начальной точки
        if i % 2 == 0:
            delta -= delta_x / 2
        else:
            delta += delta_x / 2
        # обнуление начальной точки + смещение
        x_start = (x + indent) * koef + delta
        y_start -= delta_y


# суглинки
def loams(d, x, y, width, height):
    delta_y = 5 * koef
    # угол наклона
    alpha = 30
    tg_30 = math.tan((math.pi / 180) * alpha)
    delta_x = tg_30 * delta_y
    y_start = y * koef
    x_start = x * koef
    # отрисовываем с левого угла
    # движемся по левой грани вниз, по верхней грани вправо
    while y_start >= (y - height) * koef + delta_y and x_start <= (x + width) * koef:
        c = draw.Lines(
            x * koef,
            y_start - delta_y,
            x_start + delta_x,
            y * koef,
            stroke="black",
        )
        d.append(c)
        y_start -= delta_y
        x_start += delta_x
    # в зависимости от высоты и ширины получается два варианта:
    if width >= height:  # ширина больше высоты
        # переназначаем начальные значения
        x_low_start = ((y - height) * koef - y_start) * tg_30 + delta_x
        # движемся по верхней грани вправо, по нижней грани - тоже вправо
        while (
            x_start <= (x + width) * koef - delta_x
            and x * koef + x_low_start <= (x + width) * koef
        ):
            c = draw.Lines(
                x * koef + x_low_start,
                (y - height) * koef,
                x_start + delta_x,
                y * koef,
                stroke="black",
            )
            d.append(c)
            x_low_start += delta_x
            x_start += delta_x
        y_right_start = (
            delta_y - (delta_x - (x_start + delta_x - (x + width) * koef)) / tg_30
        )
    else:  # высота больше ширины
        y_right_start = (
            delta_y - (delta_x - (x_start + delta_x - (x + width) * koef)) / tg_30
        )
        while y_start >= (y - height) * koef + delta_y:
            c = draw.Lines(
                x * koef,
                y_start - delta_y,
                (x + width) * koef,
                y * koef - y_right_start,
                stroke="black",
            )
            d.append(c)
            y_start -= delta_y
            y_right_start += delta_y
        x_low_start = ((y - height) * koef - y_start) * tg_30 + delta_x
    # движемя по правой грани вниз, по нижней грани - вправо
    while (
        y * koef - y_right_start >= (y - height) * koef
        and x * koef + x_low_start <= (x + width) * koef
        and x * koef + x_low_start >= x * koef
    ):
        c = draw.Lines(
            x * koef + x_low_start,
            (y - height) * koef,
            (x + width) * koef,
            y * koef - y_right_start,
            stroke="black",
        )
        d.append(c)
        y_right_start += delta_y
        x_low_start += delta_x


# мергели
def marls(d, x, y, width, height):
    delta_x, delta_y, delta, indent = scaling("stones")
    i = 0
    indent = 1
    # стартовые значения
    y_start = y * koef
    x_start = (x + indent) * koef
    while y_start > (y - height) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        while x_start < (width + x) * koef:
            # следующий цикл нужен, чтоб обрезать вертикальные линии,
            # которые могут вылезти за пределы слоя
            if (i + 1) * delta_y <= height * koef:
                c = draw.Lines(
                    x_start + 1 * koef,
                    y_start,
                    x_start - 1 * koef,
                    y_start - delta_y,
                    stroke="black",
                )
                d.append(c)
                x_start += delta_x
            else:
                # остаток от delta_y
                y_min = delta_y - ((i + 1) * delta_y - height * koef)
                # поправка смещения (вместо +1 и -1)
                new_d = (delta_y - y_min) * (2 * koef / delta_y)
                # y2 - как раз смещение минус разница, вылезающая за пределы
                c = draw.Lines(
                    x_start + 1 * koef,
                    y_start,
                    x_start - 1 * koef + new_d,
                    y_start - y_min,
                    stroke="black",
                )
                d.append(c)
                x_start += delta_x
        i += 1
        # смещение начальной точки
        if i % 2 == 0:
            delta -= delta_x / 2
        else:
            delta += delta_x / 2
        # обнуление начальной точки + смещение
        x_start = (x + indent) * koef + delta
        y_start -= delta_y


# супеси
def sandy_loams(d, x, y, width, height):
    # параметры штриховки
    line_black = 24
    line_white = line_black / 3
    delta_y = 5 * koef
    # угол наклона
    alpha = 30
    tg_30 = math.tan((math.pi / 180) * alpha)
    delta_x = tg_30 * delta_y
    y_start = y * koef
    x_start = x * koef
    # отрисовываем с левого угла
    # движемся по левой грани вниз, по верхней грани вправо
    while y_start >= (y - height) * koef + delta_y and x_start <= (x + width) * koef:
        c = draw.Lines(
            x * koef,
            y_start - delta_y,
            x_start + delta_x,
            y * koef,
            stroke="black",
            stroke_dasharray=f"{line_black}, {line_white}",
        )
        d.append(c)
        y_start -= delta_y
        x_start += delta_x
    # в зависимости от высоты и ширины получается два варианта:
    if width >= height:  # ширина больше высоты
        # переназначаем начальные значения
        x_low_start = ((y - height) * koef - y_start) * tg_30 + delta_x
        # движемся по верхней грани вправо, по нижней грани - тоже вправо
        while (
            x_start <= (x + width) * koef - delta_x
            and x * koef + x_low_start <= (x + width) * koef
        ):
            c = draw.Lines(
                x * koef + x_low_start,
                (y - height) * koef,
                x_start + delta_x,
                y * koef,
                stroke="black",
                stroke_dasharray=f"{line_black}, {line_white}",
            )
            d.append(c)
            x_low_start += delta_x
            x_start += delta_x
        y_right_start = (
            delta_y - (delta_x - (x_start + delta_x - (x + width) * koef)) / tg_30
        )
    else:  # высота больше ширины
        y_right_start = (
            delta_y - (delta_x - (x_start + delta_x - (x + width) * koef)) / tg_30
        )
        while y_start >= (y - height) * koef + delta_y:
            c = draw.Lines(
                x * koef,
                y_start - delta_y,
                (x + width) * koef,
                y * koef - y_right_start,
                stroke="black",
                stroke_dasharray=f"{line_black}, {line_white}",
            )
            d.append(c)
            y_start -= delta_y
            y_right_start += delta_y
        x_low_start = ((y - height) * koef - y_start) * tg_30 + delta_x
    # движемя по правой грани вниз, по нижней грани - вправо
    while (
        y * koef - y_right_start >= (y - height) * koef
        and x * koef + x_low_start <= (x + width) * koef
        and x * koef + x_low_start >= x * koef
    ):
        c = draw.Lines(
            x * koef + x_low_start,
            (y - height) * koef,
            (x + width) * koef,
            y * koef - y_right_start,
            stroke="black",
            stroke_dasharray=f"{line_black}, {line_white}",
        )
        d.append(c)
        y_right_start += delta_y
        x_low_start += delta_x


# песчаники
def sandstones(d, x, y, width, height):
    delta_x, delta_y, delta, indent = scaling("stones")
    # шаг между точками внутри крапа
    step = delta_x / 5
    i = 0
    # стартовые значения
    y_start = y * koef
    x_start = (x + indent) * koef
    while y_start > (y - height) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        if delta != 0:
            c = draw.Circle(
                x_start - step, y_start - delta_y / 2, 0.2 * koef, fill="black"
            )
            d.append(c)
            c = draw.Circle(
                x_start - step * 2, y_start - delta_y / 2, 0.2 * koef, fill="black"
            )
            d.append(c)
        while x_start < (width + x - indent) * koef:
            if (i + 1) * delta_y <= height * koef:
                c = draw.Lines(
                    x_start - 0.5 * koef,
                    y_start,
                    x_start + 0.5 * koef,
                    y_start - delta_y,
                    stroke="black",
                )
                d.append(c)
                c = draw.Lines(
                    x_start + 0.5 * koef,
                    y_start,
                    x_start - 0.5 * koef,
                    y_start - delta_y,
                    stroke="black",
                )
                d.append(c)
                # отрисовка точек
                for n in range(1, 5):
                    c = draw.Circle(
                        x_start + step * n,
                        y_start - delta_y / 2,
                        0.2 * koef,
                        fill="black",
                    )
                    d.append(c)
                x_start += delta_x
            # следующий цикл нужен, чтоб обрезать вертикальные линии,
            # которые могут вылезти за пределы слоя
            else:
                # остаток от delta_y
                y_min = delta_y - ((i + 1) * delta_y - height * koef)
                # поправка смещения (вместо +1 и -1)
                new_d = (delta_y - y_min) * (1 * koef / delta_y)
                # y2 - как раз смещение минус разница, вылезающая за пределы
                c = draw.Lines(
                    x_start - 0.5 * koef,
                    y_start,
                    x_start + 0.5 * koef - new_d,
                    y_start - y_min,
                    stroke="black",
                )
                d.append(c)
                c = draw.Lines(
                    x_start + 0.5 * koef,
                    y_start,
                    x_start - 0.5 * koef + new_d,
                    y_start - y_min,
                    stroke="black",
                )
                d.append(c)
                if delta_y / 2 < y_min:
                    for n in range(1, 5):
                        c = draw.Circle(
                            x_start + step * n,
                            y_start - delta_y / 2,
                            0.2 * koef,
                            fill="black",
                        )
                        d.append(c)
                x_start += delta_x
        i += 1
        # смещение начальной точки
        if i % 2 == 0:
            delta -= delta_x / 2
        else:
            delta += delta_x / 2
        # обнуление начальной точки + смещение
        x_start = (x + indent) * koef + delta
        y_start -= delta_y


# доломиты
def dolomites(d, x, y, width, height):
    delta_x, delta_y, delta, indent = scaling("stones")
    indent = 0.6
    # расстояние между палками для крапа
    between = 0.3 * koef
    i = 0
    # стартовые значения
    y_start = y * koef
    x_start = (x + indent) * koef
    while y_start > (y - height) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        while x_start < (width + x - indent) * koef:
            # следующий цикл нужен, чтоб обрезать вертикальные линии,
            # которые могут вылезти за пределы слоя
            if (i + 1) * delta_y <= height * koef:
                c = draw.Lines(
                    x_start + between,
                    y_start,
                    x_start + between,
                    y_start - delta_y,
                    stroke="black",
                )
                d.append(c)
                c = draw.Lines(
                    x_start - between,
                    y_start,
                    x_start - between,
                    y_start - delta_y,
                    stroke="black",
                )
                d.append(c)
                x_start += delta_x
            else:
                # x2 - как раз смещение минус разница, вылезающая за пределы
                c = draw.Lines(
                    x_start + between,
                    y_start,
                    x_start + between,
                    y_start - delta_y + ((i + 1) * delta_y - height * koef),
                    stroke="black",
                )
                d.append(c)
                c = draw.Lines(
                    x_start - between,
                    y_start,
                    x_start - between,
                    y_start - delta_y + ((i + 1) * delta_y - height * koef),
                    stroke="black",
                )
                d.append(c)
                x_start += delta_x
        i += 1
        # смещение начальной точки
        if i % 2 == 0:
            delta -= delta_x / 2
        else:
            delta += delta_x / 2
        # обнуление начальной точки + смещение
        x_start = (x + indent) * koef + delta
        y_start -= delta_y


# мел
def chalk(d, x, y, width, height):
    # смещение по горизонтали и вертикали (для мела одинаковое)
    delta = scaling("chalk")
    # стартовые значения
    y_start = y * koef - delta
    x_start = x * koef + delta
    # горизонтальная штриховка
    while y_start > (y - height) * koef:
        c = draw.Lines(x * koef, y_start, (x + width) * koef, y_start, stroke="black")
        d.append(c)
        y_start -= delta
    # вертикальная штриховка
    while x_start < (x + width) * koef:
        c = draw.Lines(x_start, y * koef, x_start, (y - height) * koef, stroke="black")
        d.append(c)
        x_start += delta


# единичный крап гнейсов
def gneisses_speck(d, x, y, size_1):
    size_2 = (6 / 14) * size_1
    c = draw.Lines(x, y, x + size_1 * koef, y, stroke="black")
    d.append(c)
    x += size_1 * koef
    c = draw.Lines(x, y, x + size_2 * koef, y - size_2 * koef, stroke="black")
    d.append(c)
    x += size_2 * koef
    y -= size_2 * koef
    c = draw.Lines(x, y, x + size_2 * koef, y + size_2 * koef, stroke="black")
    d.append(c)
    x += size_2 * koef
    y += size_2 * koef
    c = draw.Lines(x, y, x + size_1 * koef, y, stroke="black")
    d.append(c)


# гнейсы
def gneisses(d, x, y, width, height):
    # масштаб размера
    size, indent, delta = scaling("rocks")
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = (40 / 14) * size * koef + (12 / 14) * size * koef
    delta_y = 2 * koef
    i = 1
    # стартовые значения
    y_start = (y - indent) * koef
    while y_start > (y - height + indent) * koef:
        x_start = (x + delta) * koef
        if i % 2 != 1:
            c = draw.Lines(
                x_start - 12 / 14 * size * koef,
                y_start,
                x_start - size * koef - 12 / 14 * size * koef,
                y_start,
                stroke="black",
            )
            d.append(c)
        while x_start < (width + x) * koef:
            gneisses_speck(d, x_start, y_start, size)
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= (delta_x / 2) / koef
        else:
            delta += (delta_x / 2) / koef

        y_start -= delta_y


# единичный крап гранитов


def granites_speck(d, x, y, size_1, st_width):
    c = draw.Lines(
        x,
        y,
        x + size_1 * koef,
        y,
        stroke="black",
        stroke_width=f"{st_width}",
    )
    d.append(c)
    c = draw.Lines(
        x + size_1 * koef / 2,
        y + size_1 * koef / 2,
        x + size_1 * koef / 2,
        y - size_1 * koef / 2,
        stroke="black",
        stroke_width=f"{st_width}",
    )
    d.append(c)


# граниты
def granites(d, x, y, width, height):
    # масштаб размера
    size, indent, delta = scaling("rocks")
    # смещение по горизонтали, вертикали, изменение смещения по горизонтали
    delta_x = (size + 1.6 * size) * koef
    delta_y = 1.2 * size * koef
    i = 1
    # стартовые значения
    st_width = 3
    y_start = (y - 2 * indent + 0.1) * koef
    while y_start > (y - height + indent) * koef:
        x_start = (x + delta) * koef
        while x_start < (width + x) * koef:
            granites_speck(d, x_start, y_start, size, st_width)
            x_start += delta_x
        i += 1
        if i % 2 == 1:
            delta -= (delta_x / 2) / koef
            st_width += 2
        else:
            delta += (delta_x / 2) / koef
            st_width -= 2
        y_start -= delta_y
