#2. Create a function named ‘check_string’, the function should
#   accept a string data from theuser and the function should check if
#   the user input contains the letter ‘s’ in it. If it contains the
#   letter ‘s’ then print- ‘The string is containing the letter ‘s’’,
#   if not then print- ‘The string doesn’t contain the letter ‘s’’.
class Solution:
    def __init__(self):
        pass
    def check_string(self,strr):
        demo=  "The string is containing the result 's'."
        if "s" in strr or "S" in strr:
              print(demo)
        else:
            print("The string doesn't contain the word 's'.")
input_str=str(input("Enter sentence :\n"))
one_str=Solution()
one_str.check_string(input_str)
#4. Create a lambda function that should double or
#   multiply the number (that we will be passing in the
#   lambda function) by 2. Store the lambda function in a
#   variable named ‘double_num’.
