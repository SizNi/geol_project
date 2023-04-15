from datetime import datetime
from docxtpl import DocxTemplate
import json
# from drawing.index_colours import convertation


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
    # преобразует все компоненты отложений в единую строку (отложения, прослои, вкрапления)
    # добавляем отложения
    bedding_depth = 0.0
    for elem in data["layers"]:
        res = ", ".join(
            map(str, data["layers"][elem]["sediments"])
        ).capitalize()
        # добавляем прослои
        if 'interlayers' in data["layers"][elem]:
            res += '. Прослои: ' + ", ".join(
            map(str, data["layers"][elem]["interlayers"])
        )
        # добавляем вкрапления
        if 'inclusions' in data["layers"][elem]:
            res += '. Вкрапления: ' + ", ".join(
            map(str, data["layers"][elem]["inclusions"])
        )
        data["layers"][elem]["sediments"] = res
        # преобразование мощности отложений во флоат
        data["layers"][elem]["thick"] = float(data["layers"][elem]["thick"])
        # добавление подошвы пласта
        bedding_depth += data["layers"][elem]["thick"]
        data["layers"][elem]["bedding_depth"] = bedding_depth
    # строение скважины (колонны, фильтра)
    columns = data['well_data']['columns']
    # заполняем табличку с обсадными колоннами
    obs = []
    for elem in columns:       
        if columns[elem]['type'] == 'обсадная':
            obs.append(columns[elem])
        else:
            context['philter'] = columns[elem]
            # сюда вставить разбор на части фильтровой колонны
    print(context['philter'])
    context['obs'] = obs
    context["year_now"] = datetime.now().year
    context["layers"] = list(data["layers"].values())
    #print(context)
    doc.render(context)
    doc.save("well_passport/results/generated_doc.docx")


filling_pass()
