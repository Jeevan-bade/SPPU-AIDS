import numpy as np

class ART1Network:
    def __init__(self, input_size, vigilance=0.9, learning_rate=1.0):
        """
        Initialize the ART1 network.
        
        Parameters:
        - input_size: Size of input patterns
        - vigilance: Vigilance parameter (0 < vigilance <= 1)
        - learning_rate: Learning rate (0 < learning_rate <= 1)
        """
        self.input_size = input_size
        self.vigilance = vigilance
        self.learning_rate = learning_rate
        
        # Initialize weights
        # Bottom-up weights (input to output)
        self.W = np.ones((1, input_size)) / (1 + input_size)
        # Top-down weights (output to input)
        self.T = np.ones((1, input_size))
        
        # Number of output nodes (categories)
        self.num_categories = 1
    
    def predict(self, x):
        """
        Classify the input pattern x.
        
        Returns:
        - category index or -1 if no match found
        """
        x = np.array(x)
        
        # Calculate activation for each category
        for j in range(self.num_categories):
            # Calculate bottom-up activation
            activation = np.sum(self.W[j] * x)
            
            # Calculate match with top-down weights
            match = np.sum(self.T[j] * x) / np.sum(x)
            
            # Check if meets vigilance criterion
            if match >= self.vigilance:
                # Return the first matching category
                return j
        
        # If no match found, return -1
        return -1
    
    def train(self, x):
        """
        Train the network with input pattern x.
        
        Returns:
        - category index assigned to the pattern
        """
        x = np.array(x)
        
        # Try to classify the pattern
        category = self.predict(x)
        
        if category == -1:
            # No match found - create new category
            self._add_category(x)
            return self.num_categories - 1
        else:
            # Update weights for the matching category
            self._update_weights(category, x)
            return category
    
    def _add_category(self, x):
        """Add a new category for the input pattern."""
        # Add new bottom-up weights
        new_W = self.learning_rate * x / (self.learning_rate - 1 + np.sum(x))
        self.W = np.vstack([self.W, new_W])
        
        # Add new top-down weights
        new_T = x.copy()
        self.T = np.vstack([self.T, new_T])
        
        # Increment category count
        self.num_categories += 1
    
    def _update_weights(self, category, x):
        """Update weights for an existing category."""
        # Update bottom-up weights
        self.W[category] = (self.learning_rate * x * self.T[category]) / (
            self.learning_rate - 1 + np.sum(x * self.T[category]))
        
        # Update top-down weights
        self.T[category] = x * self.T[category]

# Example usage
if __name__ == "__main__":
    # Create an ART1 network with 5 input nodes
    art = ART1Network(input_size=5, vigilance=0.8)
    
    # Training patterns (binary)
    patterns = [
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0]
    ]
    
    # Train the network
    print("Training the ART network:")
    for i, pattern in enumerate(patterns):
        category = art.train(pattern)
        print(f"Pattern {i+1}: {pattern} -> Category {category}")
    
    # Test the network
    test_pattern = [1, 0, 1, 0, 1]
    print(f"\nTesting pattern: {test_pattern}")
    category = art.predict(test_pattern)
    if category == -1:
        print("No matching category found - pattern is novel")
    else:
        print(f"Pattern belongs to category {category}")