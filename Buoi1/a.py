# bien + kieu du lieu --------------------------
a = 10

#  type casting
b = int(12.6)
print(b)  # 12

# b1 = int("12.6")
# print(b)  # error

# c = int("15,3")
# print(c)  # error

d = str(int(float("15.3")))
print(d)  # 15

# operator + logical + if - else ------------------
x = 2**3  # mu
print(x)

import math

m = math.floor(12 / 5)

y = False or True
print(y)  # true

z = True and False
print(z)  # false

age = 60
if age > 10:
    print("child")
elif age > 0:
    print("teen")
elif age > 50:
    print("old")
else:
    print("c")

# vong lap ------------------------------------
for i in range(6):
    print(i)

a = 5
while a % 2 == 0:
    print("a")


# import + main --------------------------------
def hello():
    print(__name__, "hello")

# chi khi chay file goc => name = main
# khi chay file khac => name = a
if __name__ == "__main__":
    hello()
