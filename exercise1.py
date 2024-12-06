# exercise1

#1
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print(f"The sum is: {a + b}")

#2
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print(f"The maximum is: {max(a, b)}")

#3
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print(f"The maximum is: {max(a, b, c)}")

#4
n = int(input("Enter the number of elements: "))
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
print(f"The maximum is: {max(numbers)}")

#5
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

#6
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

#7
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
average = (a + b + c) / 3
print(f"The average is: {average}")

#8
x = float(input("Enter the value of x: "))
t = float(input("Enter the value of t: "))
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
y = float(input("Enter the initial value of y: "))  # Example initial value of y
result = (x * (t + y)**2) / (a + b)
print(f"The result is: {result}")

#9
gpa = float(input("Enter the GPA (0–4): "))
if 0 <= gpa < 2:
    grade = "F"
elif 2 <= gpa < 2.5:
    grade = "D"
elif 2.5 <= gpa < 3:
    grade = "C"
elif 3 <= gpa < 3.5:
    grade = "B"
elif 3.5 <= gpa <= 4:
    grade = "A"
else:
    grade = "Invalid GPA"
print(f"The letter grade is: {grade}")
