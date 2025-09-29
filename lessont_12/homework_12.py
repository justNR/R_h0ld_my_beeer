#1
pow = lambda x: x**2

print(pow(5))

#2
is_even = lambda x: x % 2 ==0

print(is_even(3))

#3

def sort_by_last_letter(words):
    return sorted(words, key=lambda x: x[-1])
words = ["banana","cherry", "apple"]
print(sort_by_last_letter(words))

#1

def multiply_by(n):
    def wrap_mult(x):
        return n * x
    return wrap_mult

times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # 30
print(times5(10))  # 50


#2

def counter(start=0):
    count = start
    def wrap_count():
        nonlocal count
        count += 1 
        return count
    return wrap_count

c1 = counter(5)
c2 = counter()
print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2
