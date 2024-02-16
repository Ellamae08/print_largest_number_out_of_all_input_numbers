while True:
    try:
        num1 = float(input("\n\033[1;34;40mEnter the first number: "))
        num2 = float(input("\033[1;34;40mEnter the second number: "))
        num3 = float(input("\033[1;34;40mEnter the third number: "))

        if num1 >= num2 and num1 >= num3:
            largest_number = num1
        elif num2 >= num1 and num2 >= num3:
            largest_number = num2
        else:
            largest_number = num3

        if num1 == num2 == num3:
            print("\033[1;37;40mAll numbers are equal.\n")
        else:
            print("\033[1;33;40mThe largest number is:", largest_number)
            print()
        break

    except ValueError:
        print("\033[1;31;40mInvalid input. Please enter a valid number.")