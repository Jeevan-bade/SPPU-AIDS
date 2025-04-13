import numpy as np

# Sigmoid Activation Function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# XOR Inputs and Outputs
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Input values (4 samples)
y = np.array([[0], [1], [1], [0]]) # XOR Output (4 samples)

# Initialize the weights randomly with mean 0
np.random.seed(1)

input_layer_neurons = 2 # Number of input neurons
hidden_layer_neurons = 4 # Number of hidden neurons
output_layer_neurons = 1 # Number of output neurons

# Weights between input and hidden layer
weights_input_hidden = np.random.uniform(low=-1, high=1, size=(input_layer_neurons,hidden_layer_neurons))
# Weights between hidden and output layer
weights_hidden_output = np.random.uniform(low=-1, high=1,size=(hidden_layer_neurons, output_layer_neurons))

# Learning rate
learning_rate = 0.1
# Number of epochs (iterations)
epochs = 10000
# Training the neural network using Backpropagation
for epoch in range(epochs):
    # Forward Propagation
    # Input to hidden layer
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    # Hidden to output layer
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output_layer_output = sigmoid(output_layer_input)
    # Backpropagation (Calculate the error)
    error = y - output_layer_output
    # Calculate the derivative of the error w.r.t output
    d_output = error * sigmoid_derivative(output_layer_output)

    # Calculate the derivative of the error w.r.t hidden layer
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    # Update the weights
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
    # Optional: Print the error at intervals to monitor the learning progress

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")

# After training, the network is ready to make predictions
print("Trained Output for XOR:")
print(output_layer_output)