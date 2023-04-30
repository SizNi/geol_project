from subprocess import Popen
import PIL.Image

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


def png_to_pdf():
    im = PIL.Image.open("well_passport/results/generated_cross.png")
    print(im.size)
    size = (210, 297)
    out = im.resize(size)
    out.save("well_passport/results/generated_cross_2.pdf", "PDF", quality=100)
    im.save("well_passport/results/generated_cross.pdf", "PDF", quality=100)



if __name__ == "__main__":
    sample_doc = "well_passport/results/generated_doc.docx"
    out_folder = "well_passport/results"
    # doc_to_pdf(sample_doc, out_folder)
    png_to_pdf()
