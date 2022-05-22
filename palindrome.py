user_in=input("Enter a word ")
user_in=user_in.upper()
reverse_user_in=list(user_in)
reverse_user_in.reverse()
i=range(0,len(user_in))
for val in i:
    if(user_in[val]==reverse_user_in[val]):
        print("Given word is a palindrome")
        break
    else:
        print("Given word is not a palindrome")
        break