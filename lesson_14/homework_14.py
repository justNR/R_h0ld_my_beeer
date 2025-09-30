# #1

# from math import sqrt, pow


# print(sqrt(64))
# print(pow(5,3))


# #2

# from random import choice, randint

# print(randint(1,10))
# print(choice(["Python, Java, C++"]))


# #3

# import my_module

# print(my_module.add(2,3))
# print(my_module.multiply(2,3))


# #4

# #done


# #5

# import time

# start_t = time.time() 

# time.sleep(2)
# end_t = time.time()
# print(f"Код выполнялся {end_t - start_t}")


#6

import requests

response = requests.get("https://api.github.com")
print(response.status_code)


#7

import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


#8

#done