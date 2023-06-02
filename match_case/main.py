# score = 11
# if score < 10:
#     print("fail")
# else:
#     print("pass")

number = int(input("Enter a number: "))

match number:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    case _:
        print("Unvalid data. Please enter number btween 1 - 7")

