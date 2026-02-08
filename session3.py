# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)

# age = int(input("enter your age: "))
# if age > 15:

#     print("ok your access is valid")
# else:
#     print("access denied")


# name = input("enter the name: ")
# if name == "kian" or name == "radin" or name == "radman":
#     print("hi", name)
# name = input("enter the name: ")
# age = int(input("enter the age: "))

# if name == "kian" and age == 10:
#     print("yes")
# else:
#     print("no")

a = int(input("enter a number: "))
b = int(input("enter a number: "))

op = input("enter the op (+ - * /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("error")