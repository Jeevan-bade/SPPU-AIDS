import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist 

(X_train, y_train), (X_test, y_test) = mnist.load_data() 
print(f'X_train shape: {X_train.shape}, X_test shape: {X_test.shape}')
from tensorflow.keras.utils import to_categorical 

# convert image datatype from integers to floats 
X_train = X_train.astype('float32') 
X_test = X_test.astype('float32') 

# normalising piel values 
X_train = X_train/255.0
X_test = X_test/255.0

# reshape images to add channel dimension 
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1) 
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1) 

# One-hot encoding label 
y_train = to_categorical(y_train) 
y_test = to_categorical(y_test)

from tensorflow.keras.utils import to_categorical 

# convert image datatype from integers to floats 
X_train = X_train.astype('float32') 
X_test = X_test.astype('float32') 

# normalising piel values 
X_train = X_train/255.0
X_test = X_test/255.0

# reshape images to add channel dimension 
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1) 
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1) 

# One-hot encoding label 
y_train = to_categorical(y_train) 
y_test = to_categorical(y_test)

plt.figure(figsize=(10,6)) 
plt.plot(history.history['accuracy'], color = 'blue', label = 'train') 
plt.plot(history.history['val_accuracy'], color = 'red', label = 'val') 
plt.legend() 
plt.title('Accuracy') 
plt.show()