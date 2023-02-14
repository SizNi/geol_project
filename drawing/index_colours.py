# расчленение по цветам выполнено на основании общей геохронологической шкалы
# ВСЕГЕИ https://vsegei.ru/ru/info/stratigraphy/stratigraphic_scale/
# Четвертичные отложения - Девонские отложения (за исключением палеогена)
def colour(index):
    if 'Q' in index:
        return '#fcf4d8'
    elif index[:2] == 'N2' in index or index[:2] == 'N\u2082' in index:
        return '#f9f3d9'
    elif index[:2] == 'N1' in index or index[:2] == 'N\u2081' in index or index[:1] == 'N' in index:
        return '#f3edd3'
    elif index[:2] == 'K2' in index or index[:2] == 'K\u2082' in index:
        return '#f4f7dd'
    elif index[:2] == 'K1' in index or index[:2] == 'K\u2081' in index or index[:1] == 'K' in index:
        return '#d7f0c1'
    elif 'J3' in index or 'J\u2083' in index:
        return '#daeef9'
    elif 'J2' in index or 'J\u2082' in index:
        return '#b5d0ec'
    elif 'J1' in index or 'J\u2081' in index or 'J' in index:
        return '#b5c8e9'
    elif 'T3' in index or 'T\u2083' in index:
        return '#f2daf1'
    elif 'T2' in index or 'T\u2082' in index:
        return '#e5b9e5'
    elif 'T1' in index or 'T\u2081' in index or 'T' in index:
        return '#dbb6e8'
    elif index[:2] == 'P3' in index or index[:2] == 'P\u2083' in index:
        return '#fce4c2'
    elif index[:2] == 'P2' in index or index[:2] == 'P\u2082' in index:
        return '#fcdab4'
    elif index[:2] == 'P1' in index or index[:2] == 'P\u2081' in index or index[:1] == 'P' in index:
        return '#fcd7b2'
    elif 'C3' in index or 'C\u2083' in index:
        return '#d3cac1'
    elif 'C2' in index or 'C\u2082' in index:
        return '#b0a29d'
    elif 'C1' in index or 'C\u2081' in index or 'C' in index:
        return '#b0a29d'
    elif 'D3' in index or 'D\u2083' in index:
        return '#f7d6bb'
    elif 'D2' in index or 'D\u2082' in index:
        return '#e4c0a4'
    elif 'D1' in index or 'D\u2081' in index or 'D' in index:
        return '#e4b8a4'
    else:
        return 'none'