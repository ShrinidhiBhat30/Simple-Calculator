# Simple Expression Calculator

print("Simple Calculator")
print("Enter your math expression directly (e.g., 5+3*2)")
print("Type 'exit' to quit.\n")

while True:
    expr = input("Enter expression: ")

    if expr.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = eval(expr)  # evaluates the expression
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
