import sys
try:
    color=sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")
color.write("\n- - - - - - - - - - -WELCOME- - - - - - - - - - - - - \n","KEYWORD")

color.write(" Satnam Cafeteria\n","BUILTIN")
color.write("\n\tOur Menu : \n  CupCakes  20/- per peice \n  VegCups 10/- per peice\n ","STRING")
color.write("\nTime to add them to your cart -\n","stderr")
num=int(input("enter no. of CupCakes you want : "))
num1=int(input("enter no. of VegCups you want : "))

def cake(num):
    return (num*20)

def veg(num1):
    return (num1*10)

total=((cake(num))+(veg(num1)))

color.write("\nyour total bill= ","stderr")
print(total)

color.write("\n- - - - - - - - - - -THANK YOU- - - - - - - - - - - - - ","KEYWORD")
