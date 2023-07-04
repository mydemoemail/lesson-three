print("Hello!")

# 1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середньоарифметичне трьох чисел.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
user_select = int(input("Enter 1 for get min value, enter 2 for get avg: "))

if user_select == 1:
    if num1 < num2 < num3:
        print(num1)
    elif num2 < num1 < num3:
        print(num2)
    elif num3 < num1 < num2:
        print(num3)
    else:
        print("Equals!")
elif user_select == 2:
    print(f"Average: {(num1 + num2 + num3) / 3}")
else:
    print("Incorrect selection!")

#####################

