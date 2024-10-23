#1

print("Let's find out how many days of work if three people work toghether!")

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
print(f"This means Person A takes {x} days to do their job alone \nPerson B takes {y} days \nAnd person C takes {z} days")
xy = x * y
yz = y * z
xz = x * z
xy_yz_xz = xy + yz + xz 
xyz = x * y * z
answer_ = xyz / xy_yz_xz
print(f"Person A, B and C take only {answer_} days working together!")

#2

int_1 = int(input("Enter the first integer number: "))
int_2 = int(input("Enter the second integer number: "))
int1_plus_int2 = int_1 + int_2 
int1_minus_int2 = int_1 - int_2
int1_multiplied_int2 = int_1 * int_2
int1_divided_int2 = int_1 / int_2
int1_exponet_int2 = int_1 ** int_2
int1_modulus_int2 = int_1 % int_2
int1_doubledvided_int2 = int_1 // int_2
print(int_1, "+", int_2, "=", int1_plus_int2)
print(int_1, "-", int_2, "=", int1_minus_int2)
print(int_1, "*", int_2, "=", int1_multiplied_int2)
print(int_1, "/", int_2, "=", int1_divided_int2)
print(int_1, "**", int_2, "=", int1_exponet_int2)
print(int_1, "%", int_2, "=", int1_modulus_int2)
print(int_1, "//", int_2, "=", int1_doubledvided_int2)

#3

"""Example:
 Start: a = 1 b = 2, End a = 2 b = 1
 c = a (c = 1 and a = 1)
 a = b (a = 2 and b = 2
 b = c (b=1 and c = 1"""

print("Give me two numbers")

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
print(f"This means {a} = a, and {b} = b")
c = a
a = b
b = c
print("By swapping them it becomes:")
print("a =", a, "b =", b)

#4

print("Give me two numbers")

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
print(f"This means {a} = a, and {b} = b")
a, b = b, a
print("By swapping them it becomes:")
print("a =", a, "b =", b)

#5

print("Give me three numbers")

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num1 + num2 + num3 / 3











