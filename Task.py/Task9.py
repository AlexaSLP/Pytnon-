# Задача 9/ По данному целому неотрицательному числу n
# вычислите значение n!. N! = 1 * 2* 3 * ... * N 
# (произведение всех чисел от 1 до N) 0! = 1

# input 5
# output 120

n = int (input('Введите целое число '))
factorial = 1
while n > 1 :
  factorial *= n
  n -= 1

print('Произведение всех чисел: ', factorial)