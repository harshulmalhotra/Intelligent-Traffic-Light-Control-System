import cv2

img = cv2.imread('original.png')
y=100
x=0
h=507
w==900

crop_img = img[y:y+h, x:x+w]
cv2.imwrite('re_size.png',crop_img)
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)