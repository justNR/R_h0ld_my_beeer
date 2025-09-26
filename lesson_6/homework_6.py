
#1
x = int(input("Введи число "))

if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")


#2

x = int(input("Введи число "))

if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")


#3

x = int(input("Введи число "))

if x in range(1,10):
    print("Число в диапазоне")
else:
    print("Число вне диапазона")

#4

a = int(input("Введи число "))
b = int(input("Введи число "))

if a < b:
    b = a
print(sorted(a,b))

#5
a = int(input("Введи число "))
b = int(input("Введи число "))
if a < b:
    print(a)
else:
    print(b)

#6

marks = [3, 4, 5, 2, 5, 4]

if 2 in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")


#7

x = int(input("Введи число "))

if x % 3 == 0 and x % 5 == 0:
    print("Число делится на 3 и 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
else:
    print("Число не делится на 3 и 5")

#8

x = str(input("Введи пароль "))
if "admin123" == x:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#9

amount = int(input("Введи сумму покупки "))

if amount >= 5000:
    discount = 0.1
elif amount >= 1000:
    discount = 0.05
print(amount * discount)

#10

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")


#1

grade = int(input('Введите оценку (от 1 до 5): '))
if grade == 5:
    print("Отлично!")
if grade == 4:
    print("Хорошо")
if grade == 3:
    print("Удовлетворительно")
if grade == 2 or grade == 1:
    print("Некорректная оценка")
if grade == 0:
    print("Некорректная оценка")


#2

time = int(input('Введите текущее время в часах (0-23): '))
if time < 0 or time > 23:
    print("Некорректное время")
elif 6 <= time <= 11:
    print("Утро")
elif 12 <= time <= 17:
    print("День")
elif time >= 18 and time <= 21:
    print("Вечер")
elif time >= 22 or time <= 5:
    print("Ночь")

#3

temperature = int(input("Введите температуру: "))
if temperature < -10:
    print("Очень холодно")
elif -10 <= temperature <= 0:
    print("Холодно")
elif 1 <= temperature <= 10:
    print("Прохладно")
elif 11 <= temperature <= 25:
    print("Тепло")
elif temperature >= 25:
    print("Жарко")


#4

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")



#5

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")
if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Результат:", num1 / num2)
    else:
        print("Ошибка: деление на ноль!")

else:
    print("Некорректная операция")

#1

number = int(input("Введите число: "))
result = "Четное" if number % 2 == 0 else "Нечетное"
print(result)

#2

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
max_num = num1 if num1 > num2 else num2
print("Наибольшее число: ", max_num)

#3

num1 = int(input("Введите число: "))
result = "Положительное число" if num1 > 0 else ("Отрицательным число" if num1 < 0 else "Ноль")
print(result)

#4

age = int(input("Введите свой возраст: "))
print("Вход разрешен" if age >= 18 else "Вход запрещен")

#5

amount = int(input("Введите сумму покупки: "))
final_amount = amount * 0.9 if amount > 5000 else amount
print(f"Итоговая сумма: {final_amount} руб.")