def main():
    n=int(input("Enter number : "))
    print("The number is",nature(n))

def nature(a):
    if a > 0:
        return "Positive"
    elif a < 0:
        return "Negative"
    else:
        return "Zero"
main()