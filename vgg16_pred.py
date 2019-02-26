


from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys
import os


#Check hierarchy
os.getcwd()


#Select filepath
#OK if the output is True
filename = "./Pictures/Camera Roll/***.jpg"
print(os.path.exists(filename))


# Load vgg16 weights
# The learned weights and the structure are loaded together
model = VGG16(weights='imagenet')
# model.summary()

# Read image
# The size is resized to 224 x 224 which is the default of VGG 16
img = image.load_img(filename, target_size=(224, 224))

# Convert PIL format image to array
x = image.img_to_array(img)

# Convert 3D tensor（rows, cols, channels) to
# 4D tensor (samples, rows, cols, channels) 
# samples = 1 
x = np.expand_dims(x, axis=0)

# Predicting the Top-5 class
# The 1000 class of VGG 16 is converted to a character string by decode_predictions ()
preds = model.predict(preprocess_input(x))
results = decode_predictions(preds, top=5)[0]
for result in results:
    print(result)
