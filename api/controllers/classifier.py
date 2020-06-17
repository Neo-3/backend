from api import app, jsonify, request
from PIL import Image
import numpy as np
import pandas as pd
import pickle
import os
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input

# Get upload dir
upload_path = os.path.join(os.path.dirname(__file__), '../uploads')

# Open and load Random Forest model
infile = open(os.path.join(os.path.dirname(__file__), '../models/model.pkl'), 'rb')
model = pickle.load(infile)
infile.close()

# Create VGG16 model
image.LOAD_TRUNCATED_IMAGES = True 
vgg16 = VGG16(weights='imagenet', include_top=False)


@app.route("/api/v1/classifier", methods=["POST"])
def classifier():
    file = None
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_path,filename))
       
        # Preprocess Image to fit in the Model
        img = image.load_img(upload_path+"/"+filename, target_size=(256, 256))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)

        feat = np.array(vgg16.predict(img_data))

        df_img = pd.DataFrame([feat.flatten()])

        df_img = df_img[[1109, 1111, 1621, 1623, 2133, 4693, 4695, 5193, 5207, 5319, 8683, 8777, 9170, 9200, 9289, 9392, 9636,
                    9692, 10148, 10204, 10660, 10825, 11760, 12754, 12779, 13266, 13385, 13732, 13788, 14244, 14756, 14921,
                    15268, 16875, 16969, 17316, 17481, 17591, 17690, 17723, 17828, 17852, 17870, 17884, 18103, 18202, 
                    18340, 18615, 18714, 18747, 18852, 19226, 19364, 21687, 21924, 21948, 22199, 22436, 22460, 22711, 
                    22810, 22948, 22972, 23004, 23460, 23484, 23739, 25230, 25275, 25742, 26254, 26556, 27068]]

        # Predict Image
        prediction = model.predict(df_img) 

        if prediction[0] == 1:
            return jsonify({'msg': 'succes', 'prediction': "True"})
        else:
            return jsonify({'msg': 'succes', 'prediction': "False"})
