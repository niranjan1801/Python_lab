#EVEN NUMBER
try:
    num=int(input("ENTER A NATURAL NUMBER : "))
    if(num > 0):
        if((num) & 1):
            print("odd")
        else:
            print("EVEN")
    else:
        print("PLEASE ENTER A +ve integer")        
except ValueError:
    print("PLEASE ENTER A +ve integer(ERROR)")            