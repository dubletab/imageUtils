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

if (os.path.isdir(out_dir)):
    shutil.rmtree(out_dir)
os.mkdir(out_dir)
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        last_index = filename.rfind('.')
        output_file_name = f"{filename[0:last_index]}_{resolution}x{resolution}"
        img = Image.open(f'{source_dir}/{filename}')
        new_img = img.resize((resolution, resolution),
                             Image.Resampling.LANCZOS)
        try:
            dpi = img.info['dpi']
            new_img.save(f"{out_dir}/{output_file_name}.{ext}",
                         "JPEG",
                         dpi=dpi,
                         quality=50)
        except:
            new_img.save(f"{out_dir}/{output_file_name}.{ext}",
                         "JPEG",
                         quality=50)
