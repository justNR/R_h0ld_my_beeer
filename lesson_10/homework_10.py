# #1

# uniq = {1,2,3}
# uniq.add(1)
# print(uniq)

# #2

# set_cities = {"Москва", "Ростов", "СПБ"}
# print(set_cities)

# #3

# set_nums = set(range(11))
# set_nums.discard(5)
# set_nums.discard(15)

# print(set_nums)


# #4
# str1 = "abrakadabra"
# uniq_set = set(str1)  
# print("Множество:", str1)
# print("Количество букв:", len(uniq_set))


#5

# uniq_set = set()

# uniq_set.add(10)
# uniq_set.add("hello")
# uniq_set.add((1,2,3))
# uniq_set.add([1,2,3]) # TypeError: unhashable type: 'list' нельзя добавить изменяемый тип
# print(uniq_set)

#6

# set_1 = {1,2,3}
# set_2 = {2,3,4,5}
# enumer = set_1.intersection(set_2)
# set_uni = set_1.union(set_2)
# set_diff = set_1 - set_2
# set_diff_ba = set_2 - set_1
# set_simm_diff = set_1.symmetric_difference(set_2)
# print(enumer, set_uni, set_diff, set_diff_ba, set_simm_diff)


# #7

# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}
# print(even_numbers.intersection(odd_numbers))
# print(even_numbers.union(odd_numbers))

#8

python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}

print(f"На оба курса записаны {python_students.intersection(java_students)}")
print(f"На один курс записаны {python_students.symmetric_difference(java_students)}")
print(f"На хотя бы один курс записаны {python_students.union(java_students)}")


#9

# text1 = set("программирование")
# text2 = set("автоматизация")

# print("Общие буквы:", text1 & text2)
# print("Только в первом слове:", text1 - text2)
# print("Уникальные буквы каждого слова:", text1 ^ text2)

# #1
# set_pow = {x ** 2  for x in range(1, 10) if x % 2 == 0}
# print(set_pow)

# #2
# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]

# set_words = {word.upper() for word in words}
# print(set_words)


# #3
# grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}

# new_grades = {value: ("отлично" if score >= 80 else "удовлетворительно") for value, score in grades.items()}
# print(new_grades)


#4
text = {"Python", "automation", "programming", "testing"}

new_text = {word: len(word) for word in text}
print(new_text)

#5

n = 10

new_dict = {i: {j**2 for j in range(i, i+1)} for i in range(1, n+1)}
print(new_dict)