# Task 1 - Core Python Challenges
3
# 1. Sum of Two Numbers
print("1. Sum of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# 2. Odd or Even Checker
print("\n2. Odd or Even Checker")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Factorial Calculation
print("\n3. Factorial Calculation")
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)

# 4. Fibonacci Sequence
print("\n4. Fibonacci Sequence")
n = int(input("How many terms? "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 5. String Reverse
print("\n\n5. String Reverse")
text = input("Enter a string: ")
print("Reversed String:", text[::-1])

# 6. Palindrome Check
print("\n6. Palindrome Check")
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 7. Leap Year Check
print("\n7. Leap Year Check")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 8. Armstrong Number Check
print("\n8. Armstrong Number Check")
num = int(input("Enter a number: "))

order = len(str(num))
sum_val = 0

for digit in str(num):
    sum_val += int(digit) ** order

if num == sum_val:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")