import os
import tempfile
import tensorflow as tf
import tensorflow_hub as hub

USE_URL = 'https://tfhub.dev/google/universal-sentence-encoder/4'
MODEL_NAME = 'universalencoder'
MODEL_VERSION = 1

def download_model():
    embed = hub.load(USE_URL)
    tf.saved_model.save(embed, f'./models/{MODEL_NAME}/{MODEL_VERSION}')

if __name__ == "__main__":
    download_model()
