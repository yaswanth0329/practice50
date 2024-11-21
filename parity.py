def main():
    n1 = int(input('Enter number : '))
    parity=is_parity(n1)
    print("The number is ",parity)
    
    
def is_parity(n):
    if n%2==0:
        return 'Even'
    else:
        return 'Odd'
        
main()
    