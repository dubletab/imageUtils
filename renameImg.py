import os
import shutil
from PIL import Image

# Начальное значение файлов
counter = 0
# Исходная папка
source_dir = "./source"
# Новая папка с преобразованными файлами
out_dir = "./output"
# Расширение
ext = "jpg"
# Качество изображения на выходе
qlt = 70

# Если нужно конвертировать из PNG в JPG ставь True, если нет False
is_from_png_to_jpg = False

if os.path.isdir(out_dir):
    shutil.rmtree(out_dir)
os.mkdir(out_dir)
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        img = Image.open(f"{source_dir}/{filename}")
        if is_from_png_to_jpg:
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, img)
            result_img = bg
        else:
            result_img = img
        result_img.save(
            f"{out_dir}/{counter}.{ext}", "JPEG", optimize=True, quality=qlt
        )
        counter += 1
