import os
import shutil
from PIL import Image

# Исходная папка
source_dir = "./source"
# Новая папка с преобразованными файлами
out_dir = "./output"
# Расширение
ext = "jpg"
# Требуемое разрешение
res_height = 607
res_width = 1080

if os.path.isdir(out_dir):
    shutil.rmtree(out_dir)
os.mkdir(out_dir)

for root, dirs, files in os.walk(source_dir):
    for filename in files:
        last_index = filename.rfind(".")
        output_file_name = f"{filename[0:last_index]}_{res_width}x{res_height}"
        img = Image.open(f"{source_dir}/{filename}")
        height_percent = res_height / float(img.size[1])
        width_size = int((float(img.size[0]) * float(height_percent)))
        new_img = img.resize((width_size, res_height), Image.Resampling.LANCZOS)
        new_img_width = new_img.size[0]
        result_img = new_img
        if new_img_width > res_width:
            dif_width = new_img_width - res_width
            crop_x_left = 0
            crop_y_left = 0
            crop_x_right = res_width
            crop_y_right = res_height
            if dif_width % 2 == 1:
                delta = (dif_width - 1) / 2
                crop_x_left = delta + 1
                crop_x_right = new_img_width - delta
            else:
                delta = dif_width / 2
                crop_x_left = delta
                crop_x_right = new_img_width - delta
            result_img = new_img.crop(
                (crop_x_left, crop_y_left, crop_x_right, crop_y_right)
            )
        try:
            dpi = img.info["dpi"]
            result_img.save(
                f"{out_dir}/{output_file_name}.{ext}", "JPEG", dpi=dpi, quality=50
            )
        except:
            result_img.save(f"{out_dir}/{output_file_name}.{ext}", "JPEG", quality=50)
