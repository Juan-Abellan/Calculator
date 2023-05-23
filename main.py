from art import logo


def add(n1, n2):
    """
    Function returns the addition of n1 + n2
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Function returns the subtraction of n1 - n2
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Function returns the multiplication of n1 * n2
    """
    return n1 * n2


def divide(n1, n2):
    """
    Function returns the division of n1 / n2
    """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    still = True
    print(logo)
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    oper_start = input(f"from this operations pick one {[symbol for symbol in operations]} ")

    chosen_operation_start = operations[oper_start]
    result_start = chosen_operation_start(n1=num1, n2=num2)
    print(f"{num1} {oper_start} {num2} = {result_start}")
    result = result_start

    while still:
        another = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit. ")

        if another == "y":
            oper = input(f"Once again, from this operations pick one {[symbol for symbol in operations]} ")
            chosen_operation = operations[oper]
            num = float(input("What is your next number? "))
            new_result = chosen_operation(n1=result, n2=num)
            print(f"{result} {oper} {num} = {new_result}")
            result = new_result

        else:
            still = False
            print("Thanks for using Juaninschen-Calculator!\n")
            calculator()

    # print(f"""
    # TESTING ..........................................................................................................
    # {type(operations) = }
    # {type(oper1) = }
    # {type(operations[oper1]) = }
    # {chosen_operation1(n1= num1, n2= num2) = }
    # ......................................................................................................................
    # """)
    #
    # oper2 = input(f"Once again, from this operations pick one {[symbol for symbol in operations]} ")
    # chosen_operation2 = operations[oper2]
    # num3 = int(input("What is your third number? "))
    # result2 = chosen_operation2(n1=result1, n2=num3)
    # print(
    #     f"{result1} {oper2} {num3} = {result2}")
    # 
    # print(f"""
    # TESTING ............................................................... ..........................................
    # {type(oper2) = }
    # {type(operations[oper2]) = }
    # {chosen_operation2(n1= chosen_operation1(n1= num1, n2= num2), n2= num3) = }
    # ......................................................................................................................
    # """)


calculator()
