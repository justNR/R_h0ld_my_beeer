def identity_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"result after calling")
        return result
    return wrapper

@identity_decorator
def say_hello():
    return "Hi"

say_hello()