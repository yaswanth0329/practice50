def main():
    n=input("Enter your thoughts: ")
    if n.islower():
        print("Lowercase Alphabet")
    elif n.isupper():
        print("Uppercase Alphabet")
    else:
        print("Not valid input")
        
main()