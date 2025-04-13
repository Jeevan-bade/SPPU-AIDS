import numpy as np

def mcculloch_pitts_neuron(inputs, weights, threshold):
    summation = np.dot(inputs, weights)
    return 1 if summation >= threshold else 0

def ANDNOT(x1, x2):
    # Weights and threshold for ANDNOT
    weights = [1, -1]
    threshold = 1
    return mcculloch_pitts_neuron([x1, x2], weights, threshold)

# Test ANDNOT function
print("ANDNOT(0, 0):", ANDNOT(0, 0))
print("ANDNOT(0, 1):", ANDNOT(0, 1))
print("ANDNOT(1, 0):", ANDNOT(1, 0))
print("ANDNOT(1, 1):", ANDNOT(1, 1))