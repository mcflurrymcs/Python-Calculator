import os
import time
from math import *


def clear():
    os.system('cls')


def remainder():
    x = int(input("Input the number to find the remainder of: "))
    y = int(input("Input the number to divide the remainded number by: "))
    z = x % y

    print("The remainder of %d and %d is: %d" % (x, y, z))
    asthma()


def useagain():
    a = input("Do you want to use this calc again?\nType 'menu' to go back to the main menu: ")
    if a == "yes":
        clear()
        idkbruhwtf()
    elif a == "no":
        clear()
        self_destruct()
    elif a == "menu":
        clear()
        very_start()
    else:
        clear()
        useagain()


def idkbruhwtf():
    a = int(input("Please input the action you wanna do (1 or 2): \n 1: square root 2: logarithm on base 2: "))
    if a == 1:
        clear()
        squareRoot()
    if a == 2:
        clear()
        log2R()


def mainchoices():
    aks = int(input("Please input what calculator to use (1 or 2): "))
    if aks == 1:
        clear()
        idkbruhwtf()
    elif aks == 2:
        clear()
        inputs()


def log2R():

    x = float(input("Please input the number to log on base 2: "))
    if x <= 0:
        print("You can't get the logarithm of a number under zero!!!")
        d = input("Press enter to continue")
        clear()
        log2R()
    z = log2(x)
    print(z)
    a = input("Press enter to continue: ")
    clear()
    useagain()


def squareRoot():
    x = int(input("Please input the square root you want to find the result of: "))
    if x <= 0:
        print("You can't get the (square) root of a number under zero!")
        d = input("Press enter to continue")
        clear()
        squareRoot()
    z = sqrt(x)
    print(z)
    a = input("Press enter to continue: ")
    clear()
    useagain()



def self_destruct():
    clear()
    print("SELF DESTRUCTION IN...")
    for x in range(5, 0, -1):
        print(x)
        time.sleep(1)
    print("SELF DESTRUCTION BOOM")
    time.sleep(0.5)
    exit()


def specific_enter():
    entering = input("Press enter to continue: ")
    if entering == "":
        clear()
        very_start()
    else:
        clear()
        print("Bro can't even read :skull:")
        time.sleep(0.5)
        specific_enter()


def very_start():
    ask = input("Start? (type 'list' for list of options \nor type exp to type your own expression): ").lower()
    if ask == "list":
        clear()
        lists()
    elif (ask == "rmndr") or (ask == "remainder"):
        clear()
        remainder()
    elif (ask == "sqrt") or (ask == "square root"):
        clear()
        squareRoot()
    elif (ask == "log") or (ask == "logarithm"):
        clear()
        log2R()
    elif (ask == "yes") or (ask == "y"):
        clear()
        mainchoices()
    elif ask == "qcl":
        exit()
    elif (ask == "n") or (ask == "no") or (ask == "c"):
        self_destruct()
    elif ask == "exp":
        clear()
        expression()
    else:
        clear()
        very_start()


def lists():
    print('''            1.Addition "+"
             2.Subtraction "-"
             3.Multiplication "*"
             4.Division "/"
             5.Powers "^" or "**"
             6.Find percentage of the number out of the Whole "%"
             7."%" of whole = int(number) "%of"
             ''')
    entering = input("Press enter to go back to the main menu: ")
    if entering == "":
        clear()
        very_start()
    else:
        clear()
        lists()


def asthma():
    enter = input("Press enter to continue: ")
    if enter == "":
        clear()
        again()
    else:
        clear()
        asthma()


def calc_num1():
    global num1
    try:
        num1 = float(input("Input the first number: "))
    except ValueError:
        clear()
        print("Please use Numbers to calculate not words!\n")
        time.sleep(0.5)
        calc_num1()


def calc_num2():
    global num2
    try:
        num2 = float(input("Input the second number: "))
    except ValueError:
        clear()
        print("Please use Numbers to calculate not words!\n")
        time.sleep(0.5)
        calc_num2()


def operating():
    global Operator
    Operator = input("Operator: ")
    while Operator not in Options:
        clear()
        operating()


def operation():
    global result, num1, num2
    if (Operator == "+") or (Operator == "1"):
        result = num1 + num2
        clear()
        print("Result:", result)

    elif (Operator == "-") or (Operator == "2"):
        result = num1 - num2
        clear()
        print("Result:", result)
    elif (Operator == "*") or (Operator == "3"):
        result = num1 * num2
        clear()
        print("Result:", result)
    elif (Operator == "/") or (Operator == "4"):
        try:
           result = num1 / num2
        except ZeroDivisionError:
            clear()
            print("You can't divide by Zero dummy!")
            again()
        clear()
        print("Result:", result)
    elif (Operator == "**") or (Operator == "5") or (Operator == "^"):
        result = num1 ** num2
        clear()
        print("Result:", result)
    elif (Operator == "%") or (Operator == "6"):
        result = 100 * num1/num2
        clear()
        print(num1, "out of", num2, "is", float(result))
    elif (Operator == "%of") or (Operator == "7"):
        result = (num1 / 100) * num2
        clear()
        print(num1, "% of", num2, "is", float(result))


def inputs():
    calc_num1()
    operating()
    calc_num2()
    operation()
    num1 = result
    print("")
    asthma()


def second():
    operating()
    calc_num2()
    operation()
    num1 = result
    print("")
    asthma()


def enters():
    check = input("Press enter to continue: ")
    if check == "":
        clear()
        expmenu()
    else:
        enters()


def expression():

    a = input("Expression: ")
    try:
        print(eval(a))
        enters()
    except ZeroDivisionError:
        clear()
        print("You can't divide by zero dummy!")
        expression()
    except NameError:
        clear()
        print("Please type an expression not random gibberish!")
        expression()
    except SyntaxError:
        clear()
        print("Please type an expression not random gibberish!")
        expression()


def expmenu():
    use_again = input("Do you want to use the expression calc again?\nType 'menu' to go back to the main menu: ").lower()
    if (use_again == "yes") or (use_again == "y"):
        clear()
        expression()
    elif (use_again == "no") or (use_again == "n"):
        self_destruct()
    elif use_again == "menu":
        clear()
        very_start()


def again():
    global play_again
    play_again = input('''Do you want to use the calculator again?\nType 'menu' to go back to the main menu\n
Or type 'amogus' to operate with the result: ''').lower()
    if (play_again == "yes") or (play_again == "y"):
        clear()
        inputs()
    elif play_again == "menu":
        clear()
        very_start()
    elif play_again == "amogus":
        clear()
        second()
    elif play_again == "list":
        clear()
        lists()
    elif play_again == "qcl":
        exit()
    elif (play_again == "n") or (play_again == "no") or (play_again == "c"):
        self_destruct()
    else:
        clear()
        again()


Options = ["+", "-", "*", "/", "1", "2", "3", "4", "5", "6", "**", "^", "%", "%of", "7"]


while True:
    very_start()
