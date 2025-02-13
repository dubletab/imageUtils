import os


def rename_files_in_directory(text, directory, count):
    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(directory):
        # Проверяем, является ли объект файлом
        if os.path.isfile(os.path.join(directory, filename)):
            # Убираем строку "привет" из названия файла
            new_filename = filename.replace(text, "")
            if count > 0:
                last_dot_index = new_filename.rfind(".")
                # Если точка найдена и перед ней есть хотя бы {COUNT} символов
                if last_dot_index != -1 and last_dot_index >= count:
                    # Удаляем {COUNT} символов перед последней точкой
                    new_filename = (
                        new_filename[: last_dot_index - count]
                        + new_filename[last_dot_index:]
                    )

            # Если название изменилось, переименовываем файл
            if new_filename != filename:
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                os.rename(old_file, new_file)
                print(f"Переименован: {filename} -> {new_filename}")


# Укажите путь к папке, в которой нужно переименовать файлы
directory_path = r"F:\test"
# Текст, который требуется убрать, если ничего, то поставить пустую строку ""
text = "test"
# Сколько символов перед последней точкой убрать
count_for_end_remove = 0
rename_files_in_directory(text, directory_path, count_for_end_remove)
