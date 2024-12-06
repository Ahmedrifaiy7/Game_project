# exercise2

#1
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]
print(squared_list)

#2
n = int(input("Enter the number of terms: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(f"Fibonacci series: {fibonacci[:n]}")

#3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = [x for x in range(start, end + 1) if is_prime(x)]
print(f"Prime numbers between {start} and {end}: {primes}")

#4
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#5
import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print(calendar.month(year, month))

#6
import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are real and different: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The roots are real and equal: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print(f"The roots are complex: {real_part} ± {imaginary_part}i")

