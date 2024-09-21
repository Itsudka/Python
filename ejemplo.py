import tensorflow as tf
import numpy as np


model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(2, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1)
])


model.compile(optimizer='adam', loss='mean_squared_error')


x_entrenamiento = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_entrenamiento = np.array([[0], [1], [1], [0]])
model.fit(x_entrenamiento, y_entrenamiento, epochs=100)


x_prueba = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_prueba = model.predict(x_prueba)
print(y_prueba)