def add(a,b):
    c = a + b
    return(c)
    
def sub(a,b):
    c = a - b
    return(c)

def multi(a,b):
    c = a * b
    return(c)

def div(a,b):
    c = a/b
    return(c)

print("\nOptions: \n")
print("A -> Add")
print("B -> Sub")
print("C -> Multiply")
print("D -> Division")

choice = input("\nSelect one option from above: ")

if choice == "a" or choice == "A":

    a = int(input("\nEnter your first value: "))
    b = int(input("\nEnter your second value: "))
    c = add(a,b)
    print(f"\nAnswer of {a} + {b} is {c}\n")

elif choice == "b" or choice == "B":

    a = int(input("\nEnter your first value: "))
    b = int(input("\nEnter your second value: "))
    c = sub(a,b)
    print(f"\nAnswer of {a} - {b} is {c}")

elif choice == "c" or choice == "C":

    a = int(input("\nEnter your first value: "))
    b = int(input("\nEnter your second value: "))
    c = multi(a,b)
    print(f"\nAnswer of {a} x {b} is {c}")
    
elif choice == "d" or choice == "D":

    a = int(input("\nEnter your first value: "))
    b = int(input("\nEnter your second value: "))
    c = div(a,b)
    print(f"\nAnswer of {a} ÷ {b} is {c}")

else:
    print("\nEnter Valid input from above !!! \n")