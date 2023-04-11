from datetime import datetime as dt
from docxtpl import DocxTemplate


def filling_pass():
    doc = DocxTemplate('fixtures/template.docx')
    context = {}
    doc.render(context)
    doc.save("results/generated_doc.docx")
    pass