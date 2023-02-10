import os
from PIL import Image

# Начальное значение файлов
counter = 0
# Исходная папка
source_dir = './test'
# Новая папка с преобразованными файлами
out_dir = './output'
# Расширение
ext = 'jpg'
# Качество изображения на выходе
qlt = 65
os.mkdir(out_dir)
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        img = Image.open(f'{source_dir}/{filename}')
        img.save(f"{out_dir}/{counter}.{ext}",
                 "JPEG",
                 optimize=True,
                 quality=qlt)
        counter += 1
