import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np

x_train = np.random.random((1000, 100))
y_train = np.random.randint(2, size=(1000, 1))

model = Sequential([
    Dense(64, activation="relu", input_shape=(100,)),
    Dense(64, activation="relu"),
    Dropout(0.5),
    Dense(1, activation="sigmoid"),  # Change this line
])

model.summary()

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=10,             # Number of times to iterate over the dataset
    batch_size=32,         # Number of samples per gradient update
    validation_split=0.2   # Reserve 20% of data for validation
)

x_test = np.random.rand(10, 100)  # Correct the shape here
y_test = np.random.randint(2, size=(10, 1))

loss, acc = model.evaluate(x_test, y_test)
print(f"Loss:{loss},Accuracy:{acc}")