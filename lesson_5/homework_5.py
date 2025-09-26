#1

cities = ['Москва', 'Тверь', 'Вологда']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'привет', False, 2.122121]

#2

print(cities[1])
print(numbers[-1])
#print[cities[10]] # IndexError: list index out of range

#3
numbers[2] = 10
mixed[-1] = 'Python'

#4
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers, reverse=True))

#5

num1 = [1, 2, 3]
num2 = [4, 5]
num3 = num1 + num2
strc = ["Python", 'is', 'awsome'] * 3
print(num3)
print(strc)

#6
print(3 in numbers)
print("Москва" in cities)
print([1,2] in mixed)

#7

numbers.pop(2)
print(numbers)
del cities[-1]
print(cities)


#8
s = "Python"
res = list(s)
print(res)

#1
n_cities = ["Москва", "Тверь", "Волгоград", "Дмитров", "Пушкино",]
c_cities = n_cities[:]
print(c_cities)
print(id(n_cities))
print(id(c_cities))


#2

print(n_cities[1:3])
print(n_cities[2:])
print(n_cities[0:3])
print(n_cities[:])
print(n_cities[-2:])

#3

print(n_cities[:])
print(n_cities[::-1])
print(n_cities[-2::-2])

#4

n_cities[1:2] = 'Сочи', 'Нижний новгород'
print(n_cities)

n_cities[1::2] = ["Город"] * len(n_cities[1::2])
print(n_cities) 
n_cities[1:3] = "Волгоград", "Омск"
print(n_cities) 

#5

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

list3 = ["Python", "rocks"] * 2
print(list3)


#6
list1 = [1, 2, 3] == [1, 2, 3]
print(list1)

list2 = [10, 5, 3] > [5, 10, 3] # True
print(list2)

list3 = [1, 2, 3] == [1, 2, "abc"]
print(list3) # False

#7

chars = list("Python")
print(chars)

print(max(chars)) # y
print(min(chars)) # P
result = chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[5]
print(result)


#1
numbers = [5, 10, 15]
numbers.append(20)
print(numbers)
numbers.insert(1, 7)

numbers.append("Python")
print(numbers)

#2

numbers.remove(10) # было [5, 7, 10, 15, 20, 'Python']
print(numbers) 

print(numbers.pop(-1))

print(numbers.pop(1))

numbers.clear()
print(numbers)

#3

letters = ["a", "b", "c"]
print(letters) 



copy1 = letters[:]
copy2 = list(letters) 
copy3 = letters.copy()


print(id(copy1)) 
print(id(copy2)) 
print(id(copy3)) 


print(letters is not copy1) # True
print(letters is not copy2) # True
print(letters is not copy3) # True

#4

marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks)

print(marks.count(3))
print(marks.index(5))
print(6 in marks)

#5

nums = [8, 2, 5, 1, 7]
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)

#6

cities = ['Москва', 'Тверь', 'СПБ', 'Волгоград', 'Дмитров']
print(cities.sort(reverse=True))

sorted_cities = sorted(cities)

print(sorted_cities) 
print(cities)

#7

chars = list("programming")
print(chars)

print(chars.count('g')) 

chars.reverse()
print(chars)

chars.sort()
print(chars)

#1


a = [
    [1, 2, 3, 4],     
    [5, 6, 7, 8],     
    [9, 10, 11, 12]   
]


print(a)

for row in a:        
    print(row)

print(a[1])
print(a[2][0])

#2

a[0] = [0, 0, 0, 0]
print(a)

a[1][3] = "Python"
print(a)