try:
    withdraw_amt=int(input("ENTER THE AMOUNT TO DRAW"))
    if (type(withdraw_amt)==int or type(withdraw_amt)==float):
        print(f"{withdraw_amt}")

        #check den for 100
        den_hundred = (withdraw_amt) // 100
        rem_fifty=(withdraw_amt)-((den_hundred)*100)

        #check den for 50
        den_fifty = (rem_fifty) // 50
        rem_ten=(rem_fifty)-((den_fifty)*50)

        #check den for 10
        den_ten = (rem_ten) // 10

        print(f"hundred:{den_hundred} fifty:{den_fifty} ten:{den_ten}")
    else:
        print("the withdraw amt was not integer")    
except ValueError:
    print("Not Valid!")






