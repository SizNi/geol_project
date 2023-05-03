import os


def removing():
    os.remove("well_passport/results/tmplogo.png")
    os.remove("well_passport/results/qr.png")
    os.remove("well_passport/results/generated_cross.png")
    os.remove("well_passport/results/generated_cross.pdf")
    os.remove("well_passport/results/generated_doc.docx")
    os.remove("well_passport/results/generated_doc.pdf")
    os.remove("well_passport/results/gis.pdf")
    os.remove("well_passport/results/map.png")
    os.remove("well_passport/results/result_without_pages.pdf")
    # анализы пока не удаляем, непонятно что с их конвертацией
    # os.remove("well_passport/results/analyses.pdf")
