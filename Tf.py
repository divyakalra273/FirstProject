# Import the library

import tensorflow as tf

from keras.preprocessing.image import ImageDataGenerator

from keras.layers import Convolution2D, Flatten, Dense, MaxPooling2D

from keras.models import Sequential



train_image_generator = ImageDataGenerator(1./255)

test_image_generator = ImageDataGenerator(1./255)

classes = ['cats', 'dogs']
batch_size = 128
epochs = 20

train_images = train_image_generator.flow_from_directory(directory = 'training_images',
                                                         target_size = (128, 128),
                                                         batch_size = 32,
                                                         class_mode = 'binary',
                                                         classes = classes,
                                                         shuffle = True
                                                         )

test_images = train_image_generator.flow_from_directory(directory = 'testing_images',
                                                         target_size = (128, 128),
                                                         batch_size = 32,
                                                         class_mode = 'binary',
                                                         classes = classes
                                                         )
sample_train_images, y_train = next(train_images)


model = Sequential()
model.add(Convolution2D(filters = 16, kernel_size = 3, activation = 'relu',
                        padding = 'same', input_shape = (128, 128, 3)))

model.add(MaxPooling2D())

model.add(Convolution2D(filters = 32, kernel_size = 3, activation = 'relu',
                        padding = 'same'))

model.add(MaxPooling2D())

model.add(Convolution2D(filters = 64, kernel_size = 3, activation = 'relu',
                        padding = 'same'))

model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(units = 512, activation = 'relu'))
model.add(Dense(units = 1))

model.compile(optimizer = 'adam',
              loss = tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics = ['accuracy'])

model.summary()



history = model.fit_generator(generator = train_images,
                              steps_per_epoch = 8000,
                              epochs = epochs,
                              validation_data = test_images,
                              validation_steps = 2000)