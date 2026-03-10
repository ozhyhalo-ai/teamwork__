# utils.py
def factorial(n):
    # Якщо число 0 або 1, факторіал дорівнює 1
    if n == 0 or n == 1:
        return 1
    
    # Для інших чисел множимо всі числа від 2 до n
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
