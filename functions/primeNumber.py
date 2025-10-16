def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    user_input = input("Enter any number: ")
    num = int(user_input)
    if is_prime(num):
        print(f"{num} = prime number")
    else:
        print(f"{num} = not prime number")    

except ValueError:
    print("Invalid input! Please enter a valid integer number.")
