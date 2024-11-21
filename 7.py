def main():
    number = int(input("Enter a number : "))
    if number % 5 == 0 and number % 3 == 0:
        print("Divisible by 5 and 3")
    elif number % 5 == 0:
        print("Divisible by 5 ")
    elif number % 3 == 0:
        print("Divisible by 3 ")
    else:
        print("Not Divisible by both 5 and 3")

main()