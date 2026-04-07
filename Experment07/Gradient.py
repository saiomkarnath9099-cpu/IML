import math

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Input
n = int(input("Enter the number of data points (rows): "))

x1 = []
x2 = []
y = []

print("Enter x1, x2 and y for each row:")
for i in range(n):
    a, b, c = map(float, input(f"Row {i+1}: ").split())
    x1.append(a)
    x2.append(b)
    y.append(c)

# Initialize coefficients
b0 = 0
b1 = 0
b2 = 0

learning_rate = 0.01
epochs = 1000

# Gradient Descent
for epoch in range(epochs):
    db0 = 0
    db1 = 0
    db2 = 0

    for i in range(n):
        z = b0 + b1 * x1[i] + b2 * x2[i]
        y_pred = sigmoid(z)

        error = y_pred - y[i]

        db0 += error
        db1 += error * x1[i]
        db2 += error * x2[i]

    b0 -= learning_rate * db0 / n
    b1 -= learning_rate * db1 / n
    b2 -= learning_rate * db2 / n

# Output coefficients
print("\nCalculated Coefficients:")
print(f"b0 (intercept): {b0:.4f}")
print(f"b1 (coefficient for x1): {b1:.4f}")
print(f"b2 (coefficient for x2): {b2:.4f}")

# Prediction
test = input("\nWould you like to predict a value? (y/n): ")

if test.lower() == 'y':
    t1, t2 = map(float, input("Enter new x1 and x2: ").split())
    z = b0 + b1 * t1 + b2 * t2
    prob = sigmoid(z)

    prediction = 1 if prob >= 0.5 else 0

    print(f"Predicted Probability: {prob:.4f}")
    print(f"Predicted Class: {prediction}")