
# #1
# dict_fruits = {"Яблоко": 200, "Груша": 150, "Виноград": 250}
# dict_fruits["Лимон"] = 300
# print(dict_fruits)

# #2

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# score = [name for name, score in grades.items() if score >= 4]
# print(score)

# #3

# dict_countries = {"Россия": "Москва", "США": "Вашинтон", "Великобритания": "Лондон", "Китай": "Пекин"}
# country = str(input("Введите название страны "))

# capital = dict_countries.get(country, "Страна не найдена")
# print(capital)


# #4

# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]

# courses = {}
# for name, course in students:
#     courses.setdefault(course, []).append(name)

# print(courses)


#5

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# print(grades)
# lower = min(grades, key=grades.get)
# grades.pop(lower)

# print(grades)

# #6

# students = ["Анна", "Борис", "Виктор", "Галина"]

# stidents_dict = dict.fromkeys(students, None)
# for s, v in stidents_dict.items():
#     print(f"{s}: {v}")
# stidents_dict.update({"Анна": 18, "Борис": 25, "Виктор": 52, "Галина": 30})
# print(stidents_dict)

#7

# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
# currency = str(input("Введите название валюты "))

# if currency in exchange_rates:
#     print(exchange_rates[currency])
# else:
#     print("Неизвестная валюта")
#     exchange_rates[currency] = None
#     print(exchange_rates)

#8

# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
# dict1.update(dict2)

# print(dict1)


#1


# t_nums = (4, 7.2, "привет", False, [1,2,3])
# print(t_nums[1], t_nums[-1])

# #2
# nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
# print(f" Количество вхождений числа 4: {nums.count(4)}, Индекс первого числа 7: {nums.index(7)}")

# #3
# lst = ["Python", "Java", "C++", "JavaScript"]
# t_lst = (lst)
# print(lst.__contains__("C++"))


# #4

# t_nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t_nums[0:3], t_nums[-3:], t_nums[::2])

#5

# t_tup = (1,2, {"Анна": 20, "Влад": 26}, ["яблоко", "груша", "мармелад"])
# t_tup[3].append("молоко")
# print(t_tup)