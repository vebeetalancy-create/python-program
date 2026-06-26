#1. Write a Python program to check whether a given number is an Armstrong number or not.

n = int(input("Enter a number: "))

num = n
digits = len(str(n))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


#2. Write a program that prints all Armstrong numbers in a given range.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Armstrong numbers are:")

for n in range(start, end + 1):
    digits = len(str(n))
    total = 0
    num = n

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    if total == n:
        print(n)
