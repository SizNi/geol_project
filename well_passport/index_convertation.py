# конвертация в нижний регистр индекса для документа .doc
def convertation_doc(index):
    text = index
    if len(index) >= 2:
        if index[1].isdigit():
            if int(index[1]) == 1:
                text = f"{index[0]}₁{index[2:]}"
            elif int(index[1]) == 2:
                text = f"{index[0]}₂{index[2:]}"
            elif int(index[1]) == 3:
                text = f"{index[0]}₃{index[2:]}"
        if len(index) >= 4:
            if index[3].isdigit():
                if int(index[3]) == 1:
                    text = f"{text[0:2]}₋₁{text[4:]}"
                elif int(index[3]) == 2:
                    text = f"{text[0:2]}₋₂{text[4:]}"
                elif int(index[3]) == 3:
                    text = f"{text[0:2]}₋₃{text[4:]}"
    text = text.replace("K1", "K₁").replace("P1", "P₁")
    return text
