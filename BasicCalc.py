import os
import time
#from colorama import Fore, Back, Style

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
