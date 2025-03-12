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