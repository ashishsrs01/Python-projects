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
    print("\n" + "="*50)
    print("\033[1;36m" + "     WELCOME TO CALCULATOR".center(50) + "\033[0m")
    print("="*50 + "\n")
    print("\033[1;33mSelect Operations:\033[0m")
    print("  \033[92m1.\033[0m Add")
    print("  \033[92m2.\033[0m Subtraction")
    print("  \033[92m3.\033[0m Multiplication")
    print("  \033[92m4.\033[0m Division")
    print("  \033[92m5.\033[0m Power")
    print("  \033[92m6.\033[0m Square Root")
    print("  \033[92m7.\033[0m Cube Root")
    print("  \033[92m8.\033[0m History")
    print("  \033[91m9.\033[0m Exit")
    print()

    history = []

    while True:

        choice = input("Enter Choice (1-9): ")

        if choice == "9":
            print("\n" + "="*50)
            print("\033[1;32m" + "Exiting Calculator. Goodbye!".center(50) + "\033[0m")
            print("="*50 + "\n")
            break

        elif choice in ["1", "2", "3", "4", "5"]:
            n1 = float(input("Enter First Number: "))
            n2 = float(input("Enter Second Number: "))

            if choice == "1":
                result = add(n1, n2)
                print(f"\n  \033[92m{n1} + {n2} = {result:.2f}\033[0m")
                history.append(f"{n1} + {n2} = {result:.2f}")
            elif choice == "2":
                result = subtract(n1, n2)
                print(f"\n  \033[92m{n1} - {n2} = {result:.2f}\033[0m")
                history.append(f"{n1} - {n2} = {result:.2f}")
            elif choice == "3":
                result = multiply(n1, n2)
                print(f"\n  \033[92m{n1} * {n2} = {result:.2f}\033[0m")
                history.append(f"{n1} * {n2} = {result:.2f}")
            elif choice == "4":
                result = divide(n1, n2)
                print(f"\n  \033[92m{n1} / {n2} = {result:.2f}\033[0m")
                history.append(f"{n1} / {n2} = {result:.2f}")
            elif choice == "5":
                result = power(n1, n2)
                print(f"\n  \033[92m{n1} ^ {n2} = {result:.2f}\033[0m")
                history.append(f"{n1} ^ {n2} = {result:.2f}")

        elif choice == "6":
            n1 = float(input("Enter Number: "))
            result = sqrt(n1)
            print(f"\n  \033[92msqrt({n1}) = {result:.4f}\033[0m")
            history.append(f"sqrt({n1}) = {result:.4f}")

        elif choice == "7":
            n1 = float(input("Enter Number: "))
            result = cube_root(n1)
            print(f"\n  \033[92mcube_root({n1}) = {result:.4f}\033[0m")
            history.append(f"cube_root({n1}) = {result:.4f}")

        elif choice == "8":
            if not history:
                print("\n  \033[93mNo calculation history yet.\033[0m")
            else:
                print("\n" + "-"*50)
                print("\033[1;36m" + "Calculation History (Last 3 records)".center(50) + "\033[0m")
                print("-"*50)
                for i, record in enumerate(history[-3:], 1):
                    print(f"  \033[94m{i}.\033[0m {record}")
                print("-"*50 + "\n")
                print()

        else:
            print("Invalid choice. Please select a valid operation (1-9).")


if __name__ == "__main__":
    calculator()
