from random import randint
from time import sleep

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

def create_list(size, min = 1, max = 10):
  new_list = []
  for _ in range(size):
    new_list.append(randint(min, max))
  return new_list
    
def same_numbers_in_lists(list1, list2):
  same_numbers_list = []
  for number in list1:
    if number in list2:
        same_numbers_list.append(number)
  if same_numbers_list == []:
    print("Общих чисел нет!")
  else:
    print(f'Общие числа из обоих наборов: {quicksort(same_numbers_list)}')
  return set(same_numbers_list)

print("****************************************************************")
print("Задача 22: Данная программа принимает на вход два набора чисел, а выдает все те числа, которые встречаются в обоих наборах без повторений в порядке возрастания.")
size1 = int(input('Введите размер первого набора чисел: '))
min1 = int(input('Введите минимальное значение первого набора чисел: '))
max1 = int(input('Введите максимальное значение первого набора чисел: '))
list_1 = create_list(size1, min1, max1)
print()
print(f'Первый набор чисел: {list_1}')
print()
size2 = int(input('Введите размер второго набора чисел: '))
min2 = int(input('Введите минимальное значение второго набора чисел: '))
max2 = int(input('Введите максимальное значение второго набора чисел: '))
list_2 = create_list(size2, min2, max2)
print()
print(f'Второй набор чисел: {list_2}')
print()
sleep(2)
same_numbers_in_lists(list_1, list_2)
print()
sleep(1)
print("Загрузка следующей задачи...")
print()
sleep(3)






# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

def find_best_picks(bush):
  max_berries = 0
  best_bush_number = 0
  for i in range(len(bush)):

    grab = bush[i - 1] + bush[i] + bush[0]
    
    if i + 1 >= len(bush):
      if grab > max_berries:
        max_berries = grab
        best_bush_number = i
    elif bush[i - 1] + bush[i] + bush[i + 1] > max_berries:
      max_berries = bush[i - 1] + bush[i] + bush[i + 1]
      best_bush_number = i

  print(f'Наибольшее количество ягод с трёх кустов - {max_berries}, центральный куст - {best_bush_number + 1}')

print("****************************************************************")
print("Задача 24: Данная программа принимает на вход список кустов, на которых растет какое-то количество ягод (от 1 до 10), и выдает наибольшее количество ягод c трёх рядом стоящих кустов и номер центрального кустика (с учетом его соседей)")
size = int(input('Введите количество кустов: '))
farm_plot = create_list(size)
print()
print(f'Кусты и количество ягод на них: {farm_plot}')
print()
sleep(2)
find_best_picks(farm_plot)
print()
sleep(2)
print("*** Ну вот и всё, ребята! ***")
print()