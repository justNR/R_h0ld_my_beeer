# #1
# print("Привет, мир!")
# print(5, 10, 15)

# print(10 + 25)

# #2

# print(1, 2, 3, sep='&')
# a = "Python"
# b = "лучший язык"
# print(a, b,  end="")

# #3

# x = 3.14
# y = -8
# print(f'Координаты точки: x = {x}; y = {y}')

# name = input("Введите имя: ") 
# age = input("Введите возраст: ") 
# print(f"Имя: {name}, Возраст: {age}")

# #4
# a = input("Введи имя: ")
# print(f"Привет, {a}!")

# #5
# a = input("Введи число a: ")
# b = input("Введи число b: ")
# print(a + b)

# c = int(input("Введицелое число: "))
# print(f"Число в квадрате: {c ** 2}")

# #1
# print(5 > 3)
# print(10 < 2)
# print(7 == 7) 
# print(6 != 8)
# print(4 >= 4)
# print(9 <= 3)

# res = 8 > 12
# print("Значение res:", res) 
# print(type(res)) #

# #2
# x = 15
# print(x % 2 == 0)
# print(x // 5) 
# print((x % 3 == 0) and (x % 5 == 0)) 

# #3
# y = 4.5
# print(y >= 1 and y <= 10)
# print((y >= 0 and y <= 5) or (y >=10 and y <= 15))

# #4

# print(True or False and False) # True
# print(not False and True) # True
# print(False or not True and True) ## False
# print(not (10 > 5 or 3 < 1)) # False

# #5
# a = 200
# print(bool(0)) # False
# print(bool(-5)) # True
# print(bool(3.14)) # True
# print(bool("")) # False
# print(bool("Python")) # True
# print(bool(" ")) # True

# #6

# n = 4
# print(n > 0) #True
# print(n % 2 == 0) #True
# print(n % 3 == 0) #False


#1

s = "Программирование"

print(s[0]) 
print(s[- 1]) 
print(s[2],s[-2])

#2 

#print(s[100]) #IndexError: string index out of range
print(len(s)-1) 

#3
ac = s[:6]
print(ac)
bc = s[-5:]
print(bc)
cc = s[3:7]
print(cc)
dc = s[1::2]
print(dc)
ec = s[::-1]
print(ec)

#4
print(s[::3]) 
print(s[::-2])

#5

# s[0] = "п" # TypeError: 'str' object does not support item assignment
s2 = 'Жар'
s2 = "П" + s2[1:]
print(s2)

#6

word = "abcdefgh"
print(word[2:5]) # подстрока "cde" с помощью среза
print(word[::-1])
print(word[1:7])