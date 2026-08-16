def factorial(num):
    """Calculate the factorial of a number."""
    x = 1
    for i in range(1, num + 1):
        x *= i
    return x