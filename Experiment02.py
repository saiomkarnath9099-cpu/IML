#1----------------->

import numpy as np
from scipy import stats
try:
    raw_x = input("Enter X values separated by sppace: ")
    raw_y = input("Enter Y value separated by spaces: ")
    
    x = [float(i) for i in raw_x.split()]
    y = [float(i) for i in raw_y.split()]

    n = len(x)

    if n!= len(y):
        print("Error:The nimber of x and y values must be same.")
    elif n<2:
        print("Error:You need at least two points to form a line.")
    else:
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x_sq = sum(x[i]**2 for i  in range(n))

        numerator = (n*sum_xy) - (sum_x*sum_y)
        denominator  = (n*sum_x_sq) - (sum_x**2)

        if denominator == 0:
            print("Error:Vertical lines detected.")
        else:
            m = numerator/denominator
            c = (sum_y/n) - (m*(sum_x/n))
            print("\n "+"-"*30)
            print(f"slope(m):{m:.4f}")
            print(f"Intercept(c):{c:.4f}")
            print(f"Equation:y = {m:.4f}x + {c:.4f}")
            print("-"*30)
except valueError:
    print("Error:Please enter only numeric values.")

    #2------------->
    import numpy as np
    from scipy import stats
    try:
        raw_x  = input("Enter X values separated by space: ")
        raw_y = input("Enter Y values separated by space: ")

        x = np.array[float(i) for i in raw_x.split()]
        y = np.array[float(i) for i in raw_y.split()]
#Linear Regression:
        print("\n"+"-"*30)
        print(f"Slope(m):{slope:.4f}")
        print(f"Intercept(c):{intercept:.4f}")
        print(f"Equation:y= {slope:.4f}x + {intercept:.4f}")
        print("-"*30)
    except valueError:
        print("Please enter only numbers separated by spaces.")
    except Exception as e:
        print(f"An error has occured.{e}")