number1 = int(input("enter your first number :- "))
number2 = int(input("enter your second number :- "))
sign = input("which operation would you like to do" + "+, /, *, - :- ")

if number1 == 45 and number2 == 3 and sign == "*":
    print("555")
elif number1 == 56 and number2 == 9 and sign == "+":
    print("77")
elif number1 == 56 and number2 == 6 and sign == "/":
    print("4")
elif sign == "+":
    number3 = number1 + number2
    print(number3)
elif sign == "-":
    number3 = number1 - number2
    print(number3)
elif sign == "*":
    number3 = number1 * number2
    print(number3)
elif sign == "/":
    number3 = number1 / number2
    print(number3)
else:
    print("your input is invalid")

