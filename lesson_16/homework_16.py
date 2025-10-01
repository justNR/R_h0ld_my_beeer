#1
# lst = ["Python", 123, "Java", 456, "C++", 789]

# str_lst = filter(lambda x: isinstance(x, str), lst)
# strs = " ".join(str_lst)

# print(strs)


#2

# import random
# gen = (random.randint(1, 100) for _ in range(10))
# print(f"Максимальное число {max(gen)}")

# #3

# file_name = 'lesson_16\words.txt'

# def long_words(file_name):
#     with open(file=file_name, mode="r", encoding="utf-8") as f:
#         for line in f:
#             for w in line.split():
#                 if len(w) > 5:
#                     yield w

# for w in long_words(file_name):
#     print(w)

#4

# file_name = "lesson_16/text.txt"

# def contains_python(file_name):
#     with open(file=file_name, mode="r", encoding="utf-8") as f:
#         for line in f:
#                 if "Python" in line:
#                     yield line.strip()

# for line in contains_python(file_name):
#     print(line)


# #5

# import random

# def random_until_50():
#     while True:
#         n = random.randint(1, 100)
#         yield n 
#         if n == 50:
#             return
         
# print(*random_until_50())

# #6

# def is_prime(x):
#     if x < 2:
#         return False
#     if x in(2,3):
#         return True
#     if x % 2 == 0:
#         return False
#     d = 3
#     while d * d <= x:
#         if x % d == 0:
#             return False
#         d += 2
#     return True

# def gen_primes(n):
#     count = 0
#     num = 2 
#     while count < n:
#         if is_prime(num):
#             yield num
#             count += 1
#         num += 1

# print(*gen_primes(10))


# #7

# def api_loader():
#     i = 1
#     while True:
#         yield f"Получены данные {i}"
#         i += 1

# gen = api_loader()
# for _ in range(5):
#     print(next(gen))


# #8

# s = input("Введите числа через пробел ").strip()

# pows = list(map(lambda x: int(x) ** 2, s.split()))
# print(pows)

#9

# cities =  ["Москва", "Санкт-Петербург", "Казань"]

# cities_upper = list(map(lambda x: x.upper(), cities))
# print(cities_upper)

# #10

# lits = [15, 30, 45, 22, 60, 77, 90, 100]

# dels = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, lits))

# print(dels)

# #11

# lists = ["hello", "world42", "python3", "abc", "123", "data1science"]

# digit = list(filter(lambda x: not x.isalpha(), lists))
# print(digit)


# #12

# countries = ["Россия", "Франция", "Германия"]
# capitals = ["Москва", "Париж", "Берлин"]

# countries_citiez = zip(countries, cities)

# print(list(countries_citiez))

# #13

# data = [(1, 'a'), (2, 'b'), (3, 'c')]
# unzip1, unzip2 = zip(*data)
# print(unzip1)
# print(unzip2)

#14

names = ["петр", "Иван", "мария", "Анна"]

res = sorted(names, key=lambda x: (x[0].islower(), tuple(map(ord,x))))

print(res)

#15

products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
products.sort(reverse=True)
print(products)