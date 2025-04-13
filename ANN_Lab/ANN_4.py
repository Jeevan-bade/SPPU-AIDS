import numpy as np
import matplotlib.pyplot as plt

# Define Perceptron
class Perceptron:
    def __init__(self, input_size, lr=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.lr = lr

    def predict(self, x):
        summation = np.dot(x, self.weights) + self.bias
        return 1 if summation >= 0 else 0

    def train(self, x, y, epochs):
        for _ in range(epochs):
            for i in range(len(x)):
                prediction = self.predict(x[i])
                self.weights += self.lr * (y[i] - prediction) * x[i]
                self.bias += self.lr * (y[i] - prediction)

# Generate data
np.random.seed(0)
X = np.array([[2, 2], [4, 3], [1, 1], [3, 3], [2, 3], [4, 4]])
y = np.array([0, 0, 1, 0, 1, 0])

# Train Perceptron
perceptron = Perceptron(input_size=2)
perceptron.train(X, y, epochs=100)

# Plot decision regions
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = np.array([perceptron.predict(np.array([x, y])) for x, y in zip(xx.ravel(), yy.ravel())])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
plt.title('Perceptron Decision Regions')
plt.show()