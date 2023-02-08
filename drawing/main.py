import drawSvg as draw
import math

# размер листа А4 при плотности пикселей 300 dpi
width, height = 2480, 3508
# коэффициент пересчета мм -> % от общей ширины/высоты (2480/210 = 11,809 (1 мм в пикселях))
# 2480/100 = 24,8 пикселя в 1%, соответственно 1 мм = 11,809/24,8 = 0,4761% (по y)
# 3508/100 = 35,08 пикселя в 1%, соответственно 1 мм = 11,809/35,08 = 0,3366% (по x)
# общая высота рисунка (самой скважины) - 250 мм, названий столбцов - 25 мм
mm_x = 0.004761
mm_y = 0.003366
koef = 2480/210
# шаблон данных для слоев
data = {
    1:{'id': 1, 'name':'Q', 'thick': 45.0, 'sediments': 'Глина серая, желтая'},
    2:{'id': 2, 'name':'J3', 'thick': 10, 'sediments': 'Песок мелко-среднезернистый'},
    3:{'id': 3, 'name':'J3ox-c', 'thick': 15, 'sediments': 'Глина'},
    4:{'id': 4, 'name':'C3g-P1a', 'thick': 25, 'sediments': 'Известняк'},
    }

def main():
    d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)
    # Подложка
    r = draw.Rectangle(0, 0, 210*koef, 297*koef,
                       fill='white', stroke='black')
    d.append(r)
    header(d)
    scale(d, 95)
    layers(d, 95, data)
    d.savePng('example.png')


# Создание таблицы с наименованием столбцов
def header(d):
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


# риусет масштабную линейку слева
def scale(d, well_depth):
    # выбираем масштаб
    if well_depth <= 50:
        section = 5
    elif well_depth > 50 and well_depth <= 150:
        section = 10
    else:
        section = 20
    # количество делений шкалы (section/2 для округления в большую сторону)
    section_numbers = round((well_depth + (section/2))/section)
    # колчичество мм на секцию (вся шкала растягивается на 250 мм)
    mm_section = 250 / section_numbers
    y_start = (297 - 15 - 25 - mm_section)
    for number in range(section_numbers):
        # строим прямоугольник
        # rectangle(d, 10, 297-15, 12, -25, 'Масштаб', 'v')
        r = draw.Rectangle(10*koef, y_start*koef, 12*koef, mm_section*koef,
                           fill='white', stroke='black')
        d.append(r)
        # проводим линию для текста (совпадает с низом прямоугольника)
        p = draw.Lines((10)*koef, (y_start + 1)*koef,
                       (22)*koef, (y_start + 1)*koef,
                       close=False,
                       stroke='white')
        text = str((number+1)*section)
        d.append(draw.Text([text], 40, path=p, text_anchor='middle'))
        y_start -= mm_section


# создание прямоугольника с текстом
def rectangle(d, x, y, x1, y1, text, direction):
    # f - заливать, h - с горизонтальным текстом, v - вертикальным
    # заготовка для добавления заливки
    if direction == 'f':
        r = draw.Rectangle(x*koef, y*koef, x1*koef, y1*koef,
                        fill='blue', stroke='black')
    else:
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
    elif direction == 'h':
        number_str = math.ceil(abs((len(text)*2.1)/x1))
        i = 0
        # Первоначальное положение строки
        step = y1 / number_str
        text_start_step = 0
        text_step = round(len(text)/abs(number_str))
        # ввод строк внутрь квадрата
        # -1 нужен чтоб не было проблем с выходом за пределы итератора
        # из-за округления
        while i < number_str-1:
            p = draw.Lines((x)*koef, (y+step+1)*koef,
                           (x+x1)*koef, (y+step+1)*koef,
                           close=False,
                           stroke='white')
            insert = str(text[text_start_step:text_step]) + '-'
            d.append(
                draw.Text([insert], 40, path=p, text_anchor='middle'))
            # смещение относительно первоначальной строки
            y += -5
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

# создание слоя
def layers(d, well_depth, data):
    # выбираем масштаб
    if well_depth <= 50:
        section = 5
    elif well_depth > 50 and well_depth <= 150:
        section = 10
    else:
        section = 20
    # у нас на 250 мм на листе а4 растянута полная глубина скважин с округлением
    section_numbers = round((well_depth + (section/2))/section)
    # смещение по x: (12, 12, 12, 30, 30, 15, 15, 12, 22.5, 22.5)
    # деля 250 на округленную глубину скважины - получаем сколько в мм метров
    scale_m = (250/(section_numbers * section))
    # стартовые положения. Тут будет начало цикла
    h_start = 0.0
    x_start = 10 + 12
    y_start = (297 - 15 - 25 - data[1]['thick']*scale_m)
    rectangle(d, x_start, y_start, 12, data[1]['thick']*scale_m, str(data[1]['id']), 'h')
    x_start += 12
    rectangle(d, x_start, y_start, 12, data[1]['thick']*scale_m, data[1]['name'], 'h')
    x_start += 12
    rectangle(d, x_start, y_start, 30, data[1]['thick']*scale_m, data[1]['sediments'], 'h')
    x_start += 30
    rectangle(d, x_start, y_start, 30, data[1]['thick']*scale_m, 'Здесь будет ссылка на заливку', 'f')
    x_start += 30
    # подумать как убрать подписи вниз (к низу прямоугольника)
    rectangle(d, x_start, y_start, 15, data[1]['thick']*scale_m, str(h_start), 'h')
    x_start += 15
    h_start += data[1]['thick']
    rectangle(d, x_start, y_start, 15, data[1]['thick']*scale_m, str(h_start), 'h')
    x_start += 15
    rectangle(d, x_start, y_start, 15, data[1]['thick']*scale_m, str(data[1]['thick']), 'h')
    # завершение цикла отрисовки геологии







if __name__ == "__main__":
    main()
