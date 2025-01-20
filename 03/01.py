# شرط‌ها
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# حلقه for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# حلقه while
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# کنترل جریان
for i in range(10):
    if i == 5:
        break
    print(i)

# تمرین ۱: بررسی مثبت، منفی یا صفر
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# تمرین ۲: مربع اعداد ۱ تا ۱۰
for i in range(1, 11):
    print(f"{i}^2 = {i ** 2}")

# تمرین ۳: فاکتوریل
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} is {factorial}")

# تمرین ۴: اعداد فرد بین ۱ تا ۲۰
for i in range(1, 21):
    if i % 2 != 0:
        print(i)