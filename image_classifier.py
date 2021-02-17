import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import tensorflow as tf
import numpy as np
from tensorflow import keras

import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(units=128, activation=tf.nn.relu),
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss = model.evaluate(test_images, test_labels)

predictions = model.predict(test_images)

# Print out prediction
print("Prediction", list(predictions[1]).index(max(predictions[1])))

# Print out correct answer
print("Correct Answer", test_labels[1])

plt.imshow(test_images[1], cmap='gray', vmin=0, vmax=255)
plt.show()

print("Done")