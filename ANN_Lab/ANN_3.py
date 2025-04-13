import numpy as np

# Input validation
while True:
    j = int(input("Enter a Number (0-9): "))
    if 0 <= j <= 9:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 9.")

# Step function
def step_function(x):
    return 1 if x >= 0 else 0 #works as activation

# Training data
training_data = [
    {'input': [1, 1, 0, 0, 0, 0], 'label': 1},
    {'input': [1, 1, 0, 0, 0, 1], 'label': 0},
    {'input': [1, 1, 0, 0, 1, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},
    {'input': [1, 1, 0, 1, 0, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 0, 1], 'label': 0},
    {'input': [1, 1, 0, 1, 1, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},
    {'input': [1, 1, 1, 0, 0, 0], 'label': 1},
    {'input': [1, 1, 1, 0, 0, 1], 'label': 0},
]

# Initialize weights randomly
weights = np.random.rand(6)

# Train the perceptron
epochs = 10
for _ in range(epochs):
    for data in training_data:
        input = np.array(data['input'])
        label = data['label']
        output = step_function(np.dot(input, weights))
        error = label - output
        weights += input * error

# Convert input number to 6-bit binary
input = np.array([int(x) for x in list('{0:06b}'.format(j))])

# Predict odd/even
output = "odd" if step_function(np.dot(input, weights)) == 0 else "even"
print(j, "is", output)