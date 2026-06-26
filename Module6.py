x = 30

if x < 30:
    print("x is less than 30")
elif x == 30:
    print("x is equal to 30")
else:
    print("x is greater than 30")

b = 30
if b <= 40 and b >= 30:
    print("b is less than 40 and b is greater than or equal 30")
elif b < 30 and b >= 20:
    print("b is less than 30 and b is greater than or equal 20")
elif b < 10:
    print("b is less than 10")
elif b < 20:
    print("b is less than 20")
else:
    print("b is some kind of number")

y = 3

if y == 7 or y == 3:
    print("y is equal to 7 or 3")

a = 20
while a < 17:
    print(a)
    a += 1

for char in "HELLO WORLD":
    print(char)

j = 20
i = "20"

print(j == i)

def hello():
    print("Hello World")
    print("Hello World")