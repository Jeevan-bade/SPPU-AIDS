import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
from PIL import Image
import os

# 1. Data Preparation (Using synthetic data for demonstration)
def generate_synthetic_data(num_samples=1000, img_size=(128, 128)):
    """Generate synthetic images with rectangles as objects"""
    X = np.zeros((num_samples, *img_size, 3), dtype=np.float32)
    y = []
    
    for i in range(num_samples):
        # Create random background
        X[i] = np.random.rand(*img_size, 3) * 0.3
        
        # Add random rectangle (our "object")
        x1, y1 = np.random.randint(20, img_size[0]-40, 2)
        w, h = np.random.randint(20, 40, 2)
        class_id = np.random.randint(0, 3)  # 3 classes
        
        # Draw rectangle
        X[i, y1:y1+h, x1:x1+w] = [class_id/3, (class_id+1)/3, (class_id+2)/3]
        y.append([x1/img_size[0], y1/img_size[1], 
                 (x1+w)/img_size[0], (y1+h)/img_size[1], 
                 class_id])
    
    return X, np.array(y)

# 2. CNN Model Architecture for Object Detection
def build_cnn_model(input_shape=(128, 128, 3), num_classes=3):
    """Build a CNN model for object detection with bounding box regression"""
    inputs = tf.keras.Input(shape=input_shape)
    
    # Feature extraction backbone
    x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(128, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)
    
    # Flatten and create two output branches
    x = layers.Flatten()(x)
    x = layers.Dense(256, activation='relu')(x)
    
    # Classification head
    class_output = layers.Dense(num_classes, activation='softmax', name='class_output')(x)
    
    # Bounding box regression head
    box_output = layers.Dense(4, activation='sigmoid', name='box_output')(x)
    
    return tf.keras.Model(inputs=inputs, outputs=[class_output, box_output])

# 3. Training Setup
def train_model(model, X_train, y_train):
    """Compile and train the model"""
    # Split y_train into class labels and boxes
    y_train_class = y_train[:, 4].astype(int)
    y_train_box = y_train[:, :4]
    
    # Convert class labels to one-hot
    y_train_class = tf.keras.utils.to_categorical(y_train_class, num_classes=3)
    
    model.compile(
        optimizer='adam',
        loss={
            'class_output': 'categorical_crossentropy',
            'box_output': 'mean_squared_error'
        },
        metrics={
            'class_output': 'accuracy',
            'box_output': 'mse'
        },
        loss_weights={'class_output': 1., 'box_output': 1.}
    )
    
    history = model.fit(
        X_train,
        {'class_output': y_train_class, 'box_output': y_train_box},
        epochs=20,
        batch_size=32,
        validation_split=0.2
    )
    
    return history

# 4. Performance Evaluation Metrics
def evaluate_performance(model, X_test, y_test):
    """Evaluate model using various metrics"""
    # Split y_test
    y_test_class = y_test[:, 4].astype(int)
    y_test_box = y_test[:, :4]
    y_test_class_onehot = tf.keras.utils.to_categorical(y_test_class, num_classes=3)
    
    # Predictions
    pred_class, pred_box = model.predict(X_test)
    pred_class = np.argmax(pred_class, axis=1)
    
    # 1. Classification Metrics
    print("Classification Report:")
    print(classification_report(y_test_class, pred_class))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test_class, pred_class)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.show()
    
    # 2. Localization Metrics
    def calculate_iou(boxA, boxB):
        """Calculate Intersection over Union (IoU)"""
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])
        
        inter_area = max(0, xB - xA) * max(0, yB - yA)
        boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
        boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
        
        iou = inter_area / float(boxA_area + boxB_area - inter_area)
        return iou
    
    ious = [calculate_iou(y_test_box[i], pred_box[i]) for i in range(len(y_test_box))]
    avg_iou = np.mean(ious)
    print(f"\nAverage IoU: {avg_iou:.4f}")
    
    # 3. Precision-Recall at different IoU thresholds
    thresholds = [0.3, 0.5, 0.7]
    for thresh in thresholds:
        correct = sum(iou >= thresh for iou in ious)
        precision = correct / len(pred_box)
        print(f"Precision @ IoU={thresh}: {precision:.4f}")
    
    # 4. Mean Average Precision (mAP)
    # Simplified version - in practice use COCO evaluation tools
    aps = []
    for class_id in range(3):
        class_mask = (y_test_class == class_id)
        if sum(class_mask) == 0:
            continue
        class_ious = [iou for i, iou in enumerate(ious) if y_test_class[i] == class_id]
        ap = sum(iou >= 0.5 for iou in class_ious) / sum(class_mask)
        aps.append(ap)
    
    map_score = np.mean(aps) if aps else 0
    print(f"\nmAP @ IoU=0.5: {map_score:.4f}")

# 5. Visualization
def visualize_predictions(model, X_test, y_test, num_samples=3):
    """Visualize predictions with bounding boxes"""
    pred_class, pred_box = model.predict(X_test[:num_samples])
    pred_class = np.argmax(pred_class, axis=1)
    
    fig, axes = plt.subplots(1, num_samples, figsize=(15, 5))
    for i in range(num_samples):
        img = X_test[i]
        true_box = y_test[i, :4] * 128  # Scale back to pixels
        pred_box_scaled = pred_box[i] * 128
        
        axes[i].imshow(img)
        
        # True box (green)
        rect_true = patches.Rectangle(
            (true_box[0], true_box[1]),
            true_box[2] - true_box[0],
            true_box[3] - true_box[1],
            linewidth=2, edgecolor='g', facecolor='none'
        )
        axes[i].add_patch(rect_true)
        
        # Predicted box (red)
        rect_pred = patches.Rectangle(
            (pred_box_scaled[0], pred_box_scaled[1]),
            pred_box_scaled[2] - pred_box_scaled[0],
            pred_box_scaled[3] - pred_box_scaled[1],
            linewidth=2, edgecolor='r', facecolor='none', linestyle='--'
        )
        axes[i].add_patch(rect_pred)
        
        axes[i].set_title(f"True: {int(y_test[i, 4])}, Pred: {pred_class[i]}")
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Generate synthetic data
    X, y = generate_synthetic_data(num_samples=1000)
    
    # Split into train/test
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    # Build model
    model = build_cnn_model()
    model.summary()
    
    # Train
    history = train_model(model, X_train, y_train)
    
    # Plot training history
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['class_output_accuracy'], label='Class Accuracy')
    plt.plot(history.history['val_class_output_accuracy'], label='Val Class Accuracy')
    plt.title('Classification Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['box_output_mse'], label='Box MSE')
    plt.plot(history.history['val_box_output_mse'], label='Val Box MSE')
    plt.title('Bounding Box MSE')
    plt.legend()
    plt.show()
    
    # Evaluate
    evaluate_performance(model, X_test, y_test)
    
    # Visualize
    visualize_predictions(model, X_test, y_test)