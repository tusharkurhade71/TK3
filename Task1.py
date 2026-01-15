def factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial
n = int(input(f"Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")
