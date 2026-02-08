# names = ["kian", "sepehr", "armin"] 

# i = 0

# while i < len(names):
#     print(names[i])
#     i += 1


# names = []

# while True:
#     n = input("enter the name: ")
#     names.append(n)
#     if input("Do you want to quit? y or n: ") == "y":
#         break
# print(names)


# for i in range(5, 0, -1):
#     print(i)

# i = 5
# while i > 0:
#     print(i)
#     i -= 1


import turtle

colors = ["red", "green", "blue", "purple", "black", "brown", "pink", "yellow"]
print(len(colors))
print(colors[0])
print(colors[-1])
for c in colors:
    print(c)
turtle.pensize(3)
for i in range(8):
    turtle.color(colors[i])
    turtle.fd(60)
    turtle.left(360/8)

turtle.done()