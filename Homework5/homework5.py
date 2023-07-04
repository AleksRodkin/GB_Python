from time import sleep

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(A, B):
  if B != 0:
    return exponentiation(A, B-1) * A
  return 1

print("****************************************************************")
print("Задача 26: Данная программа на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.")
base = int(input('Введите число А (основание): '))
exponent = int(input('Введите число В (показатель): '))
exponentiation_1 = exponentiation(base, exponent)
print()
print(f'Число {base} в степени {exponent} равно {exponentiation_1}')
print()
sleep(1)
print("Загрузка следующей задачи...")
print()
sleep(3)



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.

def recursive_sum(a, b):
  if b != 0:
    return recursive_sum(a + 1, b - 1)
  return a


print("****************************************************************")
print("Задача 28: Данная программа демонстрирует результат работы рекурсивной функции recursive_sum(a, b), возвращающей сумму двух целых неотрицательных чисел")
num_a = int(input('Введите первое слагаемое: '))
num_b = int(input('Введите второе слагаемое: '))
recursive_sum_1 = recursive_sum(num_a, num_b)
print()
print(f'{num_a} + {num_b} = {recursive_sum_1}')
print()
sleep(2)
print("*** Ну вот и всё, ребята! ***")
print()