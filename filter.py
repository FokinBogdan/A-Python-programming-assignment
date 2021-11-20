from PIL import Image
import numpy as np


def get_average(arr):
    return int(np.sum(arr) / 3 // (mosaic_size ** 2))


def draw_mosaic_pixel(color):
    for a in range(i, i + mosaic_size):
        for b in range(j, j + mosaic_size):
            img_array[a][b] = [color, color, color]


print('Введите название загружаемого изображения:')
input_image_name = input()

img = Image.open(input_image_name)
img_array = np.array(img)
width, height = img.size

print('Введите размер мозаики:')
mosaic_size = int(input())
print('Введите шаг серого:')
graduation = int(input())

#растягиваю или сжимаю изображение, чтобы оно соответсвовало целому числу пикселей мозайки
if width % mosaic_size != 0 or height % mosaic_size != 0:
    width = round(width / mosaic_size) * mosaic_size
    height = round(height / mosaic_size) * mosaic_size
    img_array = np.array(img.resize((width, height)))


for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        average = get_average(img_array[i:i + mosaic_size, j:j + mosaic_size])
        draw_mosaic_pixel(int(average // graduation) * graduation)

print('Введите название выгружаемого изображения:')
output_image_name = input()

res = Image.fromarray(img_array)
res.save(output_image_name)
