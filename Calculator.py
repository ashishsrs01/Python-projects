# Calculator.py
import tkinter as tk
from tkinter import messagebox, scrolledtext

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


# Global variables for GUI
history = []
result_display = None
num1_entry = None
num2_entry = None
history_display = None


def calculate(operation, op_symbol):
    try:
        n1 = float(num1_entry.get())
        n2 = float(num2_entry.get())
        result = operation(n1, n2)
        result_display.config(text=f"{result:.4f}")
        operation_str = f"{n1} {op_symbol} {n2} = {result:.4f}"
        history.append(operation_str)
        update_history()
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def calculate_single(operation, op_name):
    try:
        n1 = float(num1_entry.get())
        result = operation(n1)
        result_display.config(text=f"{result:.4f}")
        operation_str = f"{op_name}({n1}) = {result:.4f}"
        history.append(operation_str)
        update_history()
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def update_history():
    history_display.config(state=tk.NORMAL)
    history_display.delete(1.0, tk.END)
    for i, record in enumerate(history[-10:], 1):
        history_display.insert(tk.END, f"{i}. {record}\n")
    history_display.config(state=tk.DISABLED)


def clear_inputs():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_display.config(text="0")


def clear_history_func():
    history.clear()
    update_history()


def create_gui():
    global result_display, num1_entry, num2_entry, history_display
    
    root = tk.Tk()
    root.title("Calculator GUI")
    root.geometry("500x600")
    root.configure(bg="#2c3e50")
    
    # Title
    title_label = tk.Label(root, text="CALCULATOR", font=("Arial", 20, "bold"), 
                          bg="#2c3e50", fg="#3498db")
    title_label.pack(pady=10)
    
    # Input frame
    input_frame = tk.Frame(root, bg="#2c3e50")
    input_frame.pack(pady=10, padx=10)
    
    tk.Label(input_frame, text="Number 1:", font=("Arial", 10), 
            bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
    num1_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
    num1_entry.pack(side=tk.LEFT, padx=5)
    
    tk.Label(input_frame, text="Number 2:", font=("Arial", 10), 
            bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
    num2_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
    num2_entry.pack(side=tk.LEFT, padx=5)
    
    # Result display
    result_frame = tk.Frame(root, bg="#2c3e50")
    result_frame.pack(pady=10, padx=10, fill=tk.X)
    
    tk.Label(result_frame, text="Result:", font=("Arial", 10), 
            bg="#2c3e50", fg="#ecf0f1").pack()
    result_display = tk.Label(result_frame, text="0", font=("Arial", 16, "bold"), 
                               bg="#34495e", fg="#2ecc71", padx=10, pady=10)
    result_display.pack(fill=tk.X)
    
    # Button frame
    button_frame = tk.Frame(root, bg="#2c3e50")
    button_frame.pack(pady=15)
    
    button_configs = [
        ("Add", lambda: calculate(add, "+")),
        ("Subtract", lambda: calculate(subtract, "-")),
        ("Multiply", lambda: calculate(multiply, "*")),
        ("Divide", lambda: calculate(divide, "/")),
        ("Power", lambda: calculate(power, "^")),
        ("Sqrt N1", lambda: calculate_single(sqrt, "sqrt")),
        ("Cbrt N1", lambda: calculate_single(cube_root, "cbrt")),
        ("Clear", clear_inputs),
    ]
    
    for i, (text, command) in enumerate(button_configs):
        row = i // 4
        col = i % 4
        btn = tk.Button(button_frame, text=text, command=command, 
                      font=("Arial", 10), width=12, bg="#3498db", fg="white",
                      activebackground="#2980b9", relief=tk.RAISED)
        btn.grid(row=row, column=col, padx=5, pady=5)
    
    # History frame
    history_label = tk.Label(root, text="History:", font=("Arial", 10, "bold"),
                            bg="#2c3e50", fg="#ecf0f1")
    history_label.pack(pady=5)
    
    history_display = scrolledtext.ScrolledText(root, height=8, width=55,
                                                 font=("Arial", 9), bg="#34495e",
                                                 fg="#2ecc71", state=tk.DISABLED)
    history_display.pack(padx=10, pady=5)
    
    # Clear history button
    clear_hist_btn = tk.Button(root, text="Clear History", command=clear_history_func,
                              font=("Arial", 9), bg="#e74c3c", fg="white",
                              activebackground="#c0392b")
    clear_hist_btn.pack(pady=5)
    
    root.mainloop()


if __name__ == "__main__":
    import os
    # Check if display is available (for GUI)
    if os.environ.get("DISPLAY") or os.name == "nt":  # nt is Windows
        try:
            create_gui()
        except:
            # If GUI fails, fall back to CLI
            calculator()
    else:
        # No display available, use CLI
        calculator()