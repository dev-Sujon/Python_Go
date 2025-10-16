def evenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Take input from user
user_input = input("Enter any number: ")
# Check if input is a valid number
if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    num = int(user_input)
    print(f"The number {num} is {evenOdd(num)}.")
else:
    print("Invalid input! Please enter a valid integer number.")


