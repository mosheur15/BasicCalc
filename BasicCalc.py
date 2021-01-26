# -*- coding: utf-8 -*-
# required python 3.x
from time import sleep
from string import digits 
from sys import exit
from os import system as run 
from os import get_terminal_size as term_size 
from platform import system as sysname 
#from colorama import Fore, Back, Style

col, line       = term_size()
main_header     = '<----Classic Calculator---->'
symbols         = '[ + - x / ]'
menu_header     = '____Main Menu____'
menu_option     = 'Press <num> for <func>'
os              = sysname().lower()
is_int          = lambda _str: all([(i in digits) for i in _str])
print_center    = lambda _str, col: print(_str.center(col))

def clear():
    """Clear the screen"""
    # TODO: clear screen for mac
    if os == "linux":
        run("clear")
    else:
        run("cls")

def get_input(banner):
    while True:
        try:
            print_center(banner, col)
            input1 = input('>> ')
            input2 = input('>> ')
            if ((not input1) and (not input2)) or ((not input1) or (not input2)):
                print ('invalid...')
                continue
            if ((not is_int(input1)) and (not is_int(input2)) or ((not is_int(input1)) or (not is_int(input2)))):
                print_center('Please enter valid numbers', col)
                print_center('Press enter to continue...', col)
                input()
                clear()
                continue
            return int(input1), int(input2)
        except KeyboardInterrupt:
            return 1 
        except Exception as e:
            print (f"Error: {e}")
            return 2

def addition():
    a, b = get_input("<---Addition--->")
    print (f"Result: {a+b}\n")
    print_center('Press enter to continue', col)
    input()
    
def subtraction():
    a, b = get_input("<--Subtraction-->")
    print (f"Result: {a-b}\n")
    print_center('press enter to continue', col)
    input()
    
def multiplication():
    a, b = get_input("<--Multiplication-->")
    print (f"Result: {a*b}\n")
    print_center('press enter to continue', col)
    input()
    
def divition():
    a, b = get_input("<--divition-->")
    print (f"Result: {a/b}\n")
    print_center('press enter to continue', col)
    input()
    
def floor_divition():
    a, b = get_input("<--Floor divition-->")
    print (f"Result: {a//b}\n")
    print_center('press enter to continue', col)
    input()

def main():
    while True:
        try:
            clear()
            print_center(main_header, col)
            print_center(symbols, col)
            print_center(menu_header, col)
            print('')
            print(f"[→] {menu_option.replace('<num>', '1').replace('<func>', 'Addition (+)')}")
            print(f"[→] {menu_option.replace('<num>', '2').replace('<func>', 'Subtraction (-)')}")
            print(f"[→] {menu_option.replace('<num>', '3').replace('<func>', 'Multiplication (x)')}")
            print(f"[→] {menu_option.replace('<num>', '4').replace('<func>', 'Divition (/)')}")
            print(f"[→] {menu_option.replace('<num>', '5').replace('<func>', 'Floor Divition (//)')}")
            print('')
            a = input('>> ')
            if not a: continue
            if not is_int(a):
                print_center('please enter a valid number', col)
                print_center('hit enter to continue', col)
                input()
                continue
            a = int(a)
            sleep(0.5)
            if a > 5: print ('please enter a valid number between 0-5'); input(); continue
            clear()
            if      a == 0: return 0
            elif    a == 1: addition()
            elif    a == 2: subtraction()
            elif    a == 3: multiplication()
            elif    a == 4: divition()
            else:           floor_divition()
        except KeyboardInterrupt:
            return 1 
        except Exception as e:
            print (f'Error: {e}')
            return 2
            
if __name__=="__main__":
    exit(main())





"""
os.system("mode con cols=90 lines=15")

a=25*"-"
b=40*" "
c=30*" "
heading="\n"+" "*10+a+"Classic Calculator"+a



while True:
    os.system("cls")
    print(heading)
    #print(Fore.RED+heading)
    print(b+"+ - x /"+"\n")
    
    print(c+"________Main Menu_______\n"+c+"Press 1 for addition(+)\n"+c+"Press 2 for subtraction(-)\n"+c+"Press 3 for multiplication(x)\n"+c+"Press 4 for divition in float(/)\n"+c+"Press 5 for divition in integer(//)\n"+c+"For exit press [0]")
    a=int(input(c+" "*10))
    time.sleep(0.5)
    os.system("cls")
    print(heading+"\n")
    
    try:
        if a==1:
            print(c+"_____Addition ( + )_____\n")
            input1 = int(input(c+"Enter 1st value = "))
            input2 = int(input(c+"Enter 2nd value = "))
            result = input1+input2
            print(c+"Addition is : " + str(result) )
            conti=input("\n"+c+">Press Any Key For Main Menu")
            os.system("cls")
            

        if a==2:
            print(c+"_____Subtraction ( - )_____\n")
            input1 = int(input(c+"Enter 1st value = "))
            input2 = int(input(c+"Enter 2nd value = "))
            result = input1 - input2
            print(c+"Subtraction is : " + str(result) )
            conti=input("\n"+c+">Press Any Key For Main Menu")
            os.system("cls")
        if a==3:
            print(c+"_____Multiplication ( x )_____\n")
            input1 = int(input(c+"Enter 1st value = "))
            input2 = int(input(c+"Enter 2nd value = "))
            result = input1 * input2
            print(c+"Multiplication is : " + str(result) )
            conti=input("\n"+c+">Press Any Key For Main Menu")
            os.system("cls")
        if a==4:
            print(c+"_____Division ( / )_____\n")
            input1 = int(input(c+"Enter 1st value = "))
            input2 = int(input(c+"Enter 2nd value = "))
            result = input1 / input2
            print(c+"Division is : "+ str(result) )
            conti=input("\n"+c+">Press Any Key For Main Menu")
            os.system("cls")
        if a==5:
            print(c+"_____Floor Division ( // )_____\n")
            input1 = int(input(c+"Enter 1st value = "))
            input2 = int(input(c+"Enter 2nd value = "))
            result = input1 // input2
            print(c+"Division is : "+ str(result) )
            conti=input("\n"+c+">Press Any Key For Main Menu")
            os.system("cls")

        if a==0:
            print(c+"         Thank you,Bye")
            time.sleep(2)
            break
    except Exception as e:
            os.system("cls")
            print(heading)
            print(c+"[x] You entered invalid input \n")
            time.sleep(1.5)
"""