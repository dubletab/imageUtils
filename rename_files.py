import os


def rename_files_in_directory(text, directory):
    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(directory):
        # Проверяем, является ли объект файлом
        if os.path.isfile(os.path.join(directory, filename)):
            # Убираем строку "привет" из названия файла
            new_filename = filename.replace(text, "")

            # Если название изменилось, переименовываем файл
            if new_filename != filename:
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                os.rename(old_file, new_file)
                print(f"Переименован: {filename} -> {new_filename}")


# Укажите путь к папке, в которой нужно переименовать файлы
directory_path = r"F:\test"
# Текст, который требуется убрать
text = "sss"
rename_files_in_directory(text, directory_path)
