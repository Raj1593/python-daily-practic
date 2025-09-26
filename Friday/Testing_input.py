# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
#
# print(f" {name} is {age} years old")


# name = input("what is your name: ")
# age = input("what is your age: ")
#
# age = int(age) + 1
# print(f"my name is {name}")
# print(f"my age is {age}")


# import math
#
# radius = float(input("enter your radius: "))
# area = math.pi * radius ** 2
# circumference = 2 * math.pi * radius
#
#
# a = float(input("enter your side a: "))
# b = float(input("enter your side b: "))
#
# c = math.sqrt(pow(a, 2) + pow(b, 2))
#
# print(f"side c is:{c}")
#
# print(f"my circumference is {circumference}")
# print(f"my area is {area}")

age = int(input("age: "))

if age >= 18:
    print(f"you are eligible to vote because your are {age} years old")
else:
    print(f"you are not eligible to vote because your are {age} years old")