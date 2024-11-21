def main():
    n1 = int(input('Enter your number: '))
    n2 = int(input('Enter your number: '))
    result = add(n1,n2)
    print("The sum of two numbers is : ",result)
    
def add(a,b):
   result = a + b
   return result
   
main()
   