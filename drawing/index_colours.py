# расчленение по цветам выполнено на основании общей геохронологической шкалы
# ВСЕГЕИ https://vsegei.ru/ru/info/stratigraphy/stratigraphic_scale/
# Четвертичные отложения - Девонские отложения (за исключением палеогена)
# переделать на словарь
colours = {
    "Q": "#fcf4d8",
    "J\u2083": "#daeef9",
    "J\u2082": "#b5d0ec",
    "J\u2081": "#b5c8e9",
    "J": "#b5d0ec",
    "N\u2082": "#f9f3d9",
    "N\u2081": "#f3edd3",
    "N": "#f3edd3",
    "K\u2082": "#f4f7dd",
    "K\u2081": "#d7f0c1",
    "K": "#d7f0c1",
    "T\u2083": "#f2daf1",
    "T\u2082": "#e5b9e5",
    "T\u2081": "#dbb6e8",
    "T": "#e5b9e5",
    "P\u2083": "#fce4c2",
    "P\u2082": "#fcdab4",
    "P\u2081": "#fcd7b2",
    "P": "#fcdab4",
    "C\u2083": "#d3cac1",
    "C\u2082": "#b0a29d",
    "C\u2081": "#9e9c9c",
    "C": "#b0a29d",
    "D\u2083": "#f7d6bb",
    "D\u2082": "#e4c0a4",
    "D\u2081": "#e4b8a4",
    "D": "#e4c0a4",
    "S\u2082": "#e9edc6",
    "S\u2081": "#d7d6b4",
    "O\u2083": "#ccf0e2",
    "O\u2082": "#c0edd4",
    "O\u2081": "#a5dbbf",
    "O": "#c0edd4",
    "Ꞓ\u2083": "#ccf0e2",
    "Ꞓ\u2082": "#c0edd4",
    "Ꞓ\u2081": "#a5dbbf",
}


# возврат заливки по индексу
def colour(index):
    if len(index) >= 2:
        index = index[0:2]
    for elem in colours:
        if elem in index:
            return colours[elem]
    return None


# конвертация в нижний регистр индекса
def convertation(index):
    if len(index) >= 2:
        if index[1].isdigit():
            if int(index[1]) == 1:
                text = f"{index[0]}\u2081{index[2:]}"
            elif int(index[1]) == 2:
                text = f"{index[0]}\u2082{index[2:]}"
            elif int(index[1]) == 3:
                text = f"{index[0]}\u2083{index[2:]}"
        if len(index) >= 4:
            if index[3].isdigit():
                if int(index[3]) == 1:
                    text = f"{text[0:2]}\u208B\u2081{text[4:]}"
                elif int(index[3]) == 2:
                    text = f"{text[0:2]}\u208B\u2082{text[4:]}"
                elif int(index[3]) == 3:
                    text = f"{text[0:2]}\u208B\u2083{text[4:]}"
        return text
    return index
