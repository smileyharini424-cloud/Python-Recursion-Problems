# Python Recursion Problems

## Explanation

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

Every recursive function should have a **base case** to stop the recursion.

This program demonstrates three common recursion problems:

* Factorial
* Fibonacci series
* Sum of natural numbers

## Problem Statement

Write a Python program to solve common mathematical problems using recursion.

The program should calculate:

* Factorial of a number
* Fibonacci series
* Sum of natural numbers

## Features

* Demonstrates recursion
* Uses base cases
* Calculates factorial
* Generates Fibonacci series
* Calculates sum of natural numbers
* Uses separate functions for each problem

## How It Works

### Factorial

The factorial of `n` is:

```text
n! = n × (n - 1)!
```

Base case:

```text
0! = 1
```

### Fibonacci

Each Fibonacci number is calculated as:

```text
F(n) = F(n - 1) + F(n - 2)
```

Base cases:

```text
F(0) = 0
F(1) = 1
```

### Sum of Natural Numbers

The sum is calculated as:

```text
sum(n) = n + sum(n - 1)
```

Base case:

```text
sum(0) = 0
```

## Technologies Used

* Python 3

## Data Structure Used

* Recursion
* Function call stack

## Methods Used

* `factorial()`
* `fibonacci()`
* `sum_natural()`

## Program Flow

1. Read a number from the user.
2. Calculate its factorial recursively.
3. Generate Fibonacci numbers recursively.
4. Calculate the sum of natural numbers recursively.
5. Display all results.

## Sample Input

```text
Enter a number: 5
```

## Sample Output

```text
Factorial: 120
Fibonacci Series: 0 1 1 2 3
Sum of Natural Numbers: 15
```

## Time Complexity

* Factorial: O(n)
* Fibonacci: O(2ⁿ)
* Sum of Natural Numbers: O(n)

## Space Complexity

* Factorial: O(n)
* Fibonacci: O(n)
* Sum of Natural Numbers: O(n)

## Key Learning

* Understanding recursion
* Creating base cases
* Understanding recursive calls
* Solving mathematical problems recursively
* Understanding the function call stack

## File Location

```text
Python-Recursion-Problems/recursion_problems.py
```

## Repository Structure

```text
Python-Recursion-Problems/
│
├── recursion_problems.py
└── README.md
```

## Author

V.Harini
