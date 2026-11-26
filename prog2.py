n_delay=int(input("ENTER NUMBER OF DAYS"))
fine=0

try:
    if(n_delay==0):
        print("No fine")
    elif(n_delay<=5):
        fine +=0.5*n_delay
    elif(n_delay<=10):
            fine+=5*n_delay
    elif(n_delay<=30):
            fine+=10*n_delay
    else:
        print("MEMBERSHIP CANCELLED")
except ValueError:
     print("ENTER A +ve number as days")

if (fine >= 0):
     print(f"Fine is {fine}")
else:
     print("no fine")          
                  


