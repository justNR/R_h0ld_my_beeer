#1

num = int(input("Введи число "))

i = 0
while i < num:
    i += 1 
    print(i)


#2

num = int(input("Введи число "))
i = 0
even = 0
while i < num:
    even += i
    i += 2
print(even)



#3

num = int(input("Введи число "))
ccount = 0
while num > 0:
    count += 1
    num //= 10
print(ccount)


#4

num = int(input("Введи число "))
max_n = 0
while num > 0:
    last_digit = num % 10
    if last_digit > max_n:
        max_n = last_digit
    num //= 10
print(max_n)


#5

passwd = ""
while passwd != "qwerty123":
    passwd = input("Введите пароль ")


#1

lst = [1, 2, 5, 7, 9]

i = 0

while i < len(lst):
    if lst[i] % 2 == 0:
        print(lst[i])
        break
    i += 1
    
#2

total = 0
while True:
    num = int(input("Введите число (0 для выхода) "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)


# 3

a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))

start = min(a,b)
last = max(a,b)

curr = start

print("Нечетные ")
while curr <= last:
    if curr % 2 == 0:
        curr += 1
        continue
    print(curr)
    curr += 1

#4

n = int(input("Введите число n: "))

if n <= 1:
    print("Не простое число")
else:
    i = 2
    while i < n:
        if n% i == 0:
            print(f"Не простое число (тк делится на {i})")
            break
        i += 1
    else:
        print(f"{n} простое число")

#5

max_num = None
while True:
    u_input = input("Введите число: ")
    if u_input == "":
        break
    num = int(u_input)
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num
if max_num is not None:
    print(f"Наибольшее число: {max_num}")
else:
    print("Не было введено ни одного числа")


#1
word = input("Введите строку: ")
for char in reversed(word):
    print(char)

#2

num = [1, 2, 4, 6, 7, 8, 9, 10]

for i in range(len(num)):
    if num[i] % 2 == 0:
        num[i] = 0
print(num)

#3

n = int(input("Введите число N: "))
pows = []
for i in range(n + 1):
    pows.append(2 ** i)
print(pows)

#4

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
k = int(input("Введите шаг K: "))
for num in range(a, b + 1, k):
    print(num)


