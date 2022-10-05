"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort

        isEven = (len(numbers) % 2) == 0
        midPoint = len(numbers) // 2

        if (isEven) :
            print("is even")

            num1 = numbers[midPoint - 1]
            num2 = numbers[midPoint]

            print((num1 + num2) / 2)

        else:
            print("is odd")
            print(numbers[midPoint])


    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
