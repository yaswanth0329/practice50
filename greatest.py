def main():
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))
    c = int(input("Enter number : "))
    greatest=greatest_number(a,b,c)
    print(f"The greatest number is {greatest}")

def greatest_number(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3 
        
main()
    
    
    
   