def main():
    n1 = int(input('Enter number 1 : '))
    n2 = int(input('Enter number 2 : '))
    n3 = int(input('Enter number 3 : '))
    result = add(n1,n2,n3)
    print("The sum of three numbers are : ",result)
    
def add(a,b,c):
    result = a + b + c
    return result
    
main()