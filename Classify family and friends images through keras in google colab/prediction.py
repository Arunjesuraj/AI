#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class predict:
    def __init__(self,filename):
        self.filename =filename


    def predictionfamfrnd(self):
        # load model
        classifier = load_model('classifier.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)

        if result[0][0] >=0.5:
            prediction = 'Friends'
            return [{ "image" : prediction}]
        else:
            prediction = 'Family'
            return [{ "image" : prediction}]


