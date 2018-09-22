
#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#
# Created by Deuse 16.09.18
#
#
#

from skimage import io
from scipy.spatial import distance
import dlib
import numpy
import os



class Analyzer:

    def __init__(self, input_image, input_dirname):
        self.input_image = input_image
        self.input_dirname = input_dirname
        self.images = []

        #load trained models
        self.sp = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
        self.facerec = dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat')
        self.detector = dlib.get_frontal_face_detector()

        #load images and creating a descriptor of input image
        self.load()
        self.prepare()


    def load(self):
        for img in os.listdir(self.input_dirname):
           self.images.append(self.input_dirname + img)

        return self


    def prepare(self):
        self.input_img = io.imread(self.input_image)
        self.input_dets = self.detector(self.input_img, 1)

        for d in self.input_dets:
            self.input_shape = self.sp(self.input_img, d)
            self.input_face_descriptor = self.facerec.compute_face_descriptor(self.input_img,self.input_shape)
        return self

    def detect(self):
        concurrences = []

        for image in self.images:
            img = io.imread(image)
            try:
                dets = self.detector(img, 1)
                for d in dets:
                    shape = self.sp(img, d)
                    face_descriptor = self.facerec.compute_face_descriptor(img, shape)
                    dist = distance.euclidean(self.input_face_descriptor, face_descriptor)

                    if dist < 0.6:
                        print("SUCCESS " + image + " " +  str(dist))
                        concurrences.append(image)
                    else:
                        print("FAILURE " + image + " " + str(dist))
            except RuntimeError:
                pass

        return concurrences

    def create_html(self, images):
        html = ['<html><body><h2>This is the input image</h2><img src="' + self.input_image + '"width="200"/><hr/><br>']
        for image in images:
            html += ['<img src="' + image + '"width="200"/>']
        html += ['<h1></h1></body></html>']
        html = '\n'.join(html)

        with open("index.html", "w") as f:
            f.write(html)



#def main():

 #   analyzer = Analyzer('imgs/15370968152210.jpg', 'imgs/')
  #  concurrences = analyzer.detect()
   # analyzer.create_html(concurrences)




#if __name__ == "__main__":
#    main()















