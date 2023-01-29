def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def conjecture(number):
    while number != 1:
        number = collatz(number)
        print(number)

try:
    number = int(input("Enter a number: "))
    conjecture(number)
except ValueError:
    print("Invalid input. Enter a valid integer.")

    
