def main():
    n=int(input("Enter your number : "))
    if n % 5 == 0 and n % 11 == 0:
        print("Divisible by 5 and 11")
    else:
        print("Not Divisible by 5 and 11")
     
main()