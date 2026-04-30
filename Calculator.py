# Calculator.py

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot Divide by 0")
    else:
        return a/b

def power(a,b):
    return a**b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    else:
        return a**0.5

def cube_root(a):
    if a < 0:
        return -(-a)**(1/3)
    else:
        return a**(1/3)


def calculator():
    print("welcome to calculator")
    print("Select Operatinons:")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Cube Root")
    print("8. Exit")

    while True:

        choice = input("Enter Choice (1-8): ")

        if choice == "8":
            print("Exiting Calculator. Goodbye!")
            break

        elif choice in ["1", "2", "3", "4", "5"]:

            n1 = float(input("Enter First Number: "))
            n2 = float(input("Enter Second Number: "))

            if choice == 1:
                print(f"{n1} + {n2} = {add(n1,n2)}")
            elif choice == 2:
                print(f"{n1} - {n2} = {subtract(n1,n2)}")
            elif choice == 3:
                print(f"{n1} * {n2} = {multiply(n1,n2)}")
            elif choice == 4:
                print(f"{n1} / {n2} = {divide(n1,n2)}")
            elif choice == 5:
                print(f"{n1} ^ {n2} = {power(n1,n2)}")
            elif choice == 6:
                print(f"sqrt({n1}) = {sqrt(n1)}")
            elif choice == 7:
                print(f"cube_root({n1}) = {cube_root(n1)}")

        else:
            print("Invalid choice. PLease select a valid opeartion (1-8).")


if __name__ == "__main__":
    calculator()