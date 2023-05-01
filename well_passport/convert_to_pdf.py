from subprocess import Popen
import img2pdf

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


def img_to_pdf():
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open("well_passport/results/generated_cross.pdf", "wb") as f:
        f.write(
            img2pdf.convert(
                "well_passport/results/generated_cross.png", layout_fun=layout_fun
            )
        )


if __name__ == "__main__":
    sample_doc = "well_passport/results/generated_doc.docx"
    out_folder = "well_passport/results"
    # doc_to_pdf(sample_doc, out_folder)
    # png_to_pdf()
