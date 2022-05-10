# exceptions_division_calc_try_this.py

from microbit import *

sleep(1000)

print("Division Calculation")

try:
    n = 20
    d = 5

    q = n / d

except ZeroDivisionError:
    print("Can't divide by zero.")

except TypeError:
        print("Expected a number.")

else:
    print("q = n / d")
    print("  = ", n, " / ", d)
    print("  = ", q)

finally:
    print("Try again!")
    print()