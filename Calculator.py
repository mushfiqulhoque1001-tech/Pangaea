
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    print(f"Division: {a / b if b != 0 else 'undefined'}")
    print(f"Modulus: {a % b if b != 0 else 'undefined'}")
    print(f"Exponentiation: {a ** b}")
    
except ValueError:
    print("Error: Please enter valid numbers")
except Exception as e:
    print(f"An error occurred: {e}")
