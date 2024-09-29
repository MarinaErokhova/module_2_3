my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] #задаем список
print(my_list) #вывод списка в консоль
i = 0 #начальное значение индекса
while i < len(my_list):
    number = my_list [i] #число из списка
    i += 1 #увеличить значение переменной на 1
    if number == 0:
        continue
    elif number < 0:
        break
    else:
        print(number)
