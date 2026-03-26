def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def multiply(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    if colsA != rowsB:
        raise ValueError("Incompatible shapes for matrix multiplication")
    return [[sum(A[i][k] * B[k][j] for k in range(colsA)) for j in range(colsB)] for i in range(rowsA)]


def inverse_2x2(m):
    if len(m) != 2 or len(m[0]) != 2 or len(m[1]) != 2:
        raise ValueError("inverse_2x2 requires a 2x2 matrix")
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    return [[m[1][1] / det, -m[0][1] / det], [-m[1][0] / det, m[0][0] / det]]


def multivariate_regression(X, Y):
    # X: n x p matrix, Y: n x m matrix (m output variables)
    XT = transpose(X)
    XTX = multiply(XT, X)
    XTX_inv = inverse_2x2(XTX)
    XTY = multiply(XT, Y)
    return multiply(XTX_inv, XTY)


if __name__ == "__main__":
    n = int(input("Enter number of data points: "))
    m = int(input("Enter number of Y outputs: "))

    X = []
    Y = []

    print("\nEnter values:")
    for i in range(n):
        xi = float(input(f"Enter x value for row {i+1}: "))
        X.append([1.0, xi])

        y_row = []
        for j in range(m):
            yij = float(input(f"Enter y value for row {i+1}, output {j+1}: "))
            y_row.append(yij)
        Y.append(y_row)

    B = multivariate_regression(X, Y)

    print("\nRegression coefficients (including intercept):")
    for row in B:
        print(row)
