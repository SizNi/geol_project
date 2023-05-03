from subprocess import Popen
import img2pdf
import os
from PIL import Image
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

LIBRE_OFFICE = r"/usr/bin/libreoffice"


def doc_to_pdf(input_docx, out_folder):
    p = Popen(
        [
            LIBRE_OFFICE,
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            out_folder,
            input_docx,
        ]
    )
    print([LIBRE_OFFICE, "--convert-to", "pdf", input_docx])
    p.communicate()


def img_to_pdf(output, input):
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(output, "wb") as f:
        f.write(img2pdf.convert(input, layout_fun=layout_fun))


def bmp_to_png(output, input):
    img = Image.open(input)
    img.save(output, "png")


def pdf_merge(pdf_list, output):
    merger = PdfMerger()
    if type(pdf_list) == list:
        for elem in pdf_list:
            merger.append(open(elem, "rb"))
        with open(output, "wb") as result:
            merger.write(result)
    elif type(pdf_list) == dict:
        sorted_pdf = dict(sorted(pdf_list.items(), key=lambda x: x[0]))
        pdf_merge(list(sorted_pdf.values()), output)


# конвертируем гис в пдф
def gis_to_pdf():
    if os.path.exists("well_passport/fixtures/gis.doc"):
        doc_to_pdf("well_passport/fixtures/gis.doc", "well_passport/fixtures")
    elif os.path.exists("well_passport/fixtures/gis.docx"):
        doc_to_pdf("well_passport/fixtures/gis.docx", "well_passport/fixtures")
    elif os.path.exists("well_passport/fixtures/gis.png"):
        img_to_pdf("well_passport/fixtures/gis.png", "well_passport/fixtures/gis.pdf")
    elif os.path.exists("well_passport/fixtures/gis.jpg"):
        img_to_pdf("well_passport/fixtures/gis.jpg", "well_passport/fixtures/gis.pdf")
    if os.path.exists("well_passport/fixtures/gis_2.doc"):
        doc_to_pdf("well_passport/fixtures/gis_2.doc", "well_passport/fixtures")
    elif os.path.exists("well_passport/fixtures/gis_2.docx"):
        doc_to_pdf("well_passport/fixtures/gis_2.docx", "well_passport/fixtures")
    elif os.path.exists("well_passport/fixtures/gis_2.png"):
        img_to_pdf(
            "well_passport/fixtures/gis_2.png", "well_passport/fixtures/gis_2.pdf"
        )
    elif os.path.exists("well_passport/fixtures/gis_2.jpg"):
        img_to_pdf(
            "well_passport/fixtures/gis_2.jpg", "well_passport/fixtures/gis_2.pdf"
        )
    elif os.path.exists("well_passport/fixtures/gis_2.bmp"):
        bmp_to_png(
            "well_passport/fixtures/gis_2.png", "well_passport/fixtures/gis_2.bmp"
        )
        img_to_pdf(
            "well_passport/fixtures/gis_2.pdf", "well_passport/fixtures/gis_2.png"
        )
        os.remove("well_passport/fixtures/gis_2.png")
    if os.path.exists("well_passport/fixtures/gis_2.pdf") and os.path.exists(
        "well_passport/fixtures/gis.pdf"
    ):
        pdf_list = [
            "well_passport/fixtures/gis.pdf",
            "well_passport/fixtures/gis_2.pdf",
        ]
        pdf_merge(pdf_list, "well_passport/results/gis.pdf")
        os.remove("well_passport/fixtures/gis_2.pdf")
        os.remove("well_passport/fixtures/gis.pdf")


# блок добавления номеров страниц
def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.setFontSize(10)
        # координаты номера
        c.drawString((200) * mm, (290) * mm, str(i))
        c.showPage()
    c.save()


def add_page_numbers(pdf_path, newpath):
    tmp = "__tmp.pdf"

    writer = PdfWriter()
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        n = len(reader.pages)

        # новый пдф с номерами
        create_page_pdf(n, tmp)

        with open(tmp, "rb") as ftmp:
            number_pdf = PdfReader(ftmp)
            for p in range(n):
                page = reader.pages[p]
                number_layer = number_pdf.pages[p]
                page.merge_page(number_layer)
                writer.add_page(page)

            if len(writer.pages) > 0:
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)


if __name__ == "__main__":
    sample_doc = "well_passport/results/generated_doc.docx"
    out_folder = "well_passport/results"
    # add_page_numbers("well_passport/results/result.pdf", "well_passport/results/result_2.pdf")
    # doc_to_pdf(sample_doc, out_folder)
    # png_to_pdf()
    # gis_to_pdf()
    # img_to_pdf("well_passport/fixtures/gis_2.pdf", "well_passport/fixtures/gis_2.png")
