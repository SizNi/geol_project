from datetime import datetime
from docxtpl import DocxTemplate, InlineImage
import json
from filter_section import filter_sec
from index_convertation import convertation_doc
from date_convertation import convertation_date
from logo_convertation import convertation_logo
from convert_to_pdf import (
    doc_to_pdf,
    img_to_pdf,
    gis_to_pdf,
    pdf_merge,
    add_page_numbers,
)
from utility import removing
from map_convertation import get_map
from drawing.main import main as main_cross
from docx.shared import Mm
import os

# логотип и данные для qr и разреза
path = "well_passport/fixtures/logo.png"
qr_data = "https://enhyp.ru/"
path_cross = "well_passport/results/generated_cross.png"
map_path = "well_passport/results/map.png"


def filling_pass():
    # создаем то, что отправится в док
    context = {}
    doc = DocxTemplate("well_passport/fixtures/template_1.docx")
    with open("well_passport/fixtures/data.json") as json_file:
        data = json.load(json_file)
        context.update(data["main_data"])
    # логотип (если его нет - создаем) и qr
    if os.path.exists("well_passport/results/tmplogo.png") is False:
        convertation_logo(path)
    context["logo"] = InlineImage(
        doc, "well_passport/results/tmplogo.png", height=Mm(18)
    )
    context["qr"] = InlineImage(doc, "well_passport/results/qr.png", height=Mm(20))
    # добавляем карту и получаем координаты в ГСК 2011
    coordinates = [
        float(data["main_data"]["NL"]),
        float(data["main_data"]["SL"]),
    ]
    new_coordinates = get_map(coordinates, map_path)
    context["map"] = InlineImage(doc, map_path, width=Mm(199))
    # заменяем координаты в массиве
    data["main_data"]["NL"] = round(new_coordinates[0], 6)
    data["main_data"]["SL"] = round(new_coordinates[1], 6)
    # отправляем данные для разреза
    cross_data = {}
    cross_data["layers"] = data["layers"]
    cross_data["well_data"] = data["well_data"]
    main_cross(cross_data, path_cross)
    # преобразуем разрез в пдф формата А4
    img_to_pdf(
        "well_passport/results/generated_cross.pdf",
        "well_passport/results/generated_cross.png",
    )
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
        data["well_data"]["debit"]
        * 0.278
        / (data["well_data"]["dynamic_lvl"] - data["well_data"]["static_lvl"]),
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
    # словарь адресов приложений
    merge_dict = {}
    # добавляем результаты ГИС если они есть
    attouchment = 0
    pril = []
    if "GIS" in data:
        context["gis_date"] = data["GIS"]["date"]
        context["gis_designer"] = data["GIS"]["designer"]
        context["gis_type"] = data["GIS"]["type"]
        context["gis_results"] = data["GIS"]["results"]
        attouchment += 1
        context["gis_attouchment"] = attouchment
        # конвертим файл геофизики
        gis_to_pdf()
        pril.append({"id": attouchment, "name": "Результаты ГИС"})
        merge_dict[attouchment + 1] = "well_passport/results/gis.pdf"
    else:
        context["gis_date"] = False
    # заполняем ОФР
    if "OFR" in data:
        context["debit_1"] = round(
            data["well_data"]["debit"] * 0.278,
            2,
        )
        context["debit_2"] = round(
            data["well_data"]["debit"] * 24,
            1,
        )
        context["debit_3"] = round(
            data["well_data"]["debit"]
            / (data["well_data"]["dynamic_lvl"] - data["well_data"]["static_lvl"]),
            2,
        )
        context["debit_4"] = context["debit_3"] * 24
        context["ofr_reservoir"] = data["OFR"]["reservoir"]
        context["fill_time"] = round(data["OFR"]["reservoir"] / context["debit_1"], 1)
        context["ofr_equipment"] = data["OFR"]["equipment"]
        context["ofr_pump_type"] = data["well_data"]["pump_type"]
        context["ofr_pump_power"] = data["well_data"]["pump_power"]
        context["ofr_pump_depth"] = data["well_data"]["pump_depth"]
        context["ofr_pump_column"] = data["well_data"]["pump_column"]
        context["ofr_start_date"] = data["OFR"]["start_date"]
        context["ofr_end_date"] = data["OFR"]["end_date"]
        # расчет разницы в часах между началом и концом ОФР
        context["ofr_time"] = convertation_date(
            data["OFR"]["start_date"], data["OFR"]["end_date"]
        )
        context["ofr_designer"] = data["OFR"]["designer"]
    else:
        context["ofr_designer"] = False
    attouchment += 1
    context["cross_attouchment"] = attouchment
    pril.append({"id": attouchment, "name": "Геологический разрез скважины"})
    merge_dict[attouchment + 1] = "well_passport/results/generated_cross.pdf"
    # заполняем анализы если есть
    if "analyses" in data:
        context["analyses"] = data["analyses"]
        attouchment += 1
        context["analyses_attouchment"] = attouchment
        pril.append({"id": attouchment, "name": "Анализы подземных вод"})
        merge_dict[attouchment + 1] = "well_passport/results/analyses.pdf"
    else:
        context["analyses"] = False
    # список приложений для оглавления
    context["pril"] = pril
    context["current_date"] = datetime.now().date().strftime("%d.%m.%Y")
    doc.render(context)
    doc.save("well_passport/results/generated_doc.docx")
    # конвертируем в пдф (файл, папка с результатом)
    doc_to_pdf("well_passport/results/generated_doc.docx", "well_passport/results")
    merge_dict[1] = "well_passport/results/generated_doc.pdf"
    pdf_merge(merge_dict, "well_passport/results/result_without_pages.pdf")
    # добавляем номера страниц
    add_page_numbers(
        "well_passport/results/result_without_pages.pdf",
        "well_passport/results/result.pdf",
    )
    # удаляем лишнее
    removing()


filling_pass()
