# from datetime import datetime
from docxtpl import DocxTemplate
import json


def filling_pass():
    doc = DocxTemplate("well_passport/fixtures/test_template.docx")
    with open("well_passport/fixtures/test_data.json") as json_file:
        data = json.load(json_file)
        context = {
            "col_labels": ["fruit", "vegetable", "stone", "thing"],
            "tbl_contents": [
                {"label": "yellow", "cols": ["banana", "capsicum", "pyrite", "taxi"]},
                {
                    "label": "red",
                    "cols": ["apple", "tomato", "cinnabar", "doubledecker"],
                },
                {"label": "green", "cols": ["guava", "cucumber", "aventurine", "card"]},
            ],
        }

    doc.render(context)
    context = data
    doc.save("well_passport/results/generated_test.docx")


filling_pass()
