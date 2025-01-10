def calculate_factorial(n):
    if type(n) != int or n < 0:
        return "Please enter a non-negative integer"
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial