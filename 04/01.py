# تابع جمع
def add(a, b):
    return a + b

# تابع فاکتوریل (بازگشتی)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# تابع تشخیص عدد اول
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# تابع lambda برای محاسبه مربع
square = lambda x: x ** 2

# فراخوانی توابع
result_add = add(3, 5)
print("Sum:", result_add)  # خروجی: Sum: 8

result_factorial = factorial(5)
print("Factorial:", result_factorial)  # خروجی: Factorial: 120

result_prime = is_prime(7)
print("Is Prime:", result_prime)  # خروجی: Is Prime: True

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print("Squared Numbers:", squared_numbers)  # خروجی: Squared Numbers: [1, 4, 9, 16, 25]