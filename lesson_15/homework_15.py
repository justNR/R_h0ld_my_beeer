#1
# file1 = "lesson_15/data.txt"


# res =  open(file=file1, mode="r", encoding="utf-8")

# txt_l = res.readlines()
# print(txt_l)


#2

# file1 = "lesson_15/data.txt"


# with open(file=file1, mode="r", encoding="utf-8") as f:

#     txt_l = f.readline()
#     print(txt_l)

#3


# file1 = "lesson_15/data.txt"


# with open(file=file1, mode="r", encoding="utf-8") as f:
#     print(f.read(10))


# #4
#     file1 = "lesson_15/data.txt"


# with open(file=file1, mode="r", encoding="utf-8") as f:
#     out_file = []
#     for symb in f:
#         out_file.append(symb)
#     print(out_file)


#5
# file1 = "lesson_15/data.txt"
# with open(file=file1, mode="r", encoding="utf-8") as f:
#     for line in f:
#         print(f"Cтрока: {line.rstrip()}")


#6

# file1 = "lesson_15/data.txt"
# with open(file=file1, mode="r", encoding="utf-8") as f:
#     print(f.read(6))
#     f.seek(0)
#     print(f.read(6))



# #7
# file1 = "lesson_15/data.txt"
# with open(file=file1, mode="r", encoding="utf-8") as f:
#     f.seek(0, 2)                      
#     size = f.tell()   
#     print(f"Размер файла: {size} байт")

#8
# file1 = "lesson_15/data.txt"
# with open(file=file1, mode="r", encoding="utf-8") as f:
#     print(f.read())

#9

# file1 = "lesson_15/data1.txt"
# try:
#     with open(file=file1, mode="r", encoding="utf-8") as f:
#         f.seek(0, 2)                      
#         size = f.tell()   
#         print(f"Размер файла: {size} байт")
# except:
#     print("Ошибка: Файл не найден")

#10

# file1 = "lesson_15/data.txt"

# try:
#     res =  open(file=file1, mode="r", encoding="utf-8")

#     txt_l = res.readlines()
#     print(txt_l)
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     res.close()


#11
# file1 = "lesson_15/data.txt"
# try:
#     with open(file=file1, mode="r", encoding="utf-8") as f:
#        for line in f:
#            print(line.rstrip()) 
# except:
#     print("Ошибка: Файл не найден")


#12

# file1 = "lesson_15/numbers.txt"
# try:
#     with open(file=file1, mode="r", encoding="utf-8") as f:
#         count = 0
#         for line in f:
#             count += int(line)
#         print(count)
# except:
#     print("Ошибка: Файл не найден")


#13

import datetime

file1 = "lesson_15/log.txt"
with open(file=file1, mode="a", encoding="utf-8") as f:
    log_type = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    f.write(f"{log_type} - Запуск программы \n")
