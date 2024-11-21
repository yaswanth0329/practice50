def main():
    a = int(input("Enter length of the triangle : "))
    b = int(input("Enter length of the triangle : "))
    c = int(input("Enter length of the triangle : "))
    if a == b == c :
        print("Equilateral Triangle ")
    elif a != b != c :
        print("Scalene Triangle ")
    else:
         print("Isosceles Triangle ")
         
main()
         
    
        