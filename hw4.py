#Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно упростит вам жизнь.

x_list = [2, 1, 4, 2, 12, 32, 12, 45]
y_list = [3, 2, 23, 45, 0, 54, 9, 14]

mid_x = sum(x_list) // len(x_list)
mid_y = sum(y_list) // len(y_list)

up = (sum(map(lambda x: x - mid_x, x_list))) * (sum(map(lambda y: y - mid_y, y_list)))

down = ((sum(map(lambda x: (x - mid_x) ** 2, x_list))) * (sum(map(lambda y: (y - mid_y) ** 2, y_list)))) ** 0.5

res = round(up / down, 3)
print(res)