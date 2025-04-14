# Import Requirements
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Hidden Layers
model = Sequential([
    Dense(64, activation='relu', input_shape=(100,)),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.summary() # Get summary

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Data for training
x_train = np.random.rand((1000, 100))
y_train = np.random.randint(2, size=(1000, 1))

model_training = model.fit(
    x_train,
    y_train,
    epochs=10,             # Number of times to iterate over the dataset
    batch_size=32,         # Number of samples per gradient update
    validation_split=0.2   # Reserve 20% of data for validation
)

x_test = np.random.rand(10, 100)  # Correct the shape here
y_test = np.random.randint(2, size=(10, 1))

loss, acc = model.evaluate(x_test, y_test)
print(f"Loss:{loss}, Accuracy:{acc}")

# input = Input(shape= (100,))
# x = Dense(64, activation='relu')(input)
# x = Dense(64, activation='relu')(x)
# output = Dense(1, activation='sigmoid')(x)

# functional_model = Model(inputs=input, outputs=output)
# functional_model.summary()

# functional_model.compile(
#     optimizer = 'adam',
#     loss = 'binary_crossentropy',
#     matrics = ['accuracy']
# )

early_stopping = EarlyStopping(monitor='loss', patience=3, verbose=1)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='early_stopping', save_best_only=True, verbose=1)

training = model.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    callbacks = [early_stopping, model_checkpoint]
)

model.save('best_model.h5')

# To import model
# -----------------

# from tensorflow.keras.models import load_model
# model = load_model('best_model.h5')

#  Evaluate the loaded model
# loaded_model.evaluate(X_test, y_test