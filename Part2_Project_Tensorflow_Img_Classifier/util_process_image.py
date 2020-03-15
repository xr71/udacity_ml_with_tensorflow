import tensorflow as tf 
import numpy as np 

def process_image(img):
    image = np.squeeze(img)
    image = tf.image.resize(image, (224, 224))/255.0

    return image
