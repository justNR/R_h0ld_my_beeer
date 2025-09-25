#1
s = "Python для авторизации"
print(s.upper()) 
print(s.lower())
#2
msg = "абракадабра"
msg.find("ра")
msg.count("а", 2)

#3
print(msg.find("ка")) 
print(msg.rfind("а")) 
print(msg.find("xyz")) 

#4
text = "Я изучаю Java"
txt1 = text.replace("Java", "Python")
print(txt1.replace(" "," "))

#5

str = "Python"
print(str.isalpha())
str1 = "12345"
print(str1.isdigit()) 
str2 = "123abc"
print(not str2.isdigit()) 

#6

code = "42"
print(code.rjust(5, "0"))
text = "text"
print(text.ljust(10, "*"))

#7

text = "яблоко, груша, банан"
print(text.split())

text1 = "Python;Java;C++"
print(text1.split(";"))

#8

words = "Привет", "мир", "!"
print(" ".join(words)) # Привет мир !

fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))

#9
str1 = " Python"
print(str1.lstrip())
str2 = "Python "
print(str2.rstrip())
str3 = " Python "
print(str3.strip())

#10

text = "программирование"
print(text.replace("п", "П")) 
print(text.capitalize())
print(text.count("р")) 
print(text.find("и")) 
print(text[::-1])

#1
text = "Hello\nPython"
print(text) 

#2
t = "Python\tAutomation"
print(t)

#3
path = "C:\new\test.txt"
print(path)

path1 = "C:\\new\\test.txt"
print(path1)

text1 = "Марка вина \"Ягодка\""
print(text1)

#4

path = r"C:\new\test.txt"
print(path) # в обычной строке спец символы обрабатываются а в сырой игнорируются

#5

s = "Hello\b World"
print(s) # Hell World - символ - \b-удаляет предыдущий символ

s1 = "Hello\fPython"
print(s1) # HelloPython

#1

name = "Рома"
age = 29

print("Меня зовут " + name + ", мне " + str(age) + " лет.")
print("Меня зовут " + name + ", мне " + age + " лет.") # TypeError: can only concatenate str (not "int") to str

#2
name = "Маша"
age = 36
print("Привет, меня зовут {name}, мне {age} лет.".format(name=name, age=age)) 
print("Привет, меня зовут {name}, мне {age} лет.".format(age=age, name=name)) 

#3

city = "Москве"
year = 2025
print(f"Сегодня {year} год, и я живу в {city}.") 
print(f"Через 5 лет будет {year + 5} год.")

#4

name = "Рома"
age = 29

print(f"Дважды мой возраст: {age*2}") 
print(f"Мое имя в верхнем регистре: {name.upper()}")

#5


dollar_rate = 84
print("Курс валют: 1 доллар = {:.1f} рубля.".format(dollar_rate))

number = 7
print(f"Квадрат числа {number} равен {number ** 2}.")