from keras.models import load_model
import numpy as np
import cv2
from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)

#Loading the keras model
def load_mod():
    model = load_model("cats_dogs_model.hdf5")
    return model

#Resizing and reshaping the image for getting prediction
def preprocess_image(image):
    # if image in not in RGB then convert it
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = cv2.resize(image, (150, 150))
    image = image.reshape(1, 150, 150, 3)
    image = 1/255.0 * image
    return image

@app.route("/", methods=["POST"])
def index():
    filestr = request.files['file'].read()
    npimg = np.fromstring(filestr, np.uint8)
   # convert numpy array to image
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    image = preprocess_image(image)
    prediction = load_mod().predict(image)
    y_predict_in_binary = (prediction>0.5).astype(int)
    if y_predict_in_binary == 1:
        predstr = "Dog"
    elif y_predict_in_binary == 0:
        predstr = "Cat"
    pred = {'image': str(predstr)}
    return jsonify(pred)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')