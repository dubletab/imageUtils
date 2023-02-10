import os
import shutil
from PIL import Image

# Исходная папка
source_dir = './source'
# Новая папка с преобразованными файлами
out_dir = './output'
# Расширение
ext = 'jpg'
# Требуемое разрешение
resolution = 600

shutil.rmtree(out_dir)
os.mkdir(out_dir)
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        last_index = filename.rfind('.')
        output_file_name = f"{filename[0:last_index]}_{resolution}x{resolution}.{ext}"
        img = Image.open(f'{source_dir}/{filename}')
        img.thumbnail(size=(resolution, resolution))
        img.save(f"{out_dir}/{output_file_name}.{ext}", "JPEG")
