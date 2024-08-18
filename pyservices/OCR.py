import cv2
import pytesseract

image = cv2.imread('image.png')

text = pytesseract.image_to_string(image)
print(text)