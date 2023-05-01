import staticmaps
from PIL import Image, ImageDraw
from pyproj import Transformer


# получаем карту с расположением
def get_map(coordinates, path):
    width = 800
    height = 800
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)

    point = staticmaps.create_latlng(coordinates[0], coordinates[1])
    context.add_object(staticmaps.Marker(point, color=staticmaps.RED, size=8))
    img = context.render_cairo(width, height)
    img.write_to_png(path)
    img = Image.open(path)
    # убираем вотермарку осм
    cord = (0, 0, 800, 785)
    new_img = img.crop(cord)
    pencil = ImageDraw.Draw(new_img)
    pencil.rectangle((0, 0, 799, 784), outline="black")
    new_img.save(path)
    # переводим координаты из WGS84 в ГСК 2011
    # погрешность конвертации в сравнении с картой недропользования около 0.1-0.2 м
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:7683")
    return transformer.transform(coordinates[0], coordinates[1])


if __name__ == "__main__":
    path = "well_passport/results/point.png"
    coordinates = [55.5807, 37.7751]
    get_map(coordinates, path)
