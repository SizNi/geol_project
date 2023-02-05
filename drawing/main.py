import drawSvg as draw
import math

# размер листа А4 при плотности пикселей 300 dpi
width, height = 2480, 3508
# коэффициент пересчета мм -> % от общей ширины/высоты (2480/210 = 11,809 (1 мм в пикселях))
# 2480/100 = 24,8 пикселя в 1%, соответственно 1 мм = 11,809/24,8 = 0,4761% (по y)
# 3508/100 = 35,08 пикселя в 1%, соответственно 1 мм = 11,809/35,08 = 0,3366% (по x)
mm_x = 0.004761
mm_y = 0.003366
koef = 2480/210
line = 0.001


def main():
    d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)
    # Подложка
    r_0 = draw.Rectangle(0, 0, 210*koef, 297*koef,
                         fill='white', stroke='black')
    d.append(r_0)
    # d x1, y1, x2, y2
    # создание заголовка таблицы (надо немного поправить перенос строк, для таблицы
    # можно сделать его вручную)
    rectangle(d, 10, 297-15, 12, -25, 'Масштаб', 'v')
    rectangle(d, 22, 297-15, 12, -25, '№ слоя', 'v')
    rectangle(d, 34, 297-15, 12, -25, 'Возраст', 'v')
    rectangle(d, 46, 297-15, 30, -25, 'Описание пород', 'h')
    rectangle(d, 76, 297-15, 30, -25, 'Разрез скважины', 'h')
    rectangle(d, 106, 297-15, 45, -10, 'Залегание слоя, м', 'h')
    rectangle(d, 106, 297-25, 15, -15, 'От', 'h')
    rectangle(d, 121, 297-25, 15, -15, 'До', 'h')
    rectangle(d, 136, 297-25, 15, -15, 'Мощность', 'h')
    rectangle(d, 151, 297-15, 12, -25, 'Уровень, м', 'v')
    rectangle(d, 163, 297-15, 45, -10, 'Конструкция скважины', 'h')
    rectangle(d, 163, 297-25, 22.5, -15, 'Диаметр, мм', 'h')
    rectangle(d, 185.5, 297-25, 22.5, -15, 'Глубина, м', 'h')
    d.savePng('example.png')


def rectangle(d, x, y, x1, y1, text, direction):
    r = draw.Rectangle(x*koef, y*koef, x1*koef, y1*koef,
                       fill='white', stroke='black')
    d.append(r)
    # создание переноса строки если надо
    if len(text) <= x1 / 2.1 or direction == 'v':
        # расположение текста в завимости от ориентации текста
        if direction == 'v':
            p = draw.Lines((x+x1/2+1)*koef, (y+y1)*koef,
                           (x+x1/2+1)*koef, y*koef,
                           close=False,
                           stroke='black')
        else:
            p = draw.Lines((x)*koef, (y+y1/2-1)*koef,
                           (x+x1)*koef, (y+y1/2-1)*koef,
                           close=False,
                           stroke='white')
        d.append(draw.Text([text], 40, path=p, text_anchor='middle'))
    else:
        number_str = math.ceil(abs((len(text)*2.1)/y1))
        i = 0
        # шаг с которым будем смещать строки
        step = y1 / number_str
        text_start_step = 0
        text_step = round(len(text)/abs(number_str))
        # ввод строк внутрь квадрата
        # -1 нужен чтоб не было проблем выходом за пределы строки
        # из-за округления
        while i < number_str-1:
            p = draw.Lines((x)*koef, (y+step+1)*koef,
                           (x+x1)*koef, (y+step+1)*koef,
                           close=False,
                           stroke='white')
            d.append(
                draw.Text([text[text_start_step:text_step]], 40, path=p, text_anchor='middle'))
            y += step
            i += 1
            text_start_step = text_step
            text_step += text_step
        # добавление остатка строки
        p = draw.Lines((x)*koef, (y+step+1)*koef,
                       (x+x1)*koef, (y+step+1)*koef,
                       close=False,
                       stroke='white')
        d.append(draw.Text([text[text_start_step:]],
                 40, path=p, text_anchor='middle'))


if __name__ == "__main__":
    main()
