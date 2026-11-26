#for a given main string,find all the positions of given substrings in main string

main_string="HELLO THS IS MAIN HELLO AGAIN!"
sub="HELLO"
pos=[]
x=main_string.split(" ")
print("Positions are : ",end="")
for i in range(len(x)):
    print(i,x[i])
    pos.append(i if (sub==x[i]))
print(pos)    