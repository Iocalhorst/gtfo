import string
import time
import os


def clear():
    if os.name=="nt":
        os.system('cls')
    else : 
        os.system('clear')

symbols=string.printable




def main():
    number=1

    while True:
        print("Basis2=binaer, 8=oktal, 16=hex",'\n')




        for targetbase in range(2,17):
            restmenge=number
            targetexpression=""
            while (restmenge>0) :
                zaehler=restmenge%targetbase
                targetexpression+=symbols[zaehler]
                restmenge=restmenge//targetbase
            print("Basis : ",targetbase,' - > ', targetexpression[::-1])
        number+=1
        time.sleep(0.5)
        clear()

 
main()