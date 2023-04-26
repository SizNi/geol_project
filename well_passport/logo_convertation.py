from PIL import Image
import qrcode


# меняем размер логотипа и пересохраняем
# создаем qr-код
def convertation_logo(path):
    img = Image.open(path)
    newimg = img.resize((166, 166))
    newimg.save("well_passport/results/tmplogo.png")
    img = qrcode.make("https://enhyp.ru/")
    img.save("well_passport/results/qr.png")
