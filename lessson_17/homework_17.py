#1

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]


res = list(filter(lambda x: isinstance(x,(str, list)), items))

print(res)


#2

def describe_type(x):
    if isinstance(x, str):
        print("Это строка")
    elif isinstance(x, bool):
        print("Это булево значение")
    elif isinstance(x, (int, float)):
        print("Это число")
    else:
        print("Неизвестный тип")

describe_type(5.5)       # Это число
describe_type(True)      # Это булево значение
describe_type("Привет")  # Это строка
describe_type([1, 2, 3]) # Неизвестный тип


#3

def filter_list(f, data: list[int]) -> list[int]:
    return list(filter(f, data))

data = [1, 3, 5, 7]
result = filter_list(lambda x: x > 3, data)
print(result) 

#4

def print_info(name: str, age: int, tags: str) -> None:
    print(name, age, tags)

#5

def analyze(data: list):
    if data:  
        count = len(data)
        avg = sum(data) / count
        print(f"Количество элементов: {count}, среднее значение: {avg}")
    else:
        print("Список пустой")

#6

flags = [True, True, True, False]

print(all(flags))
print(any(flags))


#7

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']

win_row = all([x == "x" for x in field[0:3]])

print(win_row)


#8

P = ['0', '0', '0', '*', '0']

mine = any([x== "*"] for x in P)
print(mine)


#9

from random import choices
colors = ["red", "green", "blue", "yellow", "purple"]
print(choices(colors))

#10

import random

random.seed(1)
print([random.randint(0, 100) for _ in range(10)])


#11
def greet(name: str) -> str:
    return f"Привет, {name}"

#12

def multiply(a: int, b: float) -> float:
    return a * b


#13

def area(length: float, width: float) -> float:
    return length * width


print(area.__annotations__)