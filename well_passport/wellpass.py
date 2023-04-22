from datetime import datetime
from docxtpl import DocxTemplate
import json
from filter_section import filter_sec
from index_convertation import convertation_doc


def filling_pass():
    # создаем то, что отправится в док
    context = {}
    doc = DocxTemplate("well_passport/fixtures/template_1.docx")
    with open("well_passport/fixtures/data.json") as json_file:
        data = json.load(json_file)
        context.update(data["main_data"])
    # сложение частей расположения в единый адрес
    context["well_location"] = (
        context["region"] + ", " + context["district"] + " г.о., " + context["location"]
    )
    # строение скважины (колонны, фильтра)
    columns = data["well_data"]["columns"]
    # заполняем табличку с обсадными колоннами
    obs = []
    for elem in columns:
        if columns[elem]["type"] == "обсадная":
            obs.append(columns[elem])
        else:
            context["filter"] = columns[elem]
            # вызов функции, разбирающей фильтровые части
            context["filter_parts"] = filter_sec(columns[elem])
    context["obs"] = obs
    # добавляем цементацию
    context["cementation"] = data["well_data"]["cementation"]
    context["year_now"] = datetime.now().year
    context["layers"] = list(data["layers"].values())
    # преобразование индексов в нижний регистр
    elem_depth = 0
    for elem in context["layers"]:
        elem["name"] = convertation_doc(elem["name"])
        # определяем основной горизонт
        if "main" in elem:
            context["main_aquifer"] = elem["name"]
            # добавляем отложения основного горизонта
            # print(elem["sediments"])
            context["main_aquifer_sediments"] = ", ".join(map(str, elem["sediments"]))
            context["ma_from"] = elem_depth
            context["ma_till"] = elem_depth + elem["thick"]
        # получаем кровлю следующего горизонта
        elem_depth += elem["thick"]
    # преобразует все компоненты отложений в единую строку (отложения, прослои, вкрапления)
    # добавляем отложения
    bedding_depth = 0.0
    for elem in data["layers"]:
        res = ", ".join(map(str, data["layers"][elem]["sediments"])).capitalize()
        # добавляем прослои
        if "interlayers" in data["layers"][elem]:
            res += ". Прослои: " + ", ".join(
                map(str, data["layers"][elem]["interlayers"])
            )
        # добавляем вкрапления
        if "inclusions" in data["layers"][elem]:
            res += ". Вкрапления: " + ", ".join(
                map(str, data["layers"][elem]["inclusions"])
            )
        data["layers"][elem]["sediments"] = res
        # преобразование мощности отложений во флоат
        data["layers"][elem]["thick"] = float(data["layers"][elem]["thick"])
        # добавление подошвы пласта
        bedding_depth += data["layers"][elem]["thick"]
        data["layers"][elem]["bedding_depth"] = bedding_depth
    context["well_depth"] = data["well_data"]["well_depth"]
    # добавление фильтровых интервалов в таблицу
    # по хорошоему надо будет переделать вместе с исходным форматом,
    # получилось дублирование данных
    obs = []
    dt = context["filter"]["filter"]
    filter_length = 0
    for elem in dt:
        obs.append(dt[elem])
        filter_length += dt[elem]["till"] - dt[elem]["from"]
    context["filter_length"] = filter_length
    context["filter_table"] = obs
    context["static_lvl"] = data["well_data"]["static_lvl"]
    context["static_lvl"] = data["well_data"]["static_lvl"]
    context["debit"] = data["well_data"]["debit"]
    context["ud_debit"] = round(
        (data["well_data"]["dynamic_lvl"] - data["well_data"]["static_lvl"])
        * 0.278
        / data["well_data"]["debit"],
        2,
    )
    context["lowering"] = round(
        data["well_data"]["dynamic_lvl"] - data["well_data"]["static_lvl"], 2
    )
    # добавление информации по ЗСО если она есть
    if "ZSO" in data:
        context["r1"] = data["ZSO"]["r1"]
        context["r2"] = data["ZSO"]["r2"]
        context["r3"] = data["ZSO"]["r3"]
        context["zso_designer"] = data["ZSO"]["designer"]
    else:
        context["r1"] = False
    # добавляем результаты ГИС если они есть
    if "GIS" in data:
        context["gis_date"] = data["GIS"]["date"]
        context["gis_designer"] = data["GIS"]["designer"]
        context["gis_type"] = data["GIS"]["type"]
        context["gis_results"] = data["GIS"]["results"]  
    else:
        context["gis_date"] = False
    doc.render(context)
    doc.save("well_passport/results/generated_doc.docx")


filling_pass()
