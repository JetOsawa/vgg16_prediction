


from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import model_from_json
#from keras.optimizers import Adam
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
#model_filename = 'vgg16_model.json'
#weights_filename = 'vgg16_weights.h5'
#json_string = open(model_filename).read()
#model = model_from_json(json_string)
##model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001, beta_1=0.5), metrics=['accuracy'])
#model.load_weights(weights_filename)
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
