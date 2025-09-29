# #1
# def greet(name: str) -> str:
#     print(f"Привет, {name}! Добро пожаловать!")

# greet("Анна")

# #2

# def square(num: int) -> int:
#     return num ** 2

# print(square(5))


# #3
# def is_even(num: int) -> bool:
#     return True if num % 2 == 0 else False

# print(is_even(4))

# #4
# def repear_string(text: str, times: int) -> str:
#     return text * times

# print(repear_string("привет ", 5))

# #5

# def add(a,b) -> int:
#     return a + b

# print(add(3,2))

# #6

# def get_max(a, b, c):
#     return max(a,b,c)

# print(get_max(2,4,6))

# #7

# def calculate(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         return a / b
# print(calculate(5, 5, "+"))

# #8

# def reverse_string(text):
#     return text[::-1]

# print(reverse_string("привет"))

# #9

# def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
#     if ignore_spaces:
#         s1 = s1.replace(" ", "")
#         s2 = s2.replace(" ", "")
#     if ignore_case:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     return s1 == s2
# print(compare_strings("Hello", " hello "))


# #11

# def create_profile(name, age, **extra):
#     print("Профиль пользователя:")
#     print(f"Имя: {name}")
#     print(f"Возраст: {age}")
#     if extra:
#         print("Дополнительная информация:")
#         for key, v in extra.items():
#             print(f"{key}: {v}")

# print(create_profile("Иван", 30, city="МСК", job='QA'))


# #12

# def process_orders(*orders, discount=0):
#     sum_ord = sum(orders)
#     sale = sum_ord * (1 - discount / 100)
#     print(f"Сумма заказа: {ord}")
#     print(f"С учетом скидки: {sale}")
# process_orders(100, 200, 300, discount=10)

# #13

# def merge_lists(*lists):
#     result = []
#     for lst in lists:
#         result.extend(lst)
#     return result
# print(merge_lists([1, 2], [3, 4], [5, 6]))

# #14

# def merge_dicts(*dicts):
#     result = {}
#     for dict in dicts:
#         result.update(dict)
#     return result