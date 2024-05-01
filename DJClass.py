import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import glob
import math


class Photo:
    def __init__(self, path):
        self.count = 0
        self.path = (path)
        self.cap = cv2.VideoCapture(0)
        self.all_images = []


        # input photo -> splits
            #returns the split image which can be parsed as seen below
    '''
    def increment():
        glob.glob(count)
        count = count + 1
        return count
    '''

    def Parsing(self):
        #self.count += 1
        for file in glob.glob(self.path):
            image = cv2.imread(file)

            new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            Split = new_image.copy()
                #below is the code to get the color bands
            #Split_blue, Split_green, Split_red = Split[:, :, 0], Split[:, :, 1], Split[:, :, 2]

                #testing for iteration
            print(self.count)
                #return 
            return Split()
        
                #Save if needed
            #cv2.imwrite(f"C:/Users/david/Documents/GitHub/Image-processing-test-V1/Images_BLUE/Split_blue_{count}.bmp", Split_blue)
            #cv2.imwrite(f"C:/Users/david/Documents/GitHub/Image-processing-test-V1/Images_GREEN/Split_green_{count}.bmp", Split_green)
            #cv2.imwrite(f"C:/Users/david/Documents/GitHub/Image-processing-test-V1/Images_RED/Split_red_{count}.bmp", Split_red)
    

        #Will take 1 image from camera
            #this will then be used in order to add the image to a list
                #returns the variable "feed"
    def PhotoTake(self):
        ret, frame = self.cap.read()
        feed = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        return feed


        #will save 1 image from camera to a list
            #this list can be called later to find specific images
    def AppendPhoto(self, feed):
        self.all_images.append(feed)
        print(self.all_images)


        #Saves a photo from the appended list prior
            #Would like to specify which image from the list we will save
                #with the use of self.count
    def SavePhoto(self, feed):
        #for self.count in len(self.all_images):
        self.count = self.count + 1
        cv2.imwrite("C:/Users/david/Desktop/Photo Code/test_dump/frame_%05d.bmp" % self.count, feed)
        



#x = Photo("C:/Users/david/Documents/GitHub/Image-processing-test-V1/test_dump/*")
#x.Parsing()