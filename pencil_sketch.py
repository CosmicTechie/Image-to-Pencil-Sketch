import cv2
import numpy as np
def sketch(img):
    image = cv2.imread(img)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    ps=input('Sketch Name with Extension for Saving it:')    
    stat=cv2.imwrite(ps,pencil_sketch)
    sketch=cv2.imread(ps)
    horizontal = np.concatenate((image, sketch), axis=1)
    #cv2.imshow("original image", image)
    #cv2.imshow("pencil sketch", pencil_sketch)
    cv2.imshow("Original Vs Pencil Sketch", horizontal)
    cv2.waitKey(0)
img=input("Enter the image with its extension: ")
sketch(img)
