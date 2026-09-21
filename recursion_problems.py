def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_natural(n):
    if n == 0:
        return 0

    return n + sum_natural(n - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    print("Factorial:", factorial(number))

    print("Fibonacci Series:", end=" ")

    for i in range(number):
        print(fibonacci(i), end=" ")

    print()

    print("Sum of Natural Numbers:", sum_natural(number))
