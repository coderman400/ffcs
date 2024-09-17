import cv2

image = cv2.imread('test4.jpg')
height, width = image.shape[:2]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg', 0)
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
template_h, template_w = template.shape[:2]
top_left = max_loc
bottom_right = (top_left[0] + template_w, height-1)

print(top_left[1],bottom_right[1])

crop = image[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]

cv2.imshow('Template Match', crop)
cv2.imwrite('cropped_image.jpg',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()



