import cv2
import numpy as np

# Load image
image = cv2.imread('cropped_image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to binarize the image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 2)

# Detect horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)

# Find contours of the horizontal lines only
contours, _ = cv2.findContours(horizontal_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

height, width = image.shape[:2]

greater = []

# Draw only the contours with width greater than the specified length
for contour in contours:
    # Get the bounding rectangle for the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Check if the width of the contour is greater than the minimum length
    if w == width:
        greater.append((x,y))


image = image[0:max(greater)[1],0:width]
# Show the filtered horizontal lines
cv2.imshow('Filtered Horizontal Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
