import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural network training function
def train_neural_network(X, y, learning_rate=0.1, epochs=10000):
    input_neurons = X.shape[1]  # Number of input features
    hidden_neurons = 4  # Hidden layer neurons
    output_neurons = y.shape[1]  # Number of output neurons

    # Initialize weights and biases with random values
    hidden_weights = np.random.uniform(size=(input_neurons, hidden_neurons))
    hidden_bias = np.random.uniform(size=(1, hidden_neurons))
    output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))
    output_bias = np.random.uniform(size=(1, output_neurons))

    # Training the network over several epochs
    for _ in range(epochs):
        # Forward propagation
        hidden_layer_input = np.dot(X, hidden_weights) + hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, output_weights) + output_bias
        predicted_output = sigmoid(output_layer_input)

        # Backward propagation (calculate error and adjust weights)
        error = y - predicted_output
        d_predicted_output = error * sigmoid_derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(output_weights.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Update weights and biases
        output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
        output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
        hidden_weights += X.T.dot(d_hidden_layer) * learning_rate
        hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    return predicted_output

# Example training data: XOR problem
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])  # Inputs
y = np.array([[0], [1], [1], [0]])  # Expected outputs

# Train the neural network and get predictions
predicted_output = train_neural_network(X, y, learning_rate=0.1, epochs=10000)

# Print the predicted output after training
print("Predicted Output:\n", predicted_output)
