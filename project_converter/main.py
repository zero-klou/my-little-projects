import sys
import os
from PIL import Image

from_dir = sys.argv[1]
to_dir = sys.argv[2]


def get_imgs_names(directory):
    images = filter(lambda x: x.endswith('jpg'), os.listdir(directory))
    return images


def get_imgs(images_names):
    converted_images = []

    for img_name in images_names:
        img = Image.open(f"{from_dir}/{img_name}")
        converted_images.append(img)

    return converted_images


def save_converted_imgs_to_dir(images, directory):
    i = 0
    for image in images:
        i += 1 #index of converted img in new dir
        image.save(f'{directory}/{i}img.png', 'png')


def main_function(*dirs):
    for directory in dirs:  # проверяем наличие папок и создаём, если нет
        if os.path.exists(directory):
            print(f'Папка {directory} обнаружена')
        else:
            print(f'Папка {directory} не найдена')
            # если нет главной папки с картинками, то прерываем программу
            if dirs.index(directory) != 0:
                if input('Чтобы создать папку введите любую букву; чтобы не создавать, оставьте поле пустым: '):
                    os.mkdir(directory, 755)
                else:
                    break
            else:
                break

    print('Произвожу конвертирование и добавляю в новую папку')

    imgs_names = get_imgs_names(from_dir)
    imgs = get_imgs(imgs_names)

    save_converted_imgs_to_dir(imgs, to_dir)

    print('Операция завершена!')


main_function(from_dir, to_dir)
