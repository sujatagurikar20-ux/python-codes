# Program to demonstrate different operators in Python

a = 15
b = 4

# Arithmetic operators
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)
print("Floor Division =", a // b)
print("Remainder =", a % b)
print("Power =", a ** b)

# Comparison operators
print("\nComparison:")
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Logical operators
print("\nLogical:")
print(a > 10 and b < 10)
print(a < 10 or b < 10)
print(not(a > b))

# Assignment operators
x = 10
x += 5
print("\nAfter += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

# Bitwise operators
print("\nBitwise:")
print("AND =", a & b)
print("OR =", a | b)
print("XOR =", a ^ b)
print("Left Shift =", a << 1)
print("Right Shift =", a >> 1)

# Membership operators
numbers = [10, 15, 20, 25]
print("\nMembership:")
print(15 in numbers)
print(30 not in numbers)

# Identity operators
p = numbers
q = numbers

print("\nIdentity:")
print(p is q)
print(p is not q)

