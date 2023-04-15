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
    # сложение частей в единый адрес
    context["well_location"] = (
        context["region"] + ", " + context["district"] + " г.о., " + context["location"]
    )
    # преобразование отложений в нормальный текст для описания (сюда надо добавить прослои и вкрапления)
    for elem in data['layers']:
        data['layers'][elem]['sediments'] = ', '.join(map(str, data['layers'][elem]['sediments']))
    print(data['layers'])
    context["year_now"] = datetime.now().year
    context["layers"] = list(data["layers"].values())
    #print(context)
    #doc.render(context)
    doc.save("well_passport/results/generated_doc.docx")


filling_pass()
