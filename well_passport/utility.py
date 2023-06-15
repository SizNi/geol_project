import os


def removing():
    files_to_remove = [
        "well_passport/results/tmplogo.png",
        "well_passport/results/qr.png",
        # "well_passport/results/generated_cross.png",
        "well_passport/results/generated_cross.pdf",
        "well_passport/results/generated_doc.docx",
        "well_passport/results/generated_doc.pdf",
        "well_passport/results/gis.pdf",
        "well_passport/results/map.png",
        "well_passport/results/result_without_pages.pdf",
        # "well_passport/results/analyses.pdf"
    ]

    for file_path in files_to_remove:
        if os.path.exists(file_path):
            os.remove(file_path)
