# for i in range(3):
#     print(i, "hello")
#     print("blalalal")


# for i in range(5):
#     x = int(input("enter a number: "))
#     if x % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")


x = 0

# for i in range(5):
#     n = float(input("enter a number: "))
#     # x = x + n
#     x += n
# print(x)

import turtle
turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("green")

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.done()