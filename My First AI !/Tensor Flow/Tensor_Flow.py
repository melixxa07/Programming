""" Fashion Dataset """

# Import libraries.
import tensorflow as tf
import numpy as np
from tensorflow import keras
# Keras is a library that allows to build neural nets
import matplotlib.pyplot as plt

# TODO: To install the tensorflow so keras can be imported  ==  DONE


# 1. IMPORT DATA: Load a pre-defined (fashion) dataset (70000 of 28x28).
fashion_mnist = keras.datasets.fashion_mnist   # We call keras documentation.

# 2. Pull out data from the Dataset:
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# Returns: 60000 of the images for training and 10000 of the images for testing.

# 3. Show Data:
print(train_labels[0])   # Display the first image from de dataset / element from the training images
#print(train_images[0])
plt.imshow(train_images[0], cmap = 'gray', vmin = 0, vmax = 255)
plt.show()

print('Code Completed!')