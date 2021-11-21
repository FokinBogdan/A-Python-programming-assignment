from PIL import Image
import numpy as np
import doctest


def get_average(arr, size_mosaic):
    """
    Возвращает среднее значение сумм цветов каждого пикселя на участве arr с шагом в mosaic_size
    Параметры:
    :param arr: участок
    :param size_mosaic: шаг серого
    :return: среднее значение цвета пикселей на участке
    doctest:
    >>> get_average([[[1, 2, 3]]], 1)
    2
    >>> get_average([[[1, 2, 3]] * 3] * 3, 3)
    2
    >>> get_average([[[0, 0, 0]]], 1)
    0

    Чтобы реализовать данные тесты, get_average принимает size_mosaic
    """
    return int(np.sum(arr) / 3 // (size_mosaic ** 2))


def draw_mosaic_pixel(color):
    """
    Рисует мозаику поверх старого изображения
    Параметры:
    :param color: среднее значение цвета пикселей этого участка
    doctest:
    Не смог реализовать тесты для данной функции
    """
    for a in range(i, i + mosaic_size):
        for b in range(j, j + mosaic_size):
            img_array[a][b] = [color, color, color]


print(doctest.testmod())

print('Введите название загружаемого изображения:')
input_image_name = input()

img = Image.open(input_image_name)
img_array = np.array(img)
width, height = img.size

print('Введите размер мозаики:')
mosaic_size = int(input())
print('Введите шаг серого:')
graduation = int(input())

# растягиваю или сжимаю изображение, чтобы оно соответсвовало целому числу пикселей мозайки
if width % mosaic_size != 0 or height % mosaic_size != 0:
    width = round(width / mosaic_size) * mosaic_size
    height = round(height / mosaic_size) * mosaic_size
    img_array = np.array(img.resize((width, height)))

for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        average = get_average(img_array[i:i + mosaic_size, j:j + mosaic_size], mosaic_size)
        draw_mosaic_pixel(int(average // graduation) * graduation)

print('Введите название выгружаемого изображения:')
output_image_name = input()

res = Image.fromarray(img_array)
res.save(output_image_name)
