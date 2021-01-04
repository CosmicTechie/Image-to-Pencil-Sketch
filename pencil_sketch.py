import cv2
def sketch(img):
    image = cv2.imread(img)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    ps=input('Sketch Name with Extension for Saving it:')    
    stat=cv2.imwrite(ps,pencil_sketch)
    cv2.imshow("original image", image)
    cv2.imshow("pencil sketch", pencil_sketch)
    cv2.waitKey(0)
img=input("Enter the image with its extension: ")
sketch(img)
