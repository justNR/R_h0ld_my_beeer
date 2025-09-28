# #1

# lst = [1, 2, 3, 4, 5, 6]

# it_lst = iter(lst)
# print(next(it_lst))
# print(next(it_lst))
# print(next(it_lst))
# print(next(it_lst))
# print(next(it_lst))
# print(next(it_lst))


# #2
# str_it = "Привет как дела?"

# it_str = iter(str_it)
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))


#1

n = 10

a = [i ** 2 for i in range(1, n + 1)]
print(a)


#2

b = [i for i in range(-10, 11) if i % 2 == 0]
print(b)

#3

str_list = ["Москва", "Дмитров", "Яблоко", "Груша"]

len_str = [len(el) for el in str_list]
print(len_str)

#4


list_num = ["четное" if i % 2 == 0 else "нечетное" for i in range(1, 21)]
print(list_num)

#5

m_list = [1, "Привет", [1, "Список", 3]]

check_list = [True if iter(el) else False for el in m_list] #выбросит исключение для не итеруруемых обьектов, нужно сделать через try/exept
print(check_list)