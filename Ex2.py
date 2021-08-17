"""
Faulty calculator
like:- 45+3= 533, 56+9=4 , 56/6 = 2
"""
print("CALCULATOR", "\n")
print("Enter the first number")
num1 = float(input())
print("Enter the sign")
sign = input()
print("Enter the second number")
num2 = float(input())

if sign == "+":
    if num1 > 10 or num2 > 10:
        print(num1, "+", num2, "=", num1 + num2 + 3)
    else:
        print(num1, "+", num2, "=", num1 + num2)
elif sign == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif sign == "*":
    if num1 > 10 or num2 > 10:
        print(num1, "*", num2, "=", num1 * num2 * 2)
    else:
        print(num1, "*", num2, "=", num1 * num2)
elif sign == "/":
    if num1 > 10 or num2 > 10:
        print(num1, "/", num2, "=", (num1 / num2) * 2)
    else:
        print(num1, "/", num2, "=", num1 / num2)



