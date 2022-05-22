num=int(input("Enter a number: "))
i=range(2,num)
if (num>1):
    for val in i:
        if(num%val)==0:
            print("The number is composite")
            break
    else:
        print("The number is prime")
else:
    print("The number is not prime")