# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе.

# 6 -> 1 4 1 


S = int (input('Введите количество журавликов, которых сделали дети вместе '))
P = S//6
K = P*4
print(P, K, P)