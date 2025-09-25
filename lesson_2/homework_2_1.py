#1

a, b = 5, 3
x, y = 1.25, 3.45
print(a,b,x,y)
print(type(a))
print(type(b))
print(type(x))
print(type(y))

#2

num1 = 100
num2 = 10
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

#3

a, b = 10, 3
print(a / b)
print(a // b)
print(a % b)
a, b = -10, 3
print(a / b)
print(a // b)
print(a % b)
a, b = 10, -3
print(a / b)
print(a // b)
print(a % b)


#4

print(5 + 3 * 2)
print((5 + 3) * 2)
print(10 / 2 ** 2)

#5
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)

#1

s1 = 'Python'
s2 = 'Программирование'

print(s1, s2)

multiple_str = '''тест
тест
тест
'''
print(multiple_str)
empty = ""
print(len(empty))

#2

first_name = 'Иван '
last_name = 'Петров'
full_name = first_name + last_name
print(full_name)

#3

s = "Возраст: "
age = 25
result = s + str(age)
print(result)

#4
str1 = ("xa ") * 5
print(str1)

# s2 = ("xa ") * 2.5
# print(s2)  # can't multiply sequence by non-int of type 'float'

#5
text = "Привет, мир!"
print(len(text))

str2 = ""
print(len(str2))

#6
sentence = "Я изучаю Python"
print("Python" in sentence) # True
print("Java" in sentence) # False

#7
a = "apple"
b = "banana"
print(a == b)
print(a != b) 
print(a < b)
print(a > b) 
print(a <= b) 
print(a >= b) 

#8
print(ord('A')) 
print(ord('a'))
print(ord('Я'))