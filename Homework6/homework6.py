from random import randint
from time import sleep

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def progression(first_element, difference, element_count):
#   my_list = []
#   for i in range(1, element_count + 1):
#     my_list.append(first_element + (i-1) * difference)
  
#   return(my_list)
# print("First list ",progression(10, 5, 10))

print("****************************************************************")
print("Задача 30: Данная программа на вход принимает размер, первый элемент и разность (шаг) арифметической прогрессии, а затем выводит список, заполненный элементами арифметической прогрессии.")
size = int(input('Введите количество элементов прогрессии: '))
first_element = int(input('Введите первый элемент прогрессии: '))
difference = int(input('Введите разность (шаг) прогрессии: '))
print()
print('Список элементов арифметической прогрессии:')
sleep(2)
print(my_list := list([(first_element + (i-1) * difference) for i in range(1, size + 1)]))
print()
sleep(1)
print("Загрузка следующей задачи...")
print()
sleep(3)




# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_index(func_list, start, end):
  indexes = []
  for i in range(len(func_list)):
    if func_list[i] in range(start, end + 1):
      indexes.append(i)
  return indexes

print("****************************************************************")
print("Задача 32: Данная программа принимает на вход список элементов и диапазон, а затем выводит список индексов элементов заданного списка, значения которых принадлежат заданному диапазону")
new_size = int(input('Введите размер списка: '))
min_elem = int(input('Введите минимальное число списка: '))
max_elem = int(input('Введите максимальное число списка: '))
start = int(input('Введите начальный элемент диапазона: от '))
end = int(input('Введите последний элемент диапазона: до '))
print()
print("Заданный список:")
print(new_list := list([randint(min_elem, max_elem) for i in range(new_size)]))
print()
sleep(2)
index_list = find_index(new_list, start, end)
if index_list == []:
  print(f"Элементы, входящие в диапазон от {start} до {end}, отсутствуют")
else:
  print(f"Список индексов элементов, входящих в диапазон от {start} до {end}")
  print(index_list)
print()
sleep(2)
print("*** Ну вот и всё, ребята! ***")
print()