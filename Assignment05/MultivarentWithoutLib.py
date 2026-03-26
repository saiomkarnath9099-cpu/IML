def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def multiply(A,B):
    is_b_1d = isinstance(B[0], (int, float))
    if is_b_1d:
        return [sum(A[i][k] * B[k] for k in range(len(B))) for i in range(len(A))]
    else:
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
def invert_matrix(A):
    n = len(A)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    augmented = [A[i] + identity[i] for i in range(n)]
    for i in range(n):
        augmented[i] = [x / augmented[i][i] for x in augmented[i]]
        for j in range(n):
            if i != j:
                factor = augmented[j][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2*n)]
    inverse = [row[n:] for row in augmented]
    return inverse
try:
    print("Multiple Linear Regression")
    n = int(input("Enter the number of data points(rows):"))
    k = int(input("Enter the number of independent variables: "))
    print(f"\n Enter the feature for each row:")
    x = []
    for i in range(n):
        while True:
            try:
                row = list(map((float,input(f"Row {i+1}: ").split())))
                if len(row)!=k;
                    print(f"Error:Expected {k} values Please try again.")
                    continue
                x.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                while True:
                    try:
                        y = list(map(float,input("Enter the target values (y) separated by space: ").split()))
                        if len(y)!=n:
                            print(f"Error: Expected {n} values. Please try again.")
                            continue
                        break
                    XT = transpose(x)
                    XTX = multiply(XT,x)
                    XTX_inv = invert_matrix(XTX)
                    if XTX_inv is None:
                        print("Error: Matrix is singular. Cannot compute coefficients.")        
                    else:
                        XTy = multiply(XT,y)
                        coefficients = multiply(XTX_inv,XTy)
                        print("\n"+"="*30)
                        print("Final Regression Equation:")
                        equation = "y = " + " + ".join([f"{coefficients[i]:.4f}*x{i+1}" for i in range(k)])
                        print(equation)
                        print("="*30)
                        for i in range(k):
                            print(f"Coefficient (b{i+1}): {coefficients[i]:.4f}")
                        test = input("Do you want to test the regression equation? (yes/no): ")
                        if test.lower() == "yes":
                            x_test = []
                            for j in range(k):
                                while True:
                                    try:
                                        value = float(input(f"Enter value for x{j+1}: "))
                                        x_test.append(value)
                                        break
                                    except ValueError:
                                        print("Invalid input. Please enter a valid number.")
                            y_pred = sum(coefficients[i] * x_test[i] for i in range(k))
                            print(f"Predicted value of y: {y_pred:.4f}")                                                               
except ValueError:
    print("Invalid input. Please enter valid numbers.")
