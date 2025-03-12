import sys
import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Error. a cannot be 0", file=sys.stderr)
        sys.exit(1)

    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return [x1, x2]
    elif D == 0:
        x = -b / (2*a)
        return [x]
    else:
        return []

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f"Error. Expected a valid real number, got {e.args[0]} instead")

if __name__ == "__main__":
    a = get_float_input("a = ")
    b = get_float_input("b = ")
    c = get_float_input("c = ")

    roots = solve_quadratic(a, b, c)
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    print(f"There are {len(roots)} roots")

    for i, root in enumerate(roots, start=1):
        print(f"x{i} = {root}")