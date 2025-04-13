import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initialize the neural network with random weights
        
        Parameters:
        - input_size: number of input features
        - hidden_size: number of neurons in hidden layer
        - output_size: number of output neurons
        """
        # Initialize weights with random values
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
        
    def sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        """Derivative of sigmoid function"""
        return x * (1 - x)
    
    def forward(self, X):
        """Forward propagation"""
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, output, learning_rate):
        """Backward propagation"""
        m = X.shape[0]  # number of samples
        
        # Calculate error at output layer
        self.output_error = output - y
        self.output_delta = self.output_error * self.sigmoid_derivative(output)
        
        # Calculate error at hidden layer
        self.hidden_error = np.dot(self.output_delta, self.W2.T)
        self.hidden_delta = self.hidden_error * self.sigmoid_derivative(self.a1)
        
        # Update weights and biases
        self.W2 -= learning_rate * np.dot(self.a1.T, self.output_delta) / m
        self.b2 -= learning_rate * np.sum(self.output_delta, axis=0, keepdims=True) / m
        self.W1 -= learning_rate * np.dot(X.T, self.hidden_delta) / m
        self.b1 -= learning_rate * np.sum(self.hidden_delta, axis=0, keepdims=True) / m
    
    def train(self, X, y, epochs=1000, learning_rate=0.1, verbose=False):
        """Train the neural network"""
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)
            
            # Backward pass
            self.backward(X, y, output, learning_rate)
            
            # Print loss every 100 epochs
            if verbose and epoch % 100 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
    
    def predict(self, X):
        """Make predictions"""
        output = self.forward(X)
        return np.round(output)

# Example usage
if __name__ == "__main__":
    # Generate synthetic data
    X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
    y = y.reshape(-1, 1)  # Reshape for neural network
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Create and train neural network
    nn = NeuralNetwork(input_size=10, hidden_size=5, output_size=1)
    nn.train(X_train, y_train, epochs=1000, learning_rate=0.1, verbose=True)
    
    # Make predictions
    y_pred = nn.predict(X_test)
    
    # Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nTest Accuracy: {accuracy:.4f}")