# 1 
name = 'Роман'
age = 29
height = 83.50
print(f"Меня зовут {name}, мне {age} лет, мой вес {height} кг")
# 2
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
print(x)
# 3
a = 7
b = a
print(a,b)
a = 10
print(b)
# b ссылается на старый объект a, который равен 7 

# 4
x,y,z = 100
print(x,y,z)
print(x(id), y(id), z(id))
# id одинаковые
x,y,z = 10,5,6
print(x,y,z)
print(x(id), y(id), z(id))
# id разные

# 5
a,b = 10,7
a,b = b, a
print(a,b)

# 6
# True = 1
# print = 4
# if = 22
# При использовании переменных с системными названиями выдается ошибка
# Переменные нельзя так называть, потому что они зарезервированы под конкретные цели

import keyword
print(keyword.kwlist)

# 7

var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1= "Test"
print(type(var1))


# 8
pI = 3.14
msg = 'Message'
a_age = 30
is_valid = True
n_number = 2
print(pI, msg, a_age, is_valid, n_number)
print(type(pI))
print(type(msg))
print(type(a_age))
print(type(is_valid))
print(type(n_number))

Число = 10 # не работает
