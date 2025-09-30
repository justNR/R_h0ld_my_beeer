
# #1
# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper


# @uppercase_decorator
# def say_hello():
#     return "hello, world!"


# print(say_hello())  # "HELLO, WORLD!"

#2

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args , **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def hello():
#     print("hello")


# hello()


#3

def cache(func):
    stored_res = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_res:
            return stored_res[key]

        result = func(*args, **kwargs)
        stored_res[key] = result
        return result

    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b

print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (из кэша, без печати)
print(slow_add(4, 5))  # "Вычисляю 4 + 5..." 9
print(slow_add(4, 5))  # 9 (из кэша)

import time

#4

def timer(n):
    def decorator(func):
        def wrapper(*args, **kwargs): 
            total_time = 0
            result = None
            for _ in range(n):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)
            avg_time = total_time / n
            print(f"Средняя время выполнения: {avg_time:.3f}" )
            return result
        return wrapper
    return decorator


@timer(5)
def slow_function():
    time.sleep(2)
slow_function()

