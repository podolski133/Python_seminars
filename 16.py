# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

N = int(input('Введите число: '))
def get_factorial_list(n):
    fact = 1
    facts = []
    for i in range(1, n+1):
        fact *= i
        facts.append(fact)
    return facts
print(get_factorial_list(N))