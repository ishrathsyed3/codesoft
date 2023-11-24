# calculator with simple basic arthemetic operations 
def calculator(x,y,calculation): 
    if calculation=='+':
        return x+y
    elif calculation=='*':
        return x*y
    elif calculation=='-':
        return x-y
    elif calculation=='%':
        return x%y
    elif calculation=='//':
        return x//y
    elif calculation=='/':
        if y==0:
            print("arthemetic error occured")
    else:
        return x/y
# taking  two inputs x and y 
try:
    x=float(input("enter a number:")) #first input 
    y=float(input("enter a number:")) #second input
    calculation=input("choose your operator (+,-,*,/,//,%):")
    result= calculator(x,y,calculation) 
#result
    print(f"RESULT:{result}")  #by uing f string

except ValueError:
    print("enter a valid input ")
finally:
    print("close calculator")