# A-Python-programming-assignment

Изображение до: ![ball.jpg](ball.jpg)

Изображение после работы filter.py : ![new_ball.jpg](new_ball.jpg)

Изображение после работы old_filter.py: ![res.jpg](res.jpg)

Время выполнения filter.py: ![img.png](img.png)

Время выполнения old_filter: ![img_1.png](img_1.png)

Время выполнения filter.py больше чем old_filter.py, потому что при работе с filter.py мы вручную вводили "Название загружаемого изображения", "Размер мозаики", "Шаг серого" и "Название выгружаемого изображения", а это занимает время работы filter.py. Поэтому, время работы filter.py зависит от быстродействия пользователя: чем быстрее пользователь введёт входные данные, тем быстрее выполнится filter.py.

Время выполнения filter_with_filename.py: ![img_2.png](img_2.png)

Время выполнения filter_with_filename.py меньше чем filter.py, потому что данные инициализируются автоматически. Также filter_with_filename выполняется быстрее old_filter, так как filter_with_filename - это усовершенствованный old_filter, и old_filter работает некорректно.

Скриншот выполненных doc-тестов: ![img_3.png](img_3.png)
Смог реализовать doc-тесты только для функции "get_average", которая возвращает среднее значение сумм цветов каждого пикселя на участве arr с шагом в mosaic_size.
Для функции "draw_mosaic_pixel" doc-тесты не реализовал.