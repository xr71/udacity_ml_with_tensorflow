import tensorflow as tf
import tensorflow_hub as hub
import numpy as np 

def reload_saved_model(path_to_saved_model):
    reloaded = tf.keras.models.load_model(path_to_saved_model, custom_objects={'KerasLayer': hub.KerasLayer})

    return reloaded
