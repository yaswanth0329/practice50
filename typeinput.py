def main():
    s=input("Enter your thoughts: ")
    if s.isalpha():
        print("Alphabets")
    elif s.isdigit():
        print("Digits")
    else:
        print("Special Symbols")

main()