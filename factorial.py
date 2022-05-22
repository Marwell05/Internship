f=int(input("Enter a number "))
if (f>1):
    n = f - 1
    a = f * n
    while(n>1):
        n-=1
        a=a*n
    print("Factorial of the entered number is:",a)
elif(f<0):
    print("Factorial of negative number does not exist")
else:
    print("Factorial of the given number is : 1")