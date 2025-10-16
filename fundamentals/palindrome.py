#5. Take the user input string
# and check whether that string is palindrome or not.
class Check_Palindrome:
    def __init__(self):
        pass
    def is_palindrome(self):
        user_inp = input("Input anything :")
        cleand_inp=user_inp.replace(" ","").lower()
        return cleand_inp==cleand_inp[::-1]
check1=Check_Palindrome()
res=check1.is_palindrome()
if res==True:
    print(True,":Palindrome")
else:
    print(False,"Not palindrome")
