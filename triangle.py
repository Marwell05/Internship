user=int(input("Enter 1 to find adjacent length, 2 for opposite length & 3 for hypotenuse: \n"))
if(user==1):
    opp=int(input("Enter the opposite length: "))
    hypo=int(input("Enter the hypotenuse: "))
    adj=(((hypo**2)-(opp**2))**0.5)
    print("The length of adjacent side is:",adj)
elif(user==2):
    adj = int(input("Enter the adjacent length: "))
    hypo = int(input("Enter the hypotenuse: "))
    opp = (((hypo** 2) - (adj** 2)) ** 0.5)
    print("The length of opposite side is:", opp)
elif(user==3):
    opp = int(input("Enter the opposite length: "))
    adj = int(input("Enter the adjacent length: "))
    hypo=(((adj**2)+(opp**2))**0.5)
    print("The hypotenuse is=",hypo)
else:
    print("Enter a valid number")