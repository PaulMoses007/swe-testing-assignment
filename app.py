from calculator import Calculator

calc = Calculator()

print("Quick-Calc")

a = float(input("Enter first number: "))
op = input("Operator (+,-,*,/): ")
b = float(input("Enter second number: "))

if op == "+":
    print(calc.add(a,b))
elif op == "-":
    print(calc.subtract(a,b))
elif op == "*":
    print(calc.multiply(a,b))
elif op == "/":
    try:
        print(calc.divide(a,b))
    except ValueError as e:
        print(e)
