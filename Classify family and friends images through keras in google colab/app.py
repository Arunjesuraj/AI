#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utils import decodeImage
from prediction import predict

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = predict(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictionfamfrnd()
    return jsonify(result)


port = os.getenv("PORT")
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=5000, debug=True)


# In[5]:


get_ipython().system('pip install flask_cors')
