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
# из бд будет прихдить список
layers_data = {'layers': {
    1: {'id': 1, 'name': 'Q', 'thick': 45.0, 'sediments': 'Глина серая, желтая'},
    2: {'id': 2, 'name': 'J\u2083', 'thick': 10, 'sediments': 'Песок мелко-среднезернистый'},
    3: {'id': 3, 'name': 'J\u2083ox-c', 'thick': 15, 'sediments': 'Глина'},
    4: {'id': 4, 'name': 'C\u2083g-P\u2081a', 'thick': 25, 'sediments': 'Известняк'},
}
}
well_data = {'well_data': {
    'columns': {
        1: {'id': 1, 'D': 377, 'from': 0.0, 'till': 34.0, 'type': 'обсадная'},
        2: {'id': 2, 'D': 273, 'from': 0.0, 'till': 74.0, 'type': 'обсадная'},
        3: {'id': 3, 'D': 273, 'from': 59.0, 'till': 95.0, 'type': 'фильтровая', 'filter': {
            1: {'id': 1, 'from': 75.0, 'till': 79.0},
            2: {'id': 2, 'from': 85.0, 'till': 90.0},
        }}
    },
    'pump_type': 'ЭЦВ-6-10-110',
    'pump_depth': 55.0,
    'static_lvl': 32.0,
    'dynamic_lvl': 35.0,
    'well_depth': 95.0
}}


def main():
    d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)
    # Подложка
    r = draw.Rectangle(0, 0, 210*koef, 297*koef,
                       fill='white', stroke='black')
    d.append(r)
    # контур рисунка
    r = draw.Rectangle(10*koef, 7*koef, 198*koef, 275*koef,
                       fill='white', stroke='black')
    d.append(r)
    header(d)
    scale(d, 95)
    layers(d, 95, layers_data)
    well(d, well_data)
    d.savePng('example.png')


# выбор масштаба (размер секции и количество секций)
def scaling(well_depth):
    if well_depth <= 50:
        section = 5
    elif well_depth > 50 and well_depth <= 150:
        section = 10
    else:
        section = 20
    section_numbers = round((well_depth + (section/2))/section)
    return section, section_numbers

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
    # выбираем масштаб и количество делений
    section, section_numbers = scaling(well_depth)
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
    # смещение по x: (12, 12, 12, 30, 30, 45, 12, 45)
    # отрисовка прямоугольников под уровень и конструкцию скважины
    rectangle(d, 151, 257, 12, -well_depth*(mm_section/section), 'white', 'f')
    rectangle(d, 163, 257, 22.5, -well_depth *
              (mm_section/section), 'white', 'f')
    rectangle(d, 185.5, 257, 22.5, -well_depth *
              (mm_section/section), 'white', 'f')


# создание прямоугольника с текстом
def rectangle(d, x, y, x1, y1, text, direction):
    # f - заливать, h - с горизонтальным текстом, v - вертикальным
    # заготовка для добавления заливки
    if direction == 'f':
        r = draw.Rectangle(x*koef, y*koef, x1*koef, y1*koef,
                           fill=text, stroke='black')
    else:
        r = draw.Rectangle(x*koef, y*koef, x1*koef, y1*koef,
                           fill='white', stroke='black')
    d.append(r)
    # создание переноса строки если надо
    if direction != 'f' and (len(text) <= x1 / 2.1 or direction == 'v'):
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
def layers(d, well_depth, dt):
    # выбираем масштаб
    data = dt['layers']
    section, section_numbers = scaling(well_depth)
    # смещение по x: (12, 12, 12, 30, 30, 15, 15, 12, 22.5, 22.5)
    # деля 250 на округленную глубину скважины - получаем сколько в мм метров
    scale_m = (250/(section_numbers * section))
    # стартовые положения.
    h_start = 0.0  # глубина
    i = 1  # индекс в словаре (подумать как организовать передачу данных)
    y_start = (297 - 15 - 25)  # смещение по y после добавления заголовков
    while i in data:
        x_start = 10 + 12
        rectangle(d, x_start, y_start, 12, -
                  data[i]['thick']*scale_m, str(data[i]['id']), 'h')
        x_start += 12
        # ориентация для длинных индексов горизонтов
        if len(data[i]['name']) > 3:
            direction = 'v'
        else:
            direction = 'h'
        rectangle(d, x_start, y_start, 12, -
                  data[i]['thick']*scale_m, data[i]['name'], direction)
        x_start += 12
        rectangle(d, x_start, y_start, 30, -
                  data[i]['thick']*scale_m, data[i]['sediments'], 'h')
        x_start += 30
        rectangle(d, x_start, y_start, 30, -
                  data[i]['thick']*scale_m, 'blue', 'f')
        x_start += 30
        # подумать как убрать подписи вниз (к низу прямоугольника)
        rectangle(d, x_start, y_start, 15, -
                  data[i]['thick']*scale_m, str(h_start), 'h')
        x_start += 15
        h_start += data[i]['thick']
        rectangle(d, x_start, y_start, 15, -
                  data[i]['thick']*scale_m, str(h_start), 'h')
        x_start += 15
        rectangle(d, x_start, y_start, 15, -
                  data[i]['thick']*scale_m, str(data[i]['thick']), 'h')
        y_start -= data[i]['thick']*scale_m
        i += 1
        # завершение цикла отрисовки геологии


"""well_dto = {'well_data': {
    'columns': {
        1: {'id': 1, 'D': 377, 'from': 0.0, 'till': 34.0, 'type': 'обсадная'},
        2: {'id': 2, 'D': 273, 'from': 0.0, 'till': 74.0, 'type': 'обсадная'},
        3: {'id': 3, 'D': 273, 'from': 70.0, 'till': 95.0, 'type': 'фильтровая', 'filter': {
            1: {'id': 1, 'from': 75.0, 'till': 79.0},
            2: {'id': 2, 'from': 85.0, 'till': 90.0},
        }}
    },
    'pump_type': 'ЭЦВ-6-10-110',
    'pump_depth': 55.0,
    'static_lvl': 32.0,
    'dynamic_lvl': 35.0,
    'well_depth': 95.0
}}"""


def well(d, well_dt):
    data = well_dt['well_data']
    # масштаб
    section, section_numbers = scaling(data['well_depth'])
    scale_m = (250/(section_numbers * section))
    # стартовый диаметр внутренней колонны
    d_start = ((30/2)/(len(data['columns'])) + 2*len(data['columns']))
    i = 1
    while i in data['columns']:
        column = data['columns'][i]
        y_start = 257 - column['from']*scale_m
        x_start = 76 + (30-d_start)/2
        rectangle(d, x_start, y_start, d_start,
                  (column['from'] - column['till'])*scale_m, 'white', 'f')
        # добавление интервалов фильтра
        if column['type'] == 'фильтровая':
            filter = column['filter']
            i_f = 1
            while i_f in filter:
                rectangle(d, x_start, 257 - filter[i_f]['from']*scale_m, d_start,
                          (filter[i_f]['from'] - filter[i_f]['till'])*scale_m, 'red', 'f')
                i_f += 1
        d_start -= 2
        i += 1


if __name__ == "__main__":
    main()
