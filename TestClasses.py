import cv2
import matplotlib.pyplot as plt
import DJClass 

    # Created a class object 
object = DJClass.Photo("C:/Users/david/Desktop/Photo Code/test_dump/*") 
    
    # Calling and printing class methods 

plt.figure(figsize=(10, 10))
#object.Parsing

x = object.PhotoTake()
#print("photo bmp: ", x)
cv2.imshow('frame', x)
object.AppendPhoto(x)
object.SavePhoto(x)

print("break")

cv2.waitKey(1000)
x = object.PhotoTake()
cv2.imshow('frame', x)
object.AppendPhoto(x)
object.SavePhoto(x)

print("break")


cv2.waitKey(1000)
x = object.PhotoTake()
cv2.imshow('frame', x)
object.AppendPhoto(x)
object.SavePhoto(x)

print("break")

cv2.waitKey(1000)
x = object.PhotoTake()
cv2.imshow('frame', x)
object.AppendPhoto(x)
object.SavePhoto(x)

print("break")

cv2.waitKey(1000)
x = object.PhotoTake()
cv2.imshow('frame', x)
object.AppendPhoto(x)
object.SavePhoto(x)




#plt.show()





    
    # Calling the function 


