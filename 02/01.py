# تعریف متغیرهای عددی
age = 25                  # عدد صحیح (int)
height = 1.75             # عدد اعشاری (float)

# تعریف متغیرهای رشته‌ای
name = "Ali"              # رشته (str)
message = 'Hello, World!' # رشته (str)

# تعریف متغیرهای بولین
is_student = True         # بولین (bool)
is_working = False        # بولین (bool)

# تعریف لیست
fruits = ["apple", "banana", "cherry"]  # لیست (list)

# تعریف تاپل
coordinates = (10.0, 20.0)              # تاپل (tuple)

# تعریف دیکشنری
person = {"name": "Ali", "age": 25, "is_student": True}  # دیکشنری (dict)

# تعریف مجموعه
unique_numbers = {1, 2, 3, 4, 5}       # مجموعه (set)


# عملیات روی اعداد
a = 10
b = 3
sum_result = a + b          # جمع
difference = a - b          # تفریق
product = a * b             # ضرب
quotient = a / b            # تقسیم
power = a ** b              # توان
remainder = a % b           # باقیمانده

# عملیات روی رشته‌ها
greeting = "Hello"
name = "Ali"
full_message = greeting + " " + name  # الحاق رشته‌ها
repeated_message = greeting * 3       # تکرار رشته

# عملیات روی لیست‌ها
fruits.append("orange")               # اضافه کردن به لیست
first_fruit = fruits[0]               # اندیس‌گذاری
sliced_fruits = fruits[1:3]           # برش لیست

# عملیات روی دیکشنری
person["height"] = 1.75               # اضافه کردن کلید-مقدار جدید
person_age = person["age"]            # دسترسی به مقدار یک کلید

# عملیات روی مجموعه
unique_numbers.add(6)                 # اضافه کردن به مجموعه
unique_numbers.remove(1)              # حذف از مجموعه



# چاپ متغیرها
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Is Working:", is_working)
print("Fruits:", fruits)
print("Coordinates:", coordinates)
print("Person:", person)
print("Unique Numbers:", unique_numbers)

# چاپ نتایج عملیات روی اعداد
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Power:", power)
print("Remainder:", remainder)

# چاپ نتایج عملیات روی رشته‌ها
print("Full Message:", full_message)
print("Repeated Message:", repeated_message)

# چاپ نتایج عملیات روی لیست‌ها
print("First Fruit:", first_fruit)
print("Sliced Fruits:", sliced_fruits)

# چاپ نتایج عملیات روی دیکشنری
print("Person Age:", person_age)
print("Updated Person:", person)

# چاپ نتایج عملیات روی مجموعه
print("Updated Unique Numbers:", unique_numbers)