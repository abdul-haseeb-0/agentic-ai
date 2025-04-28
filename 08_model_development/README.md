# 🤖 Keras: Simplified Deep Learning Framework

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Keras](https://img.shields.io/badge/Keras-✔️-green) ![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

Keras is a **high-level neural networks API** written in Python. It runs on top of backends like TensorFlow, making it simple to prototype, build, and deploy deep learning models.

## 🔹 Key Features
- **User-friendly:** Minimalistic API designed for quick experimentation.
- **Modularity:** Models are built by connecting configurable building blocks (layers, optimizers, etc.).
- **Backend Agnostic:** Supports TensorFlow, Theano, CNTK, etc.

---

## 🔧 Installation
```bash
pip install tensorflow  # TensorFlow includes Keras as tf.keras
```

---

## 🍁 Building a Model with the Sequential API

The **Sequential API** is the simplest way to build a model in Keras. It lets you stack layers linearly.

### 🔹 Example: A Simple Feedforward Neural Network
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Create a Sequential model
model = Sequential([
    Dense(64, activation='relu', input_shape=(100,)),  # Input layer
    Dropout(0.5),                                      # Dropout for regularization
    Dense(64, activation='relu'),                      # Hidden layer
    Dense(1, activation='sigmoid')                     # Output layer
])

# Display the model summary
model.summary()
```

---

## ⚙️ Compiling the Model
```python
model.compile(
    optimizer='adam',                # Optimizer to update weights
    loss='binary_crossentropy',      # Loss function for binary classification
    metrics=['accuracy']             # Evaluation metric
)
```

---

## 🏋️ Training the Model
```python
import numpy as np

# Generate dummy training data
X_train = np.random.rand(1000, 100)  # 1000 samples, each with 100 features
y_train = np.random.randint(2, size=(1000, 1))  # 1000 binary labels

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,             # Number of iterations over the dataset
    batch_size=32,         # Number of samples per gradient update
    validation_split=0.2   # Reserve 20% of data for validation
)
```

---

## 📊 Evaluating and Making Predictions

### 🔹 Evaluating the Model
```python
X_test = np.random.rand(200, 100)
y_test = np.random.randint(2, size=(200, 1))

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {test_loss}, Test accuracy: {test_accuracy}")
```

### 🔹 Making Predictions
```python
predictions = model.predict(X_test)
predicted_classes = (predictions > 0.5).astype("int32")
print(predicted_classes[:5])
```

---

## 🔄 Advanced Topic: The Functional API

The **Functional API** allows you to build more complex models, including those with multiple inputs, outputs, or non-linear topology.

### 🔹 Example: Functional API Model
```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

inputs = Input(shape=(100,))
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
outputs = Dense(1, activation='sigmoid')(x)

functional_model = Model(inputs=inputs, outputs=outputs)
functional_model.summary()

functional_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

---

## 🛠️ Callbacks and Model Checkpoints

### 🔹 Using EarlyStopping and ModelCheckpoint
```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

early_stopping = EarlyStopping(monitor='val_loss', patience=3, verbose=1)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True, verbose=1)

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping, model_checkpoint]
)
```

---

## 💾 Saving and Loading Models

### 🔹 Save and Load a Model
```python
# Save the model
model.save('my_model.h5')

# Load the model
from tensorflow.keras.models import load_model
loaded_model = load_model('my_model.h5')

# Evaluate the loaded model
loaded_model.evaluate(X_test, y_test)
```

---

🌟 **Follow for more Deep Learning tips!** 🚀