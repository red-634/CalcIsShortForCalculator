import math
import time
from calculationfunctions import add, subtract, multiply, divide, power, square_root, cube_root, log, cosine, sine, tangent, inverse_cosine, inverse_sine, inverse_tangent

num1 = float()
num2 = float()
base = float()
exponent = float()
num = float()
angle = float()
value = float()

def show_menu():
    print("\n--- Calc? ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Cube Root")
    print("8. Logarithm")
    print("9. Cosine")
    print("10. Sine")
    print("11. Tangent")
    print("12. Inverse Cosine")
    print("13. Inverse Sine")
    print("14. Inverse Tangent")
    print("15. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("You chose Addition, loading...")
            time.sleep(1)
            add(num1, num2)
            time.sleep(1)

        elif choice == "2":
            print("You chose Subtraction, loading...")
            time.sleep(1)
            subtract(num1, num2)
            time.sleep(1)

        elif choice == "3":
            print("You chose Multiplication, loading...")
            time.sleep(1)
            multiply()
            time.sleep(1)

        elif choice == "4":
            print("You chose Division, loading...")
            time.sleep(1)
            divide(num1, num2)
            time.sleep(1)

        elif choice == "5":
            print("You chose Power, loading...")
            time.sleep(1)
            power(base, exponent)
            time.sleep(1)
            

        elif choice == "6":
            print("You chose Square Root, loading...")
            time.sleep(1)
            square_root(num)
            time.sleep(1)

        elif choice == "7":
            print("You chose Cube Root, loading...")
            time.sleep(1)
            cube_root(num)
            time.sleep(1)

        elif choice == "8":
            print("You chose Logarithm, loading...")
            time.sleep(1)
            log(num, base)
            time.sleep(1)

        elif choice == "9":
            print("You chose Cosine, loading...")
            time.sleep(1)
            cosine(angle)
            time.sleep(1)

        elif choice == "10":
            print("You chose Sine, loading...")
            time.sleep(1)
            sine(angle)
            time.sleep(1)

        elif choice == "11":
            print("You chose Tangent, loading...")
            time.sleep(1)
            tangent(angle)
            time.sleep(1)

        elif choice == "12":
            print("You chose Inverse Cosine, loading...")
            time.sleep(1)
            inverse_cosine(value)
            time.sleep(1)

        elif choice == "13":
            print("You chose Inverse Sine, loading...")
            time.sleep(1)
            inverse_sine(value)
            time.sleep(1)

        elif choice == "14":
            print("You chose Inverse Tangent, loading...")
            time.sleep(1)
            inverse_tangent(value)
            time.sleep(1)

        elif choice == "15":
            print("Exiting the calculator. Goodbye!")
            time.sleep(1)
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()