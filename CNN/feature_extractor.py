import os
import sys
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator

train_data = "/home/cdot/Desktop/Myfirst/Desktop/Myfirst/Face Images/Final Training Images"


class get_image_data:
    train_datagen = ImageDataGenerator(shear_range=0.1,
                                   zoom_range=0.1,
                                   horizontal_flip=True)
    test_datagen = ImageDataGenerator()
    training_set = train_datagen.flow_from_directory(train_data,
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='categorical')
    test_set = test_datagen.flow_from_directory(train_data,
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='categorical')
    # Printing class labels for each face 
    test_set.class_indices